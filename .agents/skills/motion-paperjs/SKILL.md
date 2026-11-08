---
name: motion-paperjs
description: "Create and animate vector paths, diagrams, cutout shapes, and reusable SVG artwork with Paper.js for content production."
---

# Paper.js vector content

Use for editable vector illustration, path construction, boolean geometry, diagrams, and path-following motion.
Prefer existing SVG/React primitives when the requested geometry is simple.

Read [project integration](../motion-studio/references/project-integration.md) and [render contract](../motion-studio/references/render-contract.md).
Read [upstream evidence](references/upstream.json) for dependency and license decisions.

## Choose the output

Paper.js is an optional dependency. Decide whether the result should be:
- static SVG/PNG artwork consumed by the existing templates;
- a deterministic canvas layer driven by the composition frame;
- or a baked sequence for a stateful vector effect.

Use the browser `paper` package for browser layers.
Node SVG-only and canvas-rendering variants have different dependencies; do not introduce native Cairo/Pango tooling for a task that only needs browser rendering or SVG.
The upstream README distinguishes `paper`, `paper-jsdom`, and `paper-jsdom-canvas`.

## Isolate the scene

Create a separate PaperScope/project for each owned canvas or job.
Set the exact view dimensions and load fonts/imported SVG assets before layout or capture.

- Avoid the global scope leaking into adjacent previews.
- Group semantic elements so labels, arrows, and callouts remain independently editable.
- Prefer a compact control-point representation for paths and keyframe geometry.
- Keep stroke scaling, clipping, and coordinate conversions explicit when adapting to portrait/landscape.
- Do not use unsanitized foreign SVG or external resource references as trusted local artwork.

## Frame-driven motion

The upstream live `view.onFrame` example is not the final video clock.
Disable automatic frame updates for captured content and explicitly draw the requested state.

- Evaluate transform, path offset, trim/reveal, and control-point geometry from `frame / fps`.
- Rebuild or reset base geometry before each evaluation; repeated `rotate` or incremental path edits accumulate state.
- Use arc-length positioning for objects traveling along paths when that matches the motion brief.
- For path morphs, verify compatible topology or resample intentionally; unrelated segment counts do not morph automatically.
- If an effect depends on stroke history, simulate deterministically from a known start or bake it.
- Remove the project/view and owned listeners when the layer is disposed.

## Verification

Inspect vector geometry at output size and at a zoomed view for joins, winding, clipping, and alpha fringes.
Check path reveal/morph start, midpoint, end, and a repeated frame after backward seeking.
Verify Thai labels use the intended font and survive SVG import/export when that path is used.

Render a short representative sample in the final engine.
Deliver editable vector source or geometry data together with exported assets and record the package version.
The checked LICENSE.txt is MIT even though repository metadata classifies it as Other; preserve its notice for distributed library code.
