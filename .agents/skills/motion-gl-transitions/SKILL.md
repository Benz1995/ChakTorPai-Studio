---
name: motion-gl-transitions
description: Add selected GL Transitions shader cuts to Content Studio, using a compatible Remotion presentation or explicit shader host with verified texture, timing and alpha behavior.
---

# GL Transitions for content

Use for a specific shader transition that improves a scene change. Keep the existing Remotion transitions when they already meet the brief.

Read [project integration](../motion-studio/references/project-integration.md) and the [render contract](../motion-studio/references/render-contract.md). This skill is directly callable.

## Choose the adapter

- `gl-transitions` provides shader sources, parameters and metadata; it is not a standalone video engine.
- Upstream currently includes `@gl-transitions/remotion`, which converts a named transition into a `TransitionSeries` presentation. Check the selected release's requirements and installed peer versions before adding it.
- The reviewed adapter README requires Remotion 4.0.500 or later. Its Studio preview requires Chrome 149+ with the HTML-in-canvas flag enabled; confirm actual browser support before choosing this route.
- Server rendering and Studio preview have different requirements. Use the documented WebGL backend for the render environment and test both; a compatible version number alone is insufficient.
- If the adapter is unsuitable, use a verified shader host or bake the transition. Do not insert an unsupported canvas capture layer into the shared renderer.

## Integrate the transition

1. Choose one transition by name and record its parameters, extra textures, duration and intended visual role.
2. Add it through the existing transition selector in `src/remotion/options/transitions.ts`, preserving the shared timing logic and overlap accounting.
3. Drive progress explicitly from 0 to 1 with the timeline. At the endpoints, the output must be only the from image or only the to image.
4. For a custom host, implement the specification's `getFromColor`, `getToColor`, `ratio` and normalized UV contract; a shader snippet does not define a complete WebGL program.
5. Load extra images, displacement maps and other textures before capture. Release owned GL resources and fail visibly on shader compilation or loading errors.
6. Keep captions and CTA readability through the transition; shorten or simplify the effect when it obscures the message.

Do not run an independent animation clock. Preserve scene frame counts and transition overlaps so audio and captions retain their existing alignment.

## Check alpha and compatibility

- The reviewed Remotion adapter captures arbitrary scene markup using HTML-in-canvas. Its README warns that some transparent transition regions reveal a captured scene or black rather than layers behind `TransitionSeries`.
- Confirm whether that compositing behavior is acceptable for the requested design; use another path when the effect requires true layered transparency.
- Source-package compatibility metadata does not establish that the complete Content Studio integration has been tested.
- Read the chosen transition's license header. Upstream's collection license is MIT, while the README identifies two transitions under BSD licenses; retain the applicable notices.

## Validate

- Inspect progress 0, 0.25, 0.5, 0.75 and 1, plus a short MP4 containing both adjacent scenes and their audio.
- Check aspect preservation, seams, alpha regions, texture orientation and the transition at the target output dimensions.
- Repeat a middle frame after shuffled requests. Confirm preview/export agreement in the actual browsers.
- Record transition name, parameters, package versions, any extra texture sources and the successful export evidence.

## Built-in pattern wipes

Before adding a GL adapter, check the fourteen pattern wipes already in `src/remotion/options/transitions.ts` (`blocks`, `checker`, `blinds`, `barnDoors`, `diamond`, `bars` adapted from Shaders, MIT; `circles`, `zigzag`, `splitOpen`, `slices`, `wave`, `heart`, `burst`, `slash` original; list new ones in `PATTERN_IDS`). They are CSS `clip-path` presentations in `src/remotion/effects/transitions.tsx`: no HTML-in-canvas, any scene markup, exact endpoints (hidden at 0, `none` at 1). A new pattern is a `PatternKind` branch returning a clip path for eased progress. See the [effects library](../../../content-studio/docs/effects-library.md).

## Sources and status

[Collection README](https://github.com/gl-transitions/gl-transitions/blob/master/README.md), [Remotion adapter guide](https://github.com/gl-transitions/gl-transitions/blob/master/packages/remotion/README.md) and [license](https://github.com/gl-transitions/gl-transitions/blob/master/LICENSE) were reviewed. [Metadata](references/upstream.json) records the source snapshot. Integration is on demand.
