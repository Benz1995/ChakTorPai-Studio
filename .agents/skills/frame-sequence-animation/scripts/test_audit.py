import json
from pathlib import Path
import tempfile
import unittest

from PIL import Image, ImageDraw
from assemble import assemble
from audit import audit


class AuditTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(prefix='pose-audit-')
        self.addCleanup(self.tmp.cleanup)
        self.root=Path(self.tmp.name)
        for i,color in enumerate(['red','blue']):
            im=Image.new('RGBA',(40,40))
            ImageDraw.Draw(im).rectangle((10,5,29,34),fill=color)
            im.save(self.root/f'{i}.png')
        self.manifest=self.root/'shot.json'

    def write(self,extra=None):
        data={'frames':[{'file':f'{i%2}.png'} for i in range(16)],'duration_ms':120,'mode':'loop','fps':30}
        data.update(extra or {})
        self.manifest.write_text(json.dumps(data),encoding='utf-8')

    def test_resolution_and_duplicate_count_without_mutating_inputs(self):
        self.write()
        before=(self.root/'0.png').read_bytes()
        report=audit(self.manifest,60,16)
        self.assertEqual(report['common_subject_bbox'],[10,5,30,35])
        self.assertEqual(report['native_subject_height_px'],30)
        self.assertEqual(report['display_scale'],2)
        self.assertEqual(report['distinct_raster_count'],2)
        self.assertEqual(report['pose_entries'],16)
        self.assertEqual(report['frames'][0]['edge_visible_pixels'],0)
        self.assertEqual(before,(self.root/'0.png').read_bytes())

    def test_real_encoded_receipt_and_stale_input_rejection(self):
        # 125ms planned drawing rate represented as alternating GIF-compatible delays.
        self.write({'frames':[{'file':f'{i%2}.png','duration_ms':120 if i%2==0 else 130} for i in range(16)]})
        assemble(self.manifest,self.root/'encoded')
        receipt=self.root/'encoded/receipt.json'
        report=audit(self.manifest,30,16,receipt)
        self.assertEqual(report['timing']['encoded_cycle_ms'],2000)
        self.assertEqual(set(report['timing']['frame_holds']),{3,4})
        self.assertEqual(report['shot_cycle_equivalents'],8)
        completed=json.loads(receipt.read_text(encoding='utf-8'))
        failed={**completed,'status':'failed'}
        receipt.write_text(json.dumps(failed),encoding='utf-8')
        with self.assertRaisesRegex(ValueError,'completed assembly'):
            audit(self.manifest,30,16,receipt)
        receipt.write_text(json.dumps(completed),encoding='utf-8')
        Image.new('RGBA',(40,40),'green').save(self.root/'0.png')
        with self.assertRaisesRegex(ValueError,'stale'):
            audit(self.manifest,30,16,receipt)

    def test_empty_frames_and_edge_pixels_are_diagnostics(self):
        self.write()
        Image.new('RGBA',(40,40)).save(self.root/'0.png')
        report=audit(self.manifest,30)
        self.assertIsNone(report['frames'][0]['visible_bbox'])
        Image.new('RGBA',(40,40),'blue').save(self.root/'1.png')
        self.assertGreater(audit(self.manifest,30)['frames'][1]['edge_visible_pixels'],0)

    def test_bad_display_size_is_rejected(self):
        self.write()
        for value in [0,-1,float('nan'),float('inf')]:
            with self.subTest(value=value),self.assertRaises(ValueError):
                audit(self.manifest,value)


if __name__=='__main__':
    unittest.main()
