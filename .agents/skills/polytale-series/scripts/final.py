"""PolyTale final mux: shots + overlay + voice lines + sound bed -> publishable MP4 (-14 LUFS).

Usage: python final.py <episode_dir> [out.mp4]      # default <episode_dir>/render/<id>.mp4
Needs render/shots.mp4 (shots.py), render/overlay.ass (subs.py), audio/sfx-bed.wav (sound.py)
and the voice files listed in timeline.json "vo": [{"file": "audio/vo-01.mp3", "at": 0.3}, ...].
Prints duration, loudness and true peak after writing.
"""
import json
import os as _os
import sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
import tl as tl_mod  # noqa: E402
import os
import re
import shutil
import subprocess
import sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
FONT_CANDIDATES = [
    os.path.join(ROOT, 'assets', 'fonts'),
    os.path.join(ROOT, 'content-studio', 'assets', 'fonts'),
    os.path.join(os.path.dirname(__file__), '..', '..', '..', 'assets', 'fonts'),
]
FONTS = next((d for d in FONT_CANDIDATES if os.path.exists(d)), FONT_CANDIDATES[0])


def main():
    ep = os.path.abspath(sys.argv[1])
    tl = tl_mod.load(ep)
    out = os.path.abspath(sys.argv[2]) if len(sys.argv) > 2 else os.path.join(ep, "render", f"{tl.get('id', 'episode')}.mp4")
    fonts = os.path.join(ep, "render", "fonts")
    os.makedirs(fonts, exist_ok=True)
    for f in os.listdir(FONTS):
        if f.startswith("Kanit-") and f.endswith(".ttf") and not os.path.exists(os.path.join(fonts, f)):
            shutil.copy(os.path.join(FONTS, f), fonts)
    vo = tl["vo"]
    inputs = ["-i", "render/shots.mp4"]
    parts = ["[0:v]ass=render/overlay.ass:fontsdir=render/fonts:shaping=complex[v]"]
    idx = 1
    vo_labels = []
    for v in vo:
        inputs += ["-i", v["file"]]
        ms = int(v["at"] * 1000)
        g = v.get("gain", 1.0)
        parts.append(f"[{idx}:a]aformat=sample_rates=48000:channel_layouts=stereo,volume={g},adelay={ms}|{ms}[vo{idx}]")
        vo_labels.append(f"[vo{idx}]")
        idx += 1
    bed_labels = []
    bed_file = tl.get("sfx_bed", "audio/sfx-bed.wav")
    if bed_file and os.path.exists(os.path.join(ep, bed_file)):
        inputs += ["-i", bed_file]
        parts.append(f"[{idx}:a]aformat=sample_rates=48000:channel_layouts=stereo,volume={tl.get('sfx_gain', 0.55)}[b{idx}]")
        bed_labels.append(f"[b{idx}]")
        idx += 1
    for s_ in tl.get("sfx", []):
        f = s_.get("file", f"audio/sfx/{s_['id']}.mp3")
        if not os.path.exists(os.path.join(ep, f)):
            print("missing sfx", f, "- run audio_gen.py")
            continue
        inputs += ["-i", f]
        ms = int(s_["at"] * 1000)
        chain = f"[{idx}:a]aformat=sample_rates=48000:channel_layouts=stereo"
        if s_.get("dur"):
            chain += f",atrim=0:{s_['dur']}"
        if s_.get("fade_in"):
            chain += f",afade=t=in:d={s_['fade_in']}"
        if s_.get("fade_out") and s_.get("dur"):
            chain += f",afade=t=out:st={max(0, s_['dur'] - s_['fade_out'])}:d={s_['fade_out']}"
        chain += f",volume={s_.get('gain', 0.6)},adelay={ms}|{ms}[b{idx}]"
        parts.append(chain)
        bed_labels.append(f"[b{idx}]")
        idx += 1
    cut_labels = []
    cs = tl.get("cut_sfx")  # one whoosh on every cut except skipped shots: {file, gain, lead, skip}
    if cs and os.path.exists(os.path.join(ep, cs["file"])):
        for sh in tl["shots"][1:]:
            if sh["id"] in cs.get("skip", []) or sh.get("cut_sfx") is False:
                continue
            inputs += ["-i", cs["file"]]
            ms = max(0, int((sh["start"] - cs.get("lead", 0.3)) * 1000))
            g = sh.get("cut_gain", cs.get("gain", 0.35))
            parts.append(f"[{idx}:a]aformat=sample_rates=48000:channel_layouts=stereo,volume={g},adelay={ms}|{ms}[c{idx}]")
            cut_labels.append(f"[c{idx}]")  # not ducked: transitions must stay audible
            idx += 1
    m = tl.get("music")
    if m and os.path.exists(os.path.join(ep, m.get("file", "audio/music/score.mp3"))):
        inputs += ["-i", m.get("file", "audio/music/score.mp3")]
        ms = int(m.get("at", 0) * 1000)
        chain = f"[{idx}:a]aformat=sample_rates=48000:channel_layouts=stereo"
        if m.get("dur"):
            chain += f",atrim=0:{m['dur']},afade=t=out:st={max(0, m['dur'] - m.get('fade_out', 0.3))}:d={m.get('fade_out', 0.3)}"
        chain += f",afade=t=in:d={m.get('fade_in', 1.0)},volume={m.get('gain', 0.35)},adelay={ms}|{ms}[b{idx}]"
        parts.append(chain)
        bed_labels.append(f"[b{idx}]")
        idx += 1
    parts.append("".join(vo_labels) + f"amix=inputs={len(vo_labels)}:normalize=0:dropout_transition=0,volume={tl.get('vo_gain', 1.0)},asplit[vo1][vo2]")
    # Everything is padded so no filter stops early (sidechaincompress ends with its shortest input).
    duck = tl.get("duck", {"ratio": 3, "threshold": 0.05})
    if bed_labels:
        parts.append("".join(bed_labels) + f"amix=inputs={len(bed_labels)}:normalize=0:dropout_transition=0,apad[bed]")
        parts.append("[vo2]apad[vo2p]")
        parts.append(f"[bed][vo2p]sidechaincompress=threshold={duck['threshold']}:ratio={duck['ratio']}:attack=15:release=350[bedd]")
        mix_in = ["[bedd]", "[vo1]"] + cut_labels
    else:
        parts.append("[vo2]anullsink")
        mix_in = ["[vo1]"] + cut_labels
    parts.append("".join(mix_in) + f"amix=inputs={len(mix_in)}:normalize=0:dropout_transition=0,"
                 f"atrim=0:{tl['length']:.3f},loudnorm=I=-14:TP=-1.5:LRA=11,apad[a]")
    cmd = (["ffmpeg", "-y", "-loglevel", "error"] + inputs
           + ["-filter_complex", ";".join(parts), "-map", "[v]", "-map", "[a]",
              "-c:v", "libx264", "-crf", "18", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k",
              "-ar", "48000", "-movflags", "+faststart", "-shortest", out])
    subprocess.run(cmd, cwd=ep, check=True)
    dur = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", out],
                         capture_output=True, text=True).stdout.strip()
    meas = subprocess.run(["ffmpeg", "-hide_banner", "-i", out, "-af", "ebur128=peak=true", "-f", "null", "-"],
                          capture_output=True, text=True).stderr
    i_lufs = re.findall(r"I:\s+(-?[\d.]+) LUFS", meas)
    peak = re.findall(r"Peak:\s+(-?[\d.]+) dBFS", meas)
    print(f"wrote {out}\nduration {dur}s | loudness {i_lufs[-1] if i_lufs else '?'} LUFS | true peak {peak[-1] if peak else '?'} dBFS")


if __name__ == "__main__":
    main()

