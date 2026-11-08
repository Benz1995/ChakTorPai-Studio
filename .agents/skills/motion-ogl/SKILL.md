---
name: motion-ogl
description: Create lightweight OGL shader scenes, procedural backgrounds and GPU image effects for video content with explicit frame uniforms and WebGL resource management.
---

# OGL shader content

Use when a custom shader or small GPU effect benefits from direct WebGL control. OGL provides a thin abstraction; choose Three.js when the shot needs a larger scene/model ecosystem.

Read [project integration](../motion-studio/references/project-integration.md) and the [render contract](../motion-studio/references/render-contract.md). No master-skill invocation is required.

## Define the effect

- Specify the subject, motion beats, shader parameters, palette, output dimensions and the effect's contribution to the story.
- Inspect the lockfile before adding `ogl`; pin a compatible version for the actual task rather than loading an unversioned CDN build.
- Choose a fullscreen triangle/quad for image effects or minimal geometry for a 3D effect. Keep captions and readable interface text in the existing overlay.
- Establish expected behavior for alpha, aspect ratio, texture sampling and color space before tuning the shader.

## Integrate a frame-driven canvas

1. Create the renderer, program, geometry and textures in an owned component lifecycle, with composition dimensions rather than `window.innerWidth`.
2. Set time uniforms from `frame / fps`; set progress from the specified scene interval. Seed any procedural variation from stable content inputs.
3. Set every frame-dependent value explicitly, then invoke the renderer for that frame. Do not adapt the README demo's cumulative rotations or `requestAnimationFrame` loop into a composition.
4. Wait for texture loads and shader setup before capture with the installed Remotion delay/continue API. Cancel the render with useful context on a loading or compilation failure.
5. Implement preview loading separately. Ensure canvas drawing happens before the frame can be captured; test the actual Player and headless renderer.
6. Release owned buffers, textures, programs, render targets and event handlers. Handle a lost WebGL context without producing a silent black deliverable.

## Keep the effect portable

- Check shader precision and features in the actual headless WebGL backend; interactive GPU success is insufficient.
- Use local textures and bounded resolution/pixel ratio. Render cost grows with shaded pixels and full-screen passes.
- Use stable uniforms for camera and geometry state; do not read pointer position, current date or a live audio analyser during export.
- If the effect cannot be reliably captured, bake a reviewed clip/image sequence and reuse the immutable asset through the project's media path.

## Validate

- Render beginning/middle/end frames and repeat one target frame after a backward seek.
- Check transparent edges, cropped images, banding, NaNs, shader errors and the smallest intended output size.
- Measure frame time and GPU memory for the actual export, then cap effects/passes to the content budget.
- Preserve shader and texture provenance, including any notices belonging to copied shader code.

## Reuse the built-in shader host first

Content Studio already ships a dependency-free, frame-driven WebGL host; see the [effects library](../../../content-studio/docs/effects-library.md).

- `src/remotion/effects/gl.ts` draws every layer with one shared WebGL1 context and copies pixels into the layer's 2D canvas, avoiding per-preview context limits in galleries.
- A new look is a `ShaderEffect` entry in `src/remotion/effects/shaders.ts`, `shaders-more.ts`, `shaders-extra.ts`, `shaders-sky.ts`, `shaders-world.ts` or `shaders-manga.ts` (149 exist; sky looks share the `starLayer`/`meteor`/`skyline` helpers; omit `basedOn` for original looks, set `fixedColors` when the palette is part of the look; add it to a `SHADER_GROUPS` group): GLSL defining `vec4 effect(vec2 uv, vec2 p)` using only `uTime`, `uSeed`, `uIntensity` and three palette uniforms. Pick `kind` (`background` for the `shaderfx` template, `overlay` with a CSS blend for any scene) and a render `scale`.
- `ShaderLayer` draws synchronously in `useLayoutEffect` and calls `cancelRender` on a compile/link failure during export. Pass global time (`(startFrame + frame) / fps`) when the look must continue across cuts.
- Run `npx tsx scripts/effects-library.ts seek` after changes; it compares shuffled single-frame renders with a sequential run. Add OGL only when a shot needs geometry, textures or passes beyond this host.

## Sources and status

[OGL README](https://github.com/oframe/ogl/blob/master/README.md) and [package declaration](https://github.com/oframe/ogl/blob/master/package.json) were reviewed. The package declares `Unlicense`; the reviewed repository root had no LICENSE file and GitHub returned no license classification. Recheck the selected release before distributing its code. [Upstream metadata](references/upstream.json) records this distinction. Integration is on demand.
