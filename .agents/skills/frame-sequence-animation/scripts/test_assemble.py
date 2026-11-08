"""Real encoding regressions; test art is synthetic, not evidence of GPT quality."""
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

from PIL import Image
from assemble import assemble


class AssembleTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="frame's-ทดสอบ-")
        self.root = Path(self.temp.name)
        self.addCleanup(self.temp.cleanup)
        self.colors = [(255, 0, 0, 255), (0, 255, 0, 255), (0, 0, 255, 255), (255, 255, 0, 255)]
        sheet = Image.new('RGBA', (128, 64), (0, 0, 0, 0))
        for i, color in enumerate(self.colors):
            pose = Image.new('RGBA', (64, 32), color)
            pose.putpixel((0, 0), (0, 0, 0, 0))
            pose.save(self.root / f'pose-{i}.png')
            sheet.paste(pose, ((i % 2) * 64, (i // 2) * 32))
        sheet.save(self.root / 'sheet.png')

    def manifest(self, spec):
        file = self.root / 'shot.json'
        file.write_text(json.dumps(spec), encoding='utf-8')
        return file

    def sheet_spec(self, **extra):
        return {'sheet': {'file': 'sheet.png', 'columns': 2, 'rows': 2}, **extra}

    def video_pixel(self, file, frame, x=32, y=16):
        result = subprocess.run([os.environ.get('FFMPEG_PATH') or 'ffmpeg', '-v', 'error', '-i', str(file),
                                 '-vf', f'select=eq(n\\,{frame}),format=rgb24,crop=1:1:{x}:{y}',
                                 '-frames:v', '1', '-f', 'rawvideo', 'pipe:1'], capture_output=True, check=True)
        return tuple(result.stdout)

    def test_sheet_order_delays_alpha_and_encoded_video(self):
        source = (self.root / 'sheet.png').read_bytes()
        result = assemble(self.manifest(self.sheet_spec(durations_ms=[100, 200, 300, 400], mode='loop')), self.root / 'output')
        self.assertEqual(result['playback_order'], [0, 1, 2, 3])
        self.assertEqual(result['video_holds'], [3, 6, 9, 12])
        self.assertEqual(result['gif_durations_ms'], [100, 200, 300, 400])
        self.assertEqual(result['crop_boxes'][3], [64, 32, 128, 64])
        self.assertEqual((self.root / 'sheet.png').read_bytes(), source)
        for i, color in enumerate(self.colors):
            with Image.open(self.root / f'output/frames/frame-{i:04d}.png') as frame:
                self.assertEqual(frame.getpixel((32, 16)), color)
                self.assertEqual(frame.getpixel((0, 0))[3], 0)
            actual = self.video_pixel(self.root / 'output/preview.mp4', [0, 3, 9, 18][i])
            self.assertTrue(all(abs(a - b) <= 8 for a, b in zip(actual, color[:3])), (i, actual))
        with Image.open(self.root / 'output/animation.gif') as gif:
            self.assertEqual(gif.info['loop'], 0)
            self.assertEqual(gif.convert('RGBA').getpixel((0, 0))[3], 0)
        self.assertEqual(result['status'], 'assembled_not_editorial_approved')

    def test_explicit_order_odd_padding_and_cumulative_rounding(self):
        Image.new('RGBA', (65, 33), 'blue').save(self.root / '10.png')
        Image.new('RGBA', (65, 33), 'red').save(self.root / '2.png')
        spec = {'frames': [{'file': '10.png'}, {'file': '2.png'}], 'duration_ms': 150, 'mode': 'once'}
        result = assemble(self.manifest(spec), self.root / 'ordered')
        self.assertEqual(result['video_holds'], [5, 4])
        self.assertEqual(result['video_duration_ms'], 300)
        video = result['video_metadata']['streams'][0]
        self.assertEqual((video['width'], video['height']), (66, 34))
        with Image.open(self.root / 'ordered/frames/frame-0000.png') as image:
            self.assertEqual(image.getpixel((10, 10)), (0, 0, 255, 255))
        with Image.open(self.root / 'ordered/animation.gif') as gif:
            self.assertNotIn('loop', gif.info)

    def test_pingpong_does_not_double_endpoints(self):
        result = assemble(self.manifest(self.sheet_spec(sheet={'file': 'sheet.png', 'columns': 2, 'rows': 2, 'count': 3},
                                                       duration_ms=100, mode='pingpong')), self.root / 'pingpong')
        self.assertEqual(result['playback_order'], [0, 1, 2, 1])
        self.assertEqual(result['video_frame_count'], 12)

    def test_reject_bad_timing_or_grid_without_output(self):
        for spec in [self.sheet_spec(duration_ms=15), self.sheet_spec(duration_ms=10),
                     self.sheet_spec(sheet={'file': 'sheet.png', 'columns': 3, 'rows': 2}),
                     self.sheet_spec(durations_ms=[100, 200]), self.sheet_spec(fps=True)]:
            with self.subTest(spec=spec), self.assertRaises(ValueError):
                assemble(self.manifest(spec), self.root / 'invalid')
            self.assertFalse((self.root / 'invalid').exists())

    def test_reject_mismatched_frame_dimensions(self):
        Image.new('RGB', (16, 16), 'red').save(self.root / 'small.png')
        spec = {'frames': [{'file': 'pose-0.png'}, {'file': 'small.png'}]}
        with self.assertRaisesRegex(ValueError, 'same dimensions'):
            assemble(self.manifest(spec), self.root / 'invalid')

    def test_existing_output_unchanged(self):
        out = self.root / 'existing'
        out.mkdir()
        (out / 'keep.txt').write_text('retained')
        with self.assertRaisesRegex(ValueError, 'new directory'):
            assemble(self.manifest(self.sheet_spec()), out)
        self.assertEqual((out / 'keep.txt').read_text(), 'retained')

    def test_failed_encoder_records_failure(self):
        with patch.dict(os.environ, {'FFMPEG_PATH': str(self.root / 'missing-ffmpeg.exe')}):
            with self.assertRaises(OSError):
                assemble(self.manifest(self.sheet_spec()), self.root / 'failure')
        receipt = json.loads((self.root / 'failure/receipt.json').read_text(encoding='utf-8'))
        self.assertEqual(receipt['status'], 'failed')
        self.assertTrue(receipt['commands'])
        self.assertTrue((self.root / 'sheet.png').exists())


if __name__ == '__main__':
    unittest.main()
