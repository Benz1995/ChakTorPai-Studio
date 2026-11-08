---
name: studio-3d
description: Make 3D shots for Content Studio — Blender headless renders (Cycles on the RTX GPU), the frame-driven studio3d template (React Three Fiber + @remotion/three) with GLB models, Thai 3D text, Gaussian splats and HDRI light, Poly Haven CC0 assets, Mixamo FBX to GLB, and the Hunyuan3D-2 image-to-3D feasibility path. Use for any 3D product shot, 3D title, character animation or splat scene.
---

# Studio 3D

Everything here is installed and tested in `content-studio/` (2026-10-28). Read
[the 3D guide](../../../content-studio/docs/three-d.md) for file locations, measured timings and
the API; this page is the decision path. Keep Remotion frame-driven and the existing
[render contract](../motion-studio/references/render-contract.md).

## Pick the path

| Need | Path | Notes |
| --- | --- | --- |
| Product/model orbit, animated character, splat, quick 3D title | `studio3d` template, `scene.three` | Real-time WebGL inside the Remotion render; seek-identical frames; ~1–2 s per 3D frame on export |
| Photoreal hero shot, glossy 3D Thai title with reflections, 360° turntable | `blender_render` → MP4 attached as the scene video | Cycles OptiX; ~2.3 s/frame at 1080×1920, 64 samples. Draft with `resolutionScale: 0.5`, `samples: 32` |
| HDRI light, CC0 models / textures | `polyhaven_search` → `polyhaven_fetch` | 1k HDRIs are enough for lighting; credits go to `data/polyhaven-credits.json` |
| Mixamo character | user downloads FBX → `convert_to_glb` → `scene.three.animation` | Never sign in to Mixamo/Adobe for the user |
| 3D from one product photo | Hunyuan3D-2mini (isolated venv), see the guide | Shape only (untextured) on 12 GB; texture stage is not set up |

## studio3d template (`scene.three`)

- `kind: 'model'` + `modelUrl` (.glb/.gltf, Meshopt OK; Draco/KTX2 not wired) + optional `animation` clip name.
  Clips are sampled with `AnimationMixer.setTime(frame / fps)` — never a live clock.
- `kind: 'text'` + `text` (+ `fontId` kanit | kanit-xb | prompt | mitr, `color`). The server shapes the text
  with HarfBuzz on save (`textPathUrl`), so Thai vowels and tone marks sit correctly; do not hand-build
  `TextGeometry` for Thai. Keep ≤ ~12 Thai characters per line in 9:16.
- `kind: 'splat'` + `splatUrl` (.ply / .splat / .spz / .ksplat / .sog via Spark 2.4). Raw 3DGS captures are
  usually y-down: set `flipY: true`. While rendering, each frame waits for Spark's sort of that exact camera.
- Light: `hdriUrl` (.hdr); `showHdri` draws it behind the subject; no HDRI = a soft three-light rig.
- Camera: `orbit` (default 50°), `dolly`, `rise`, `static`; `orbitDeg`, `distance` (1 = fit). Subjects are
  normalized to a unit sphere, so any model scale works.
- A scene with `videoUrl` (Blender render) plays that video instead of the live stage.
- Set via MCP `update_content` (`scenes[].three`) — local file paths are uploaded unchanged.

## Blender (5.2.3 LTS, `content-studio/local-3d/blender-5.2.3-windows-x64/`)

- Jobs run through the API (`/api/three/blender`, `/api/three/convert`) or MCP `blender_render` /
  `convert_to_glb`; the script is `content-studio/scripts/blender/bigo_blender.py` (presets `text`,
  `turntable`, `convert`). Write new presets there: keyframe every motion, fixed `cycles.seed`,
  `use_persistent_data`, render to PNG and let the API encode H.264 with FFmpeg.
- `contentId` + `sceneId` attach the MP4 as `scene.videoUrl` with its measured duration.
- Blender jobs are in memory: a dev-server restart (tsx watch reloads on edits under `server/` or
  `src/`) drops the job list and may orphan a running Blender process — avoid editing during long renders.

## Checks before delivery

1. `preview_frames` on the 3D scenes (first, middle, last); framing must clear the heading and captions.
2. Seek check: request the same seconds in a different order and compare PNGs (expect identical).
3. `render_content`, then probe the MP4 (duration, black frames). Record Poly Haven / model / font credits
   in the delivery notes (`polyhaven_credits`, `content-studio/assets/three/CREDITS.md`).
