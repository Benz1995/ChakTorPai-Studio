---
name: motion-ffmpeg
description: "Inspect, encode, remux, mix, and technically verify content deliverables with FFmpeg and ffprobe using this project's existing media utilities (ตรวจไฟล์วิดีโอ, เช็คความดัง, ส่งมอบไฟล์). Use for app render/storage contracts and delivery checks on real media files, not publication claims; requested edits such as cutting, captions or reframing use ffmpeg-skill."
---

# FFmpeg delivery and technical QA

Read [project integration](../motion-studio/references/project-integration.md) and the [render contract](../motion-studio/references/render-contract.md). Record upstream/build details using [upstream.json](references/upstream.json).

## Inspect before processing

- Reuse the configured `FFMPEG_PATH`/`FFPROBE_PATH` or binaries on PATH. Inspect `-version` and available encoders/filters before selecting a command.
- Probe the actual source for duration, dimensions, sample/display aspect ratio, frame rate/time base, rotation, codecs, channel layout, and audio streams.
- Identify the requested destination requirements and preserve the approved master. Write a clearly named derivative rather than overwriting the source.
- Prefer remuxing when only the container needs changing and stream compatibility permits it. Re-encode when codec, image geometry, audio, filtering, or timing needs to change.

## Process through explicit contracts

1. Build argument arrays with `execFile`/equivalent process APIs when handling file paths; do not interpolate user paths into shell command strings.
2. Select intended video/audio streams explicitly for sources with multiple tracks. Preserve or intentionally remove metadata and subtitle streams according to the brief.
3. For broad MP4 playback, verify the chosen H.264/AAC encoder, pixel format, dimensions, and fast-start behavior against the destination; alpha delivery needs a separate supported format.
4. Preserve FPS and duration unless conversion is required. Check scene/caption alignment after frame-rate or speed changes.
5. When mixing narration and music/SFX, define gain, start offsets, ducking, and tails explicitly. Measure the output and listen before accepting it.
6. Capture exit code, bounded stderr, input/output paths, parameters, and probed output metadata in the job receipt. Fail the operation if FFmpeg exits unsuccessfully.

## Fit the existing app

- `server/media.ts` already provides `probeDuration`, `toMp3`, `toRefWav`, safe media-path mapping, and silence generation; reuse these for their intended contracts.
- Current scene-upload audio is converted to mono MP3 at 44.1 kHz; local voice references use mono WAV at 24 kHz. Do not silently change these shared contracts for one new provider.
- Remotion's renderer produces the visual composition; an FFmpeg delivery pass should consume that output or another explicit asset, not bypass scene/settings ownership.
- A 16:9-to-9:16 crop is an editorial framing decision. Inspect people, products, and caption safe areas rather than applying a blind center crop.
- Hardware encoders can have different quality/features from software encoders. Use a representative comparison and current local availability rather than assuming a speed/quality result.
- FFmpeg licensing depends on build options and linked libraries. The repository is mainly LGPL, with optional GPL components; record the actual binary configuration when distributing a bundled runtime.

## Verify observable output

From PowerShell, with actual existing paths substituted:

```powershell
ffprobe -v error -show_format -show_streams -of json 'B:\path\delivery.mp4'
ffmpeg -v error -xerror -i 'B:\path\delivery.mp4' -map 0:v? -map 0:a? -f null -
```

- Probe and fully decode the final file; a file existing or an encoder reaching 100% is insufficient.
- Inspect start/middle/end frames and every edited transition; compare duration and A/V synchronization with the intended master.
- Listen for clipping, missing speech, abrupt cuts, and channel mistakes. A clean decode does not prove creative quality or approval.
- Report technical QA, visual/listening review, and any remaining editorial decision separately; local encoding has no publication receipt.

## Sources

[FFmpeg README](https://github.com/FFmpeg/FFmpeg/blob/master/README.md), [build-dependent license details](https://github.com/FFmpeg/FFmpeg/blob/master/LICENSE.md).
