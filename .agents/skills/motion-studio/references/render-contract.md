# Deterministic rendering contract

This applies to animation used in the Remotion export. Interactive editor UI may
use a live clock, but its motion must not determine exported video frames.

## One frame, one result

The rendered state must be a function of `(props, frame, fps, explicit seed)`.
Remotion may request frames out of order, seek backwards, remount components, or
render in parallel. Never require frame 99 to have been painted before frame 100.

- Use `useCurrentFrame()` and `useVideoConfig()`. `frame / fps` is timeline seconds.
  Read `SceneRenderProps` to distinguish scene-local frames, global `startFrame`,
  and voice lead-in. Do not shift captions/audio twice.
- Prefer Remotion interpolation and frame-based springs for ordinary text/layout
  motion. Keep UI-only React Spring effects out of video timing.
- An external timeline needs autoplay disabled and an explicit seek to the exact
  frame time. Verify its current version's seek semantics and supported runtime.
  Do not advance by delta from the previously rendered frame.
- Never use `Date.now()`, unseeded `Math.random()`, `requestAnimationFrame`, timers,
  CSS keyframe autoplay, audio context time, or a GPU ticker as the export clock.
- Seed procedural inputs from stable content/scene identifiers plus an explicit
  recorded seed. Reproducibility across a fixed environment does not imply
  bit-identical pixels across every GPU/driver/browser.

## Physics and particles

Choose a fixed simulation timestep independent of playback speed (for example,
1/60 second). Precompute a trajectory/cache or bake frames once from the initial
state and seed. Sample/interpolate that data at video frame time. Cache keys must
include scene inputs, seed, solver version, timestep, and duration.

If recomputing instead, initialize an isolated world and replay the exact step
count for the requested time; assess the CPU cost before using this per frame.
Never share a mutable world between parallel render workers. Fix substeps and
solver settings. Document the selected Rapier build's determinism properties;
fixed stepping alone is not proof of cross-platform determinism.

## Canvas, WebGL, WASM, and assets

- Disable autonomous render loops and set transforms/uniforms from the current
  frame. If a library lacks reliable seeking, bake an image sequence/video or
  implement a small deterministic effect instead of pretending its live ticker
  can be sought safely.
- Hold render completion until asynchronous setup, textures, fonts, decoders,
  WASM initialization, and the current frame's draw are finished. Use supported
  Remotion readiness APIs for the installed version, with success/failure cleanup
  so rendering does not hang. Do not fetch/generate assets independently per frame.
- Dispose renderers, materials, textures, event handlers, workers and audio nodes
  on cleanup. Control canvas dimensions/pixel ratio and color/alpha handling.
- Check the actual headless renderer backend and target browser. A working editor
  canvas is insufficient evidence for headless export. Prefer a maintained official
  integration when compatible, or import a baked asset.
- glTF compression introduces runtime decoder requirements. Test the optimized
  file in the same loader and export environment, including materials, animations,
  color spaces, and texture extensions.
- Use local `/media/` or `/assets/` URLs for app-managed files. The renderer
  absolutizes these through its configured origin. Remote assets require stable
  access and appropriate CORS; avoid network-dependent final compositions when
  the assets can be staged locally.

## Sound and captions

Generate synthesis or effects offline to an audio file, import it through the
app's media workflow, and schedule it by timeline frames. Preview and export use
the same file, sample rate, start offset, gain and duration. A separately playing
Tone.js transport is not automatically part of the encoded video soundtrack.

Reuse authored Thai text and the pronunciation mapping. ASR is a transcript/timing
estimate, not a forced aligner or proof of verbatim script accuracy. Keep original
text, detected words, corrected timings, and estimated timings distinguishable.
Word times are seconds relative to scene audio; the existing composition adds
lead-in and scene placement. Avoid overwriting the script with ASR without a reason.

## Observable acceptance checks

For a new animation integration render a representative frame directly, then after
forward playback, then after a backward seek. Compare composition and expected
object positions (pixels when feasible in a fixed environment). Inspect time 0,
a mid-action frame, a scene boundary, and the last valid frame. Check a short final
encode, not only canvas screenshots. Include at least one Thai caption and each
requested aspect in layout review.

For final files verify expected streams, resolution, FPS, duration, first/last
frames, sync, and decoding. Choose loudness targets for the actual destination;
measure before adjustment and remeasure afterward. Technical checks do not claim
rights clearance, editorial approval, or human listening that did not occur.
