#!/usr/bin/env python3
"""Read-only pose-resolution, alpha-border and timing audit; not creative approval."""
import argparse
from collections import Counter
import hashlib
import json
import math
from pathlib import Path
import sys

from assemble import integer, load_poses, sha256


def audit(manifest_file, display_height, shot_seconds=None, receipt_file=None, threshold=128):
    if not math.isfinite(display_height) or display_height <= 0:
        raise ValueError('display-height must be a finite positive pixel height')
    if shot_seconds is not None and (not math.isfinite(shot_seconds) or shot_seconds <= 0):
        raise ValueError('shot-seconds must be finite and positive')
    integer(threshold, 'alpha-threshold', 0, 254)
    manifest_file = manifest_file.resolve()
    manifest = json.loads(manifest_file.read_text(encoding='utf-8-sig'))
    poses, durations, inputs, _ = load_poses(manifest, manifest_file.parent)
    mode = manifest.get('mode', 'once')
    if mode not in ('once', 'loop', 'pingpong'):
        raise ValueError('Invalid playback mode')
    order = list(range(len(poses)))
    if mode == 'pingpong':
        order += list(range(len(poses)-2, 0, -1))
    cycle_ms = sum(durations[i] for i in order)
    frames, hashes, boxes = [], set(), []
    for i, pose in enumerate(poses):
        alpha = pose.getchannel('A')
        histogram = alpha.histogram()
        box = alpha.point(lambda a: 255 if a > threshold else 0).getbbox()
        if box:
            boxes.append(box)
        width, height = pose.size
        edge = [alpha.getpixel((x,y)) for x in range(width) for y in (0,height-1)]
        edge += [alpha.getpixel((x,y)) for y in range(1,height-1) for x in (0,width-1)]
        frames.append({'pose':i, 'cell_size':list(pose.size), 'visible_bbox':list(box) if box else None,
                       'zero_alpha_fraction':histogram[0]/(width*height),
                       'near_opaque_fraction':sum(histogram[250:])/(width*height),
                       'alpha_range':list(alpha.getextrema()),
                       'edge_mean_alpha':sum(edge)/len(edge),
                       'edge_visible_pixels':sum(a>threshold for a in edge)})
        hashes.add(hashlib.sha256(pose.tobytes()).hexdigest())
    union = None if not boxes else (min(b[0] for b in boxes), min(b[1] for b in boxes),
                                    max(b[2] for b in boxes), max(b[3] for b in boxes))
    native_height = None if union is None else union[3]-union[1]
    warnings = []
    if native_height and display_height > native_height:
        warnings.append('Subject pixels are enlarged; export resolution does not establish native subject detail.')
    if len(hashes) < len(poses):
        warnings.append('Some source poses are pixel-identical; entry count is not distinct drawing count.')
    if any(f['visible_bbox'] is None for f in frames):
        warnings.append('At least one pose is empty at the selected alpha threshold; inspect intent.')
    if any(f['edge_visible_pixels'] for f in frames):
        warnings.append('Visible pixels touch cell edges; inspect clipping or intended edge contact.')
    timing = {'basis':'manifest only; no encoded timing verified',
              'cycle_ms':cycle_ms,'pose_entries_per_second':len(order)*1000/cycle_ms}
    if receipt_file:
        receipt = json.loads(receipt_file.read_text(encoding='utf-8'))
        if receipt.get('status') != 'assembled_not_editorial_approved':
            raise ValueError('Assembly receipt does not record a completed assembly')
        if receipt.get('manifest_sha256') != sha256(manifest_file) or receipt.get('inputs') != inputs:
            raise ValueError('Assembly receipt is stale or belongs to different inputs')
        holds = receipt['video_holds']
        if receipt.get('playback_order') != order or len(holds) != len(order) or any(type(n) is not int or n <= 0 for n in holds):
            raise ValueError('Assembly receipt has inconsistent playback holds')
        fps = integer(receipt['fps'], 'receipt fps', 1, 60)
        timing.update(basis='matching assembly receipt (encode QA remains in that receipt)',
                      fps=fps, frame_holds=holds, hold_histogram=dict(Counter(holds)),
                      uniform_holds=len(set(holds))==1, encoded_cycle_ms=sum(holds)*1000/fps)
        if len(set(durations))==1 and len(set(holds))>1:
            warnings.append('Equal drawing times become unequal video holds at this FPS; review cadence.')
    cycles = None if shot_seconds is None else shot_seconds*1000/cycle_ms
    if cycles and cycles>1 and mode!='once':
        warnings.append('Shot spans multiple cycle lengths; this is a repetition-budget estimate, not proof of the final edit.')
    return {'schema_version':1,'status':'diagnostic_only_not_editorial_approval',
            'manifest':str(manifest_file),'manifest_sha256':sha256(manifest_file),'inputs':inputs,
            'pose_entries':len(poses),'distinct_raster_count':len(hashes),'alpha_threshold':threshold,
            'common_subject_bbox':list(union) if union else None,'native_subject_height_px':native_height,
            'display_height_px':display_height,'display_scale':display_height/native_height if native_height else None,
            'timing':timing,'shot_seconds':shot_seconds,'shot_cycle_equivalents':cycles,
            'warnings':warnings,'frames':frames,
            'limits':'Bounds depend on alpha threshold, not semantic anatomy. Border alpha cannot diagnose a matte by itself. No pose alignment, contact, identity, sound, actual edit repetition or artistic quality approval is inferred.'}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--manifest',type=Path,required=True)
    p.add_argument('--display-height',type=float,required=True,help='planned common-crop subject height on the final canvas')
    p.add_argument('--shot-seconds',type=float)
    p.add_argument('--receipt',type=Path)
    p.add_argument('--alpha-threshold',type=int,default=128)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args()
    try:
        if a.out.resolve()==a.manifest.resolve() or a.out.exists():
            raise ValueError('Audit output must be a new file; sources/reports are never overwritten')
        report=audit(a.manifest,a.display_height,a.shot_seconds,a.receipt,a.alpha_threshold)
        # Avoid truncation on a concurrent invocation that creates the same output.
        a.out.parent.mkdir(parents=True,exist_ok=True)
        with a.out.open('x',encoding='utf-8') as out:
            json.dump(report,out,ensure_ascii=False,indent=2);out.write('\n')
    except (OSError,ValueError,KeyError,TypeError) as error:
        print(f'Audit failed: {error}',file=sys.stderr)
        return 1
    print(json.dumps({k:report[k] for k in ['status','pose_entries','native_subject_height_px','display_scale','shot_cycle_equivalents','warnings']}))
    return 0


if __name__=='__main__':
    sys.exit(main())
