---
name: motion-gltf-transform
description: Inspect and optimize glTF or GLB assets for Content Studio 3D shots while preserving visible quality, animations, material behavior and loader compatibility.
---

# glTF asset preparation

Use for existing glTF/GLB assets that need smaller downloads, fewer draw calls or lower texture/geometry cost. This is asset processing; the final scene still needs a renderer such as Three.js.

Read [project integration](../motion-studio/references/project-integration.md) and the [render contract](../motion-studio/references/render-contract.md). This specialist works independently.

## Inspect before transforming

- Preserve the source model and associated textures. Record asset provenance, input hash, geometry/material counts, texture dimensions and animation names.
- Determine the actual target loader and its supported extensions in both Player preview and headless export.
- Inspect the available CLI or packages. The SDK separates `@gltf-transform/core`, `@gltf-transform/extensions` and `@gltf-transform/functions`; the CLI is `@gltf-transform/cli`.
- Pin and record the selected version. Use a local tool dependency or isolated invocation appropriate to the project rather than a global installation by default.

## Build a reversible pipeline

1. Write to a new output path; never overwrite the only original asset.
2. Start with inspection and operations whose effect is understood, such as deduplication or pruning unused resources. Keep a record of the exact options.
3. Reduce texture sizes according to the actual on-screen footprint and camera distance. Compare product text, normal maps, metal/roughness and alpha-masked areas.
4. Consider geometry compression and simplification separately. Lossy simplification can change silhouette, UV seams, morph targets or skinning; inspect the relevant animation poses.
5. Add Draco, Meshopt or KTX2/Basis compression only when the consumer has the corresponding decoder/transcoder and extension support. Supply those dependencies to the SDK as required.
6. Keep decoder files locally addressable for server rendering. A compressed asset that works through a CDN in the browser may fail in the render process.
7. Register the optimized asset through the project's normal asset/media convention and retain the original-to-output mapping.

The upstream `optimize input.glb output.glb` command is a starting point, not proof that the resulting asset is visually lossless or compatible with every loader. Inspect installed CLI help before choosing exact flags.

## Validate in the real shot

- Compare file size, load time, texture memory and render time against the original.
- Render matching camera/light/animation frames before and after optimization, including close-ups and silhouettes.
- Check skinning, morph targets, animation duration, transparent materials, texture orientation and color behavior.
- Load the output in both the Player and a short server-side export; missing decoder/extension errors block delivery.
- Keep the optimization receipt with input/output hashes, tool version, command/options and any accepted visual differences.

## Sources and status

[glTF Transform README](https://github.com/donmccurdy/glTF-Transform/blob/main/README.md) and [MIT license](https://github.com/donmccurdy/glTF-Transform/blob/main/LICENSE.md) were reviewed. Asset rights remain separate from SDK licensing. [Upstream metadata](references/upstream.json) records sources and package names. Integration is on demand.

**Project loader facts (2026-10-28):** the `studio3d` loader is three 0.186 `GLTFLoader` with
`MeshoptDecoder` registered; Draco and KTX2 are not wired, so prefer `meshopt` compression and plain
JPEG/PNG/WebP textures, or add the decoder files locally first. Format conversion (FBX/OBJ/multi-file
glTF → one GLB, Mixamo animation clips merged as named NLA tracks) is done by Blender through
`convert_to_glb` — see [studio-3d](../studio-3d/SKILL.md); run glTF Transform after that step when size matters.
