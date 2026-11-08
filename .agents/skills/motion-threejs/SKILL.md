---
name: motion-threejs
description: Build Three.js product shots, camera moves and 3D explainer scenes for Content Studio with frame-driven animation and checked preview/export compatibility.
---

# Three.js content scenes

Use for actual depth, lighting, model animation or camera movement. Keep typography and captions in the existing React overlay when that improves Thai text quality and layout control.

Read [project integration](../motion-studio/references/project-integration.md) and the [render contract](../motion-studio/references/render-contract.md) before implementation. This skill works independently of the master skill.

## Select a rendering path

- Inspect installed dependencies and the existing Remotion version before selecting a raw Three.js canvas or a supported React/Remotion bridge.
- Add only dependencies required by the chosen path. A React bridge is optional; Three.js itself is the `three` package.
- Check the current bridge peer dependencies against React 19 and the project's aligned Remotion packages. Do not upgrade the rendering stack merely to follow an upstream example.
- Choose geometry, materials, lighting and output size to meet the visual brief. A product orbit rarely needs a full post-processing stack.

## Implement the shot

1. Define camera framing, lens, subject scale, lighting and a clear reveal/hold/CTA sequence in output frames.
2. Keep model files, textures and decoder files locally addressable through the project's asset/media conventions. Preserve the original asset and its provenance.
3. Initialize the scene, camera and renderer once per owning component. Drive transforms and shader uniforms from `frame / fps`, not elapsed wall time.
4. For glTF animation, seek a known animation time derived from the frame instead of incrementing an animation mixer with a live clock.
5. Wait for model, texture and decoder readiness before capture using the installed Remotion render-delay API; release the handle on success and cancel on failure. Also handle preview loading, because render delays do not pause Player playback.
6. Render the requested frame explicitly. The official spinning-cube demo's animation loop is for interactive pages, not a video composition.
7. Dispose geometries, materials, textures, render targets and renderer resources owned by the component. Do not dispose shared cached assets while another scene still uses them.

## Compatibility choices

- Verify color management, tone mapping, alpha, shadows and pixel ratio in the actual headless render environment.
- Treat WebGPU as a separate compatibility choice. A working interactive WebGPU preview does not prove server-side rendering support.
- For asset optimization, use `motion-gltf-transform` and verify that the target loader has the required Draco, Meshopt or KTX2 support.
- For collision-driven movement, use `motion-rapier` to produce frame-indexed transforms; Three.js is the visual renderer, not the physics engine.

## Validate

- Inspect first, middle, final and camera-cut frames in both the Player and a short MP4 export.
- Seek frames backward and in shuffled order; compare repeated target frames for stable transforms and lighting.
- Check texture loading errors, GPU fallback, missing decoder files, black frames and alpha edges at delivery resolution.
- Record render time and peak memory before adding geometry, shadow maps or effects. Include model/texture sources and licenses in the delivery record.

## Sources and status

[Three.js README](https://github.com/mrdoob/three.js/blob/dev/README.md) and [license](https://github.com/mrdoob/three.js/blob/dev/LICENSE) were reviewed. Three.js is MIT; 3D assets have their own rights. [Upstream metadata](references/upstream.json) is a dated reference. The project's `src/remotion/showcase/Prism.tsx` provides a tested Three.js math-to-SVG example.

**WebGL path in the app (2026-10-28):** `@remotion/three@4.0.538` + `@react-three/fiber@9.8.2` drive the
`studio3d` template (`src/remotion/three/Stage3D.tsx`): frame-computed camera rig, HDRI via `HDRLoader`,
GLB via `GLTFLoader` + Meshopt, `AnimationMixer.setTime(frame / fps)`, HarfBuzz-shaped Thai 3D text and
Spark Gaussian splats. Loads use `useAsset` (`src/remotion/three/assets.ts`), which holds the frame until
the loaded object has been committed *and drawn* — while rendering, `ThreeCanvas` only redraws on frame
change, so a plain `delayRender` around a loader exports empty frames. Reuse these pieces for new 3D
scenes; for Blender, Poly Haven, Mixamo and splat workflows read [studio-3d](../studio-3d/SKILL.md).
