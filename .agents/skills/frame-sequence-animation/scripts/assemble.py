#!/usr/bin/env python3
"""Assemble an explicit pose manifest or uniform sprite sheet; no provider calls."""
import argparse
from fractions import Fraction
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

from PIL import Image, ImageColor, ImageDraw, ImageOps


def integer(value, label, low, high):
    if type(value) is not int or not low <= value <= high:
        raise ValueError(f'{label} must be an integer in {low}..{high}')
    return value


def delay(value):
    value = integer(value, 'duration_ms', 10, 60000)
    if value % 10:
        raise ValueError('duration_ms must be a multiple of 10 (GIF timing unit)')
    return value


def sha256(file):
    with file.open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest() if hasattr(hashlib, 'file_digest') else hashlib.sha256(stream.read()).hexdigest()


def load_poses(manifest, base):
    if ('sheet' in manifest) == ('frames' in manifest):
        raise ValueError('Supply exactly one of sheet or frames')
    poses, sources, crops = [], [], []
    total_pixels = 0

    def read(file):
        nonlocal total_pixels
        source = (base / file).resolve()
        with Image.open(source) as image:
            if getattr(image, 'is_animated', False):
                raise ValueError('Input poses must be still images, not an animation')
            total_pixels += image.width * image.height
            if total_pixels > 64000000:
                raise ValueError('Short-animation input exceeds 64 million decoded pixels')
            result = ImageOps.exif_transpose(image).convert('RGBA')
        sources.append({'file': str(source), 'sha256': sha256(source)})
        return result

    default = delay(manifest.get('duration_ms', 150))
    if 'sheet' in manifest:
        sheet = manifest['sheet']
        cols = integer(sheet['columns'], 'columns', 1, 256)
        rows = integer(sheet['rows'], 'rows', 1, 256)
        count = integer(sheet.get('count', cols * rows), 'count', 2, min(256, cols * rows))
        image = read(sheet['file'])
        if image.width % cols or image.height % rows:
            raise ValueError('Sheet dimensions must divide exactly by columns and rows')
        w, h = image.width // cols, image.height // rows
        for i in range(count):
            x, y = (i % cols) * w, (i // cols) * h
            box = (x, y, x + w, y + h)
            poses.append(image.crop(box))
            crops.append(list(box))
        durations = [delay(d) for d in manifest.get('durations_ms', [default] * count)]
        if len(durations) != count:
            raise ValueError('durations_ms must contain one delay per selected sheet cell')
    else:
        frames = manifest['frames']
        integer(len(frames), 'frame count', 2, 256)
        durations = []
        for frame in frames:
            poses.append(read(frame['file']))
            durations.append(delay(frame.get('duration_ms', default)))
        if any(p.size != poses[0].size for p in poses):
            raise ValueError('Every pose must have the same dimensions')
    return poses, durations, sources, crops


def assemble(manifest_file, output):
    manifest_file, output = manifest_file.resolve(), output.resolve()
    if output.exists():
        raise ValueError(f'Output must be a new directory: {output}')
    manifest = json.loads(manifest_file.read_text(encoding='utf-8-sig'))
    poses, durations, sources, crops = load_poses(manifest, manifest_file.parent)
    fps = integer(manifest.get('fps', 30), 'fps', 1, 60)
    mode = manifest.get('mode', 'once')
    if mode not in ('once', 'loop', 'pingpong'):
        raise ValueError('mode must be once, loop or pingpong')
    background = ImageColor.getrgb(manifest.get('background', '#101820'))
    if len(background) != 3:
        raise ValueError('background must be an opaque RGB color')
    order = list(range(len(poses)))
    if mode == 'pingpong':
        order += list(range(len(poses) - 2, 0, -1))
    timeline_ms = sum(durations[i] for i in order)
    if timeline_ms > 60000:
        raise ValueError('One short-animation cycle must not exceed 60 seconds')
    holds, elapsed, previous = [], 0, 0
    for i in order:
        elapsed += durations[i]
        boundary = (elapsed * fps + 500) // 1000  # cumulative half-up rounding
        if boundary <= previous:
            raise ValueError('A pose would receive zero MP4 frames; increase duration or fps')
        holds.append(boundary - previous)
        previous = boundary

    output.mkdir(parents=True)
    receipt = {
        'status': 'assembling', 'manifest': str(manifest_file),
        'manifest_sha256': sha256(manifest_file), 'inputs': sources,
        'provenance': manifest.get('provenance'), 'unique_pose_count': len(poses),
        'source_size': list(poses[0].size), 'crop_boxes': crops,
        'mode': mode, 'playback_order': order, 'source_durations_ms': durations,
        'requested_duration_ms': timeline_ms, 'fps': fps,
        'video_holds': holds, 'video_frame_count': sum(holds),
        'video_duration_ms': sum(holds) * 1000 / fps,
        'background': list(background), 'commands': [],
    }

    def command(args):
        record = {'args': args}
        receipt['commands'].append(record)
        result = subprocess.run(args, capture_output=True, timeout=300, check=False,
                                **({'creationflags': subprocess.CREATE_NO_WINDOW} if os.name == 'nt' else {}))
        record.update(exit_code=result.returncode, stderr=result.stderr.decode('utf-8', errors='replace')[-6000:])
        if result.returncode:
            raise RuntimeError(f'Command failed ({result.returncode}): {args[0]}: {record["stderr"]}')
        return result.stdout

    try:
        frame_dir = output / 'frames'
        frame_dir.mkdir()
        for i, pose in enumerate(poses):
            pose.save(frame_dir / f'frame-{i:04d}.png')
        cols = min(4, len(poses))
        sheet = Image.new('RGB', (cols * 200, ((len(poses) + cols - 1) // cols) * 160), background)
        draw = ImageDraw.Draw(sheet)
        for i, pose in enumerate(poses):
            thumb = pose.copy()
            thumb.thumbnail((192, 128))
            x, y = (i % cols) * 200, (i // cols) * 160
            sheet.paste(thumb, (x + (200 - thumb.width) // 2, y), thumb)
            draw.text((x + 4, y + 132), f'{i:03d} / {durations[i]} ms', fill='white', stroke_width=1, stroke_fill='black')
        sheet.save(output / 'contact-sheet.png')

        gif = output / 'animation.gif'
        gif_poses = [poses[i] for i in order]
        gif_poses[0].save(gif, format='GIF', save_all=True, append_images=gif_poses[1:],
                          duration=[durations[i] for i in order], disposal=2, optimize=False,
                          **({'loop': 0} if mode != 'once' else {}))
        with Image.open(gif) as decoded:
            actual_delays = []
            for i in range(decoded.n_frames):
                decoded.seek(i)
                actual_delays.append(decoded.info['duration'])
        receipt['gif_durations_ms'] = actual_delays
        if sum(actual_delays) != timeline_ms:
            raise RuntimeError('Encoded GIF duration differs from the requested cycle')

        ffmpeg = os.environ.get('FFMPEG_PATH') or 'ffmpeg'
        ffprobe = os.environ.get('FFPROBE_PATH') or 'ffprobe'
        with tempfile.TemporaryDirectory(prefix='encode-', dir=output) as temp:
            temp = Path(temp)
            for i, pose in enumerate(poses):
                # Even-size matte for H.264, without stretching the source image.
                width, height = pose.size
                rgb = Image.new('RGB', (width + width % 2, height + height % 2), background)
                rgb.paste(pose, (0, 0), pose)
                rgb.save(temp / f'pose-{i:04d}.png')
            n = 0
            for i, hold in zip(order, holds):
                for _ in range(hold):
                    target = temp / f'play-{n:06d}.png'
                    try:
                        os.link(temp / f'pose-{i:04d}.png', target)
                    except OSError:
                        shutil.copyfile(temp / f'pose-{i:04d}.png', target)
                    n += 1
            video = output / 'preview.mp4'
            command([ffmpeg, '-hide_banner', '-loglevel', 'error', '-nostdin', '-n',
                     '-framerate', str(fps), '-i', str(temp / 'play-%06d.png'),
                     '-frames:v', str(n), '-an', '-c:v', 'libx264', '-crf', '18',
                     '-pix_fmt', 'yuv420p', '-movflags', '+faststart', str(video)])
        metadata = json.loads(command([ffprobe, '-v', 'error', '-show_streams', '-show_format', '-of', 'json', str(video)]))
        stream = next(s for s in metadata['streams'] if s['codec_type'] == 'video')
        expected_size = [v + v % 2 for v in poses[0].size]
        if ([stream['width'], stream['height']] != expected_size or
                int(stream['nb_frames']) != sum(holds) or
                Fraction(stream['r_frame_rate']) != fps or
                abs(float(stream['duration']) - sum(holds) / fps) > 0.002):
            raise RuntimeError('Encoded MP4 dimensions, frame count or timing differ from the plan')
        command([ffmpeg, '-v', 'error', '-nostdin', '-xerror', '-i', str(video), '-map', '0:v:0', '-f', 'null', '-'])
        receipt.update(status='assembled_not_editorial_approved', video_metadata=metadata,
                       checks=['GIF duration', 'MP4 dimensions/FPS/frame count/duration', 'full MP4 decode'])
        receipt['outputs'] = {name: {'file': str(output / name), 'sha256': sha256(output / name)}
                              for name in ('animation.gif', 'preview.mp4', 'contact-sheet.png')}
    except Exception as error:
        receipt.update(status='failed', error=str(error))
        raise
    finally:
        (output / 'receipt.json').write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    return receipt


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--manifest', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    try:
        receipt = assemble(args.manifest, args.out)
    except (OSError, ValueError, KeyError, TypeError, RuntimeError, subprocess.TimeoutExpired) as error:
        print(f'Assembly failed: {error}', file=sys.stderr)
        return 1
    print(json.dumps({'status': receipt['status'], 'out': str(args.out.resolve()),
                      'poses': receipt['unique_pose_count'], 'duration_ms': receipt['requested_duration_ms']}))
    return 0


if __name__ == '__main__':
    sys.exit(main())
