---
name: motion-obs
description: Capture application demos, tutorials, or source footage with OBS Studio for this project's content workflow. Use for requested recordings and capture setup, not deterministic Remotion exports or livestream publishing.
---

# OBS source capture

Read [project integration](../motion-studio/references/project-integration.md) and the [render contract](../motion-studio/references/render-contract.md) before using a recording as a content asset.

## Select the capture path

- Use OBS for real application demonstrations, presenter footage, and live interactions that cannot be reconstructed from composition props.
- Keep generated motion graphics on the Remotion render path; a screen recording introduces realtime timing and capture artifacts.
- Inspect the installed OBS version, current profile, scene collection, and recording state before changing a running session.
- Use the application/window/source specified by the user. If the target is ambiguous, resolve that target before starting capture; setup and test-file inspection can continue independently.

## Prepare the shot

1. Set canvas size, output size, frame rate, crop, and pointer visibility from the content brief.
2. Prefer a dedicated window capture for app tutorials. Inspect the actual preview for unwanted windows, dialogs, notifications, or private information before recording.
3. Select the intended microphone and desktop/application audio devices. Separate voice and application sound into tracks when later mixing needs independent control.
4. Set a project-specific recording directory and unique take names. Preserve the source recording alongside any edited derivative.
5. Choose a supported encoder based on an actual short capture test and the current GPU load, including local F5/SDXL work.

## Record and ingest

- Start recording only as part of the requested capture task; preparing content skills does not itself start capture or streaming.
- Prefer an interruption-tolerant recording container such as MKV. Remux to MP4 through OBS or FFmpeg when the editing/import path needs it.
- Stop the intended recording and wait for the file to finish writing before probing or copying it.
- Use the normal upload path for supported project assets. Check the current editor's media model before attaching footage: `Scene.imageUrl` is an image slot, not a generic video-clip track.
- For a recorded video background, implement or use an explicit video-aware Remotion template and preserve its audio behavior; do not pretend a video URL is an image.
- Existing scene-audio upload extracts audio; it does not import a video timeline.
- OBS streaming and account configuration are separate from local recording and require their own user request.

## Verify observable output

- Probe the resulting file for duration, dimensions, frame rate, codecs, and intended audio tracks.
- Watch the beginning, a representative interaction, and the end; inspect text legibility, cursor movement, dropped frames, and A/V sync.
- Listen to microphone and application audio separately and then together. Report clipping, echo, and excessive background sound.
- State which take was captured and which derivative was imported. A successful recording status is not evidence of a published video.

## Sources and scope

Upstream: [OBS Studio](https://github.com/obsproject/obs-studio), [recording output guide](https://obsproject.com/kb/standard-recording-output-guide). Source/license verification is recorded in [upstream.json](references/upstream.json).

OBS is an optional external capture application here; this skill does not install it or add a capture engine to Content Studio.
