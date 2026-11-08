"""Remove the speech Veo adds to a Flow clip and keep the music/ambience bed.

Usage (global Python with demucs 4 + soundfile; ffmpeg on PATH):
  python -X utf8 strip_speech.py <clip.mp4> <out.wav> [--video <out.mp4>]

Decodes with ffmpeg (the demucs CLI save path fails on this machine's torchaudio/torchcodec),
separates with htdemucs through the Python API and writes drums+bass+other as <out.wav>.
With --video, also writes <out.mp4>: the original picture stream copied with the new bed as AAC.
"""
import argparse
import subprocess
import sys
import tempfile
from pathlib import Path

import numpy as np
import soundfile as sf
import torch
from demucs.apply import apply_model
from demucs.pretrained import get_model


def decode(src: Path, rate: int, wav: Path) -> None:
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(src), "-vn", "-ac", "2", "-ar", str(rate),
                    "-c:a", "pcm_f32le", str(wav)], check=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("src", type=Path)
    parser.add_argument("out", type=Path)
    parser.add_argument("--video", type=Path)
    args = parser.parse_args()

    model = get_model("htdemucs").eval()
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model.to(device)
    with tempfile.TemporaryDirectory() as tmp:
        wav_path = Path(tmp) / "in.wav"
        decode(args.src, model.samplerate, wav_path)
        audio, rate = sf.read(str(wav_path), dtype="float32", always_2d=True)
    wav = torch.from_numpy(audio.T.copy())
    ref = wav.mean(0)
    mean, std = ref.mean(), ref.std() + 1e-8
    with torch.no_grad():
        sources = apply_model(model, ((wav - mean) / std)[None].to(device), split=True, overlap=0.25)[0]
    sources = sources.cpu() * std + mean
    keep = [i for i, name in enumerate(model.sources) if name != "vocals"]
    bed = sources[keep].sum(0).numpy().T
    vocals = sources[model.sources.index("vocals")].numpy()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    sf.write(str(args.out), bed, rate, subtype="FLOAT")
    removed = float(np.sqrt(np.mean(vocals ** 2)))
    kept = float(np.sqrt(np.mean(bed ** 2)))
    print(f"wrote {args.out} ({bed.shape[0] / rate:.2f} s, {device}); vocal RMS removed {removed:.4f}, bed RMS {kept:.4f}")

    if args.video:
        args.video.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(args.src), "-i", str(args.out), "-map", "0:v:0",
                        "-map", "1:a:0", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest", str(args.video)],
                       check=True)
        print(f"wrote {args.video}")


if __name__ == "__main__":
    sys.exit(main())
