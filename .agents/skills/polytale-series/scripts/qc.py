"""PolyTale review sheet: one frame from the middle of each shot plus full-size subtitle crops.

Usage: python qc.py <episode_dir> [video.mp4]      # default render/<id>.mp4
Writes review/strip.png (all shots side by side, platform UI zones tinted red) and review/sub-<shot>.png (bottom 700 px at
full size, to check Thai tone marks and layout). Look at every file before delivering.
"""
import json
import os as _os
import sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
import tl as tl_mod  # noqa: E402
import os
import subprocess
import sys


# Platform UI zones (IG Reels / TikTok / Shorts): header, caption + buttons, right-side buttons.
# Faces, subtitles and cards must stay out of the red areas.
SAFE = ("drawbox=x=0:y=0:w=1080:h=220:color=red@0.16:t=fill,"
        "drawbox=x=0:y=1540:w=1080:h=380:color=red@0.16:t=fill,"
        "drawbox=x=940:y=900:w=140:h=640:color=red@0.16:t=fill")


def main():
    ep = os.path.abspath(sys.argv[1])
    tl = tl_mod.load(ep)
    vid = os.path.abspath(sys.argv[2]) if len(sys.argv) > 2 else os.path.join(ep, "render", f"{tl.get('id', 'episode')}.mp4")
    rv = os.path.join(ep, "review")
    os.makedirs(rv, exist_ok=True)
    frames = []
    for s in tl["shots"]:
        mid = s["start"] + (s["end"] - s["start"]) * 0.6
        png = os.path.join(rv, f"mid-{s['id']}.png")
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-ss", f"{mid:.2f}", "-i", vid, "-frames:v", "1",
                        "-vf", SAFE + ",scale=270:-1", png], check=True)
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-ss", f"{mid:.2f}", "-i", vid, "-frames:v", "1",
                        "-vf", "crop=1080:700:0:1150", os.path.join(rv, f"sub-{s['id']}.png")], check=True)
        frames.append(png)
    from PIL import Image
    ims = [Image.open(f) for f in frames]
    cols = min(6, len(ims))
    rows = (len(ims) + cols - 1) // cols
    w, h = ims[0].size
    sheet = Image.new("RGB", (cols * w, rows * h))
    for i, im in enumerate(ims):
        sheet.paste(im, ((i % cols) * w, (i // cols) * h))
    sheet.save(os.path.join(rv, "strip.png"))
    # Fast subtitle sheet: overlay only, on grey, at the middle of every subtitle (catches overlaps).
    fps = 10
    picks = [int((x["start"] + x["end"]) / 2 * fps) for x in tl["subs"]]
    if picks:
        sel = "+".join(f"eq(n\,{n})" for n in picks)
        tmp = os.path.join(rv, "subcheck")
        os.makedirs(tmp, exist_ok=True)
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-f", "lavfi", "-i",
                        f"color=c=0x3a3a3a:s=1080x1920:r={fps}:d={tl['length']}",
                        "-vf", f"ass=render/overlay.ass:fontsdir=render/fonts:shaping=complex,select='{sel}',crop=1080:620:0:1200,scale=540:-1",
                        "-vsync", "0", os.path.join(tmp, "s%03d.png")], cwd=ep, check=True)
        subs_png = sorted(f for f in os.listdir(tmp) if f.endswith(".png"))
        tiles = [Image.open(os.path.join(tmp, f)) for f in subs_png]
        if tiles:
            cw, ch = tiles[0].size
            cols2 = 3
            sheet2 = Image.new("RGB", (cols2 * cw, ((len(tiles) + cols2 - 1) // cols2) * ch))
            for i, im in enumerate(tiles):
                sheet2.paste(im, ((i % cols2) * cw, (i // cols2) * ch))
            sheet2.save(os.path.join(rv, "subs-sheet.png"))
    print("wrote", os.path.join(rv, "subs-sheet.png"))
    print("wrote", os.path.join(rv, "strip.png"), "and", len(frames), "subtitle crops")


if __name__ == "__main__":
    main()
