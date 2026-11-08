"""Generate real sound effects, score and extra character lines with ElevenLabs (cached).

Usage: python audio_gen.py <episode_dir> [--force]
Reads timeline.json:
  "sfx":   [{"id": "alarm", "prompt": "...", "dur": 4.0, ...}]      -> audio/sfx/<id>.mp3
  "music": {"prompt": "...", "length": 80, "file": "audio/music/score.mp3"}
  "lines": [{"file": "audio/vo-05.mp3", "text": "[กลัว สั่น] พี่… เราจะตายไหม",
             "voice": "w3e1Jn4F37O7wDwETrJ9", "pitch": 1.18}]   # child voice = adult female + pitch
Files that already exist are kept (delete one, or pass --force, to regenerate). Uses the
ELEVENLABS_API_KEY from content-studio/.env. Costs ElevenLabs credits: report what was made.
Prompts must describe the sound only — no names of films, games or artists.
"""
import json
import os as _os
import sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
import tl as tl_mod  # noqa: E402
import os
import subprocess
import sys
import urllib.request

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))


def api_key():
    if os.environ.get("ELEVENLABS_API_KEY"):
        return os.environ["ELEVENLABS_API_KEY"].strip('"')
    candidates = [
        os.path.join(ROOT, ".env"),
        os.path.join(ROOT, ".env.local"),
        os.path.join(ROOT, "content-studio", ".env"),
        os.path.join(ROOT, "content-studio", ".env.local"),
        os.path.join(os.getcwd(), ".env")
    ]
    for p in candidates:
        if os.path.exists(p):
            for line in open(p, encoding="utf-8"):
                if line.startswith("ELEVENLABS_API_KEY="):
                    v = line.split("=", 1)[1].strip().strip('"')
                    if v:
                        return v
    sys.exit("ELEVENLABS_API_KEY not found in .env or content-studio/.env")


def post(url, body, out):
    req = urllib.request.Request(url, data=json.dumps(body).encode(), method="POST",
                                 headers={"xi-api-key": api_key(), "Content-Type": "application/json",
                                          "Accept": "audio/mpeg"})
    with urllib.request.urlopen(req, timeout=300) as r:
        data = r.read()
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "wb") as fh:
        fh.write(data)


def dur(path):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path],
                                capture_output=True, text=True).stdout.strip() or 0)


def main():
    ep = os.path.abspath(sys.argv[1])
    force = "--force" in sys.argv
    tl = tl_mod.load(ep)
    extra = [dict(tl["cut_sfx"], id="cut")] if tl.get("cut_sfx", {}).get("prompt") else []
    for s in tl.get("sfx", []) + extra:
        if not s.get("prompt"):
            continue
        out = os.path.join(ep, s.get("file", f"audio/sfx/{s['id']}.mp3"))
        if os.path.exists(out) and not force:
            continue
        post("https://api.elevenlabs.io/v1/sound-generation",
             {"text": s["prompt"], "duration_seconds": min(22, max(0.5, s.get("gen_dur", s.get("dur", 4)))),
              "prompt_influence": s.get("influence", 0.5)}, out)
        print(f"sfx {s['id']}: {dur(out):.2f}s")
    cues = ([tl["music"]] if tl.get("music") else []) + tl.get("music_extra", [])
    for m in cues:
        if not m.get("prompt"):
            continue
        out = os.path.join(ep, m.get("file", "audio/music/score.mp3"))
        if not os.path.exists(out) or force:
            post("https://api.elevenlabs.io/v1/music",
                 {"prompt": m["prompt"], "music_length_ms": int(m.get("length", 60) * 1000)}, out)
            print(f"music {os.path.basename(out)}: {dur(out):.2f}s")
    for ln in tl.get("lines", []):
        out = os.path.join(ep, ln["file"])
        if os.path.exists(out) and not force:
            continue
        raw = out.replace(".mp3", ".raw.mp3")
        post(f"https://api.elevenlabs.io/v1/text-to-speech/{ln['voice']}",
             {"text": ln["text"], "model_id": ln.get("model", "eleven_v3"),
              "voice_settings": {"stability": ln.get("stability", 0.5), "similarity_boost": 0.75}}, raw)
        p = ln.get("pitch", 1.0)
        if p != 1.0:
            sr = 44100
            subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", raw, "-af",
                            f"asetrate={sr}*{p},aresample={sr},atempo={1 / p:.4f}", out], check=True)
            os.remove(raw)
        else:
            os.replace(raw, out)
        print(f"line {ln['file']}: {dur(out):.2f}s")


if __name__ == "__main__":
    main()
