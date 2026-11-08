---
name: motion-pixijs
description: "Build GPU-rendered 2D sprite, text, mask, and filter layers with PixiJS for content that benefits from a canvas scene graph."
---

# PixiJS 2D content layers

Use for many sprites, composited illustrations, GPU filters, and canvas-based 2D scenes.
For small text/shape layouts, existing React/SVG templates may be simpler.

Read [project integration](../motion-studio/references/project-integration.md) and [render contract](../motion-studio/references/render-contract.md).
Use [upstream evidence](references/upstream.json) when checking package and renderer compatibility.

## Integrate a bounded layer

PixiJS is an optional `pixi.js` dependency.
Inspect installed versions and render-host capabilities before adding it.

- Put scene construction, asset loading, frame evaluation, and disposal behind a small adapter.
- Use composition dimensions, not the editor window size; fix render resolution/device pixel ratio for the job.
- Keep text/brand data in the existing scene model when it can remain editable.
- Avoid one uncontrolled application or GPU context per gallery card; use static or baked thumbnails for expensive previews.
- Choose a renderer supported by the actual headless export environment. A working desktop WebGPU preview does not prove export compatibility.

## Make frames seekable

Initialize the renderer and await textures/fonts before marking the layer ready.
The upstream default ticker example is for live applications; adapt it for captured video.

- Disable automatic/shared ticking for exported layers.
- Derive sprite transforms, filter uniforms, and masks from `frame / fps` or a precomputed simulation.
- Do not accumulate `rotation += delta` or other ticker-based state between captured frames.
- Explicitly render after applying the requested frame's complete state.
- Keep sprite sorting, random placement, and texture choices stable for the same job.
- Rebuild mutable effects from an initial snapshot or bake them when they cannot seek deterministically.
- Release textures, listeners, display objects, and owned renderer resources on teardown; preserve shared resources until their owners finish.

## Visual and resource choices

Use atlases or shared textures for repeated artwork.
Budget filter passes, texture dimensions, and concurrent previews instead of assuming GPU availability.
Keep transparent compositing and premultiplied-alpha behavior consistent with the downstream video path.
A transparent canvas alone does not mean an H.264 MP4 will contain alpha.

For Thai text, load the intended font before layout and inspect line breaks at output resolution.
Use DOM/SVG overlays when they preserve required text quality more reliably.

## Verification

Capture the opening, busiest scene, a filter-heavy frame, and final state at target resolution.
Compare a repeated frame after an out-of-order seek and after remounting.
Inspect GPU/resource cleanup by opening and closing the preview repeatedly.

Render a short sample in the same headless engine used for delivery.
Check alpha edges, text sharpness, color, dimensions, and missing assets.
Record renderer choice and version with the output.
