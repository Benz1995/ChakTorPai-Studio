---
name: motion-p5js
description: "Create seeded generative patterns, procedural illustration, and audio-reactive visual studies with p5.js for reproducible content assets."
---

# p5.js generative visuals

Use for procedural patterns, visual metaphors, creative-coding studies, and generative backgrounds.
Keep narration, captions, and delivery in the existing content pipeline.

Read [project integration](../motion-studio/references/project-integration.md), [render contract](../motion-studio/references/render-contract.md), and [upstream evidence](references/upstream.json).

## Scope the sketch

p5.js is an optional `p5` dependency; verify the installed major and its APIs before adding it.
Create an instance-scoped sketch so the editor's multiple previews do not share global drawing state.

- Fix canvas dimensions, pixel density, palette, seed, fps, and duration as job inputs.
- Keep generation controls in editable data instead of hard-coding a single finished image.
- Use a canvas layer or bake a frame sequence when integrating the result into Remotion.
- Avoid attaching global input handlers unless interactivity is part of the requested deliverable.

## Reproducible drawing

A p5 `draw` loop is a live runtime, not the export clock.
For captured video, use controlled drawing and evaluate each requested frame explicitly.

- Use `noLoop()` and a controlled redraw path rather than relying on browser playback speed.
- Derive time from the requested frame/fps; do not use `millis()`, mouse position, or live `deltaTime` in an exported shot.
- Use fixed seeds for both random and noise generation.
- Rebuild frame state or use indexed precomputed values so evaluation does not depend on how many random calls previous frames made.
- Clear/reset drawing state deliberately; trails and feedback require deterministic simulation or a baked sequence.
- Preload or await media and fonts before frame capture.
- Remove the sketch, canvas, and owned resources on unmount.

## Audio-reactive content

Use an analysis envelope or spectrum sampled from the actual approved audio file.
Store the analyzed samples with their sample rate/hop size and map frame time into them.
Do not use microphone input or live speaker FFT as the final export source.

For a seamless loop, match the phase and derivative at its boundary where the chosen visual permits it.
For a narration background, keep visual contrast and detail below the caption and speaker hierarchy.

## Verification

Recreate the sketch with the same seed and compare representative output frames.
Seek backward, then repeat a target frame; patterns, colors, and trails must match.
Inspect the densest region, loop boundary, and caption-safe area at actual output dimensions.

Render a short representative clip through the intended delivery pipeline.
Record the seed, p5 version, dimensions, fps, and any baked analysis/frame assets.

## License scope

The checked repository contains the GNU Lesser General Public License v2.1.
Inspect the installed package's license and notices when distributing library code or modified builds.
Do not infer the licensing of an original rendered artwork solely from the library's license.
