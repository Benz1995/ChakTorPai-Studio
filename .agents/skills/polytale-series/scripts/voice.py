"""Copy Content Studio voice lines into an episode and check what the Thai ASR hears.

Usage: python voice.py <episode_dir> <contentId> <sceneId> [<sceneId> ...] [--no-asr]
Copies the newest content-studio/storage/tts/<contentId>/<sceneId>-*.mp3 to
<episode_dir>/audio/vo-01.mp3, vo-02.mp3 ... in the order given, prints each duration,
then transcribes each with thonburian-whisper-th-large-v3 on CPU (slow but reliable) and
prints the transcript next to the file so the readings can be compared with the script.
"""
import glob
import json
import os
import shutil
import subprocess
import sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
CS = os.path.join(ROOT, "content-studio")


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    asr = "--no-asr" not in sys.argv
    ep, content, scenes = os.path.abspath(args[0]), args[1], args[2:]
    os.makedirs(os.path.join(ep, "audio"), exist_ok=True)
    env = dict(os.environ, RECAP_ASR_MODEL="thonburian-whisper-th-large-v3", RECAP_ASR_DEVICE="cpu",
               PYTHONIOENCODING="utf-8")
    for i, sid in enumerate(scenes, start=1):
        files = sorted(glob.glob(os.path.join(CS, "storage", "tts", content, f"{sid}-*.mp3")), key=os.path.getmtime)
        if not files:
            sys.exit(f"no voice file for scene {sid}; run voice_content first")
        dst = os.path.join(ep, "audio", f"vo-{i:02d}.mp3")
        shutil.copy(files[-1], dst)
        dur = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", dst],
                             capture_output=True, text=True).stdout.strip()
        line = f"vo-{i:02d}.mp3  {float(dur):.2f}s"
        if asr:
            js = dst.replace(".mp3", ".asr.json")
            subprocess.run([sys.executable, "scripts/recap-transcribe.py", "--input", dst, "--output", js],
                           cwd=CS, env=env, capture_output=True)
            try:
                d = json.load(open(js, encoding="utf-8"))
                text = d.get("text") or " ".join(s.get("text", "") for s in d.get("segments", []))
            except (OSError, ValueError):
                text = "(ASR failed — run recap-transcribe.py --probe)"
            line += f"  ASR: {text}"
        print(line)


if __name__ == "__main__":
    main()
