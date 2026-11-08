#!/usr/bin/env python3
"""ChakTorPai Studio - Complete Episode Render Runner

Runs the full production pipeline for any PolyTale episode:
1. tl.py        - Resolves relative shot timings and voiceover lengths
2. audio_gen.py - Synthesizes SFX, music bed, and character dialogue (cached)
3. subs.py      - Generates bilingual Kanit subtitles & overlay (ASS)
4. shots.py     - Composites 1080x1920 30fps video frames (silent MP4)
5. final.py     - Final mux: video + subtitles + voices + sound bed (-14 LUFS)
6. qc.py        - Generates review contact sheets and safe-zone QC strips

Usage:
    python scripts/render_episode.py series/day0/ep01
    python scripts/render_episode.py series/day0/ep02
    python scripts/render_episode.py series/day0/ep02_badend
"""

import os
import sys
import subprocess
import time

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SCRIPTS = os.path.join(ROOT, ".agents", "skills", "polytale-series", "scripts")


def run_step(step_name, script_path, ep_dir, optional=False):
    print(f"\n=======================================================")
    print(f"[*] Running {step_name}: {os.path.basename(script_path)}")
    print(f"=======================================================")
    cmd = [sys.executable, script_path, ep_dir]
    t0 = time.time()
    res = subprocess.run(cmd, cwd=ROOT)
    elapsed = time.time() - t0
    if res.returncode != 0:
        if optional:
            print(f"[!] Warning: {step_name} exited with code {res.returncode} (optional step). Continuing...")
        else:
            print(f"[X] Error: {step_name} failed with exit code {res.returncode} after {elapsed:.1f}s.")
            sys.exit(res.returncode)
    else:
        print(f"[+] Completed {step_name} in {elapsed:.1f}s.")


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/render_episode.py <episode_dir>")
        print("Example: python scripts/render_episode.py series/day0/ep01")
        sys.exit(1)

    ep_dir = os.path.abspath(sys.argv[1])
    if not os.path.exists(ep_dir):
        print(f"[X] Episode directory not found: {ep_dir}")
        sys.exit(1)

    tl_json = os.path.join(ep_dir, "timeline.json")
    if not os.path.exists(tl_json):
        print(f"[X] timeline.json not found in {ep_dir}")
        sys.exit(1)

    print(f"\n=======================================================")
    print(f" ChakTorPai Studio · Pipeline Render")
    print(f" Episode: {os.path.basename(ep_dir)}")
    print(f" Path:    {ep_dir}")
    print(f"=======================================================")

    t_start = time.time()

    # 1. Resolve timeline
    run_step("1/6 Timeline Resolver", os.path.join(SCRIPTS, "tl.py"), ep_dir)

    # 2. Audio Generation (SFX, character lines - cached)
    run_step("2/6 Audio Generator", os.path.join(SCRIPTS, "audio_gen.py"), ep_dir, optional=True)

    # 3. Subtitles & Overlay (ASS)
    run_step("3/6 Subtitle Generator", os.path.join(SCRIPTS, "subs.py"), ep_dir)

    # 4. Shot Compositor (Video render)
    run_step("4/6 Shot Compositor", os.path.join(SCRIPTS, "shots.py"), ep_dir)

    # 5. Final Mux
    run_step("5/6 Final Mux", os.path.join(SCRIPTS, "final.py"), ep_dir)

    # 6. Quality Control
    run_step("6/6 Quality Control", os.path.join(SCRIPTS, "qc.py"), ep_dir, optional=True)

    total_time = time.time() - t_start
    print(f"\n=======================================================")
    print(f"[SUCCESS] All pipeline steps completed in {total_time:.1f}s ({total_time/60:.2f} mins)!")
    print(f"Deliverable: {os.path.join(ep_dir, 'render')}")
    print(f"=======================================================\n")


if __name__ == "__main__":
    main()
