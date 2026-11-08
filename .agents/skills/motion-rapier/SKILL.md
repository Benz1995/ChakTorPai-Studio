---
name: motion-rapier
description: Produce reproducible Rapier physics for 3D collisions, rigid-body product motion and constrained scenes, then feed frame-indexed transforms into Content Studio visuals.
---

# Rapier content physics

Use when 3D collision response, joints or rigid-body interactions are required. Pair it with a renderer such as Three.js; Rapier does not create the finished picture by itself.

Read [project integration](../motion-studio/references/project-integration.md) and the [render contract](../motion-studio/references/render-contract.md). This specialist can be invoked directly.

## Select the binding

- The upstream `dimforge/rapier` repository contains Rust engines and official bindings. A TypeScript browser task normally needs a published JavaScript/WASM package, not a Rust build.
- Select the 2D or 3D package to match the scene. Check current package availability and bundler compatibility before adding it.
- Upstream documents standard, SIMD, deterministic and `-compat` variants. Standard builds do not guarantee cross-platform determinism; the deterministic variants are the relevant option when replay must match across machines.
- `-compat` embeds WASM in JavaScript for wider bundler support at a size cost. Do not install every variant or assume all variants expose identical initialization in every version.

## Build the simulation asset

1. Establish units, gravity, colliders, mass, contact behavior, joints and fixed initial poses from serializable inputs.
2. Initialize the selected WASM binding once and await completion. For browser rendering, use the installed Remotion delay/continue API and an explicit failure path; preview loading needs its own state.
3. Fix the simulation timestep and input ordering. Use seeded initial conditions and keep simulation stepping independent of frame requests.
4. Precompute transforms and timed contact events for the entire scene, or store reproducible checkpoints with replay. Keep a documented mapping from output frames to simulation steps.
5. Sample this data directly at the requested frame. Interpolate position and quaternion between samples if needed, without advancing mutable world state during React renders.
6. Use simplified collision geometry for detailed visible models. Validate fast-body collision handling when narrow colliders or large velocities make tunneling possible.
7. Free worlds and WASM-owned resources according to the selected binding's API. Cache baked data by engine version, seed, scene inputs and timestep.

Do not place an interactive game loop inside the Remotion scene. Output workers can request frames in any order and may run in separate browser contexts.

## Validate

- Compare the same frame after forward playback, backward seek and shuffled requests.
- Check contact penetration, resting jitter, quaternion interpolation, joint limits and endpoint poses.
- If replay must be portable, compare outputs on the actual target environments; record the exact binding variant and version. Fixed timestep alone is not a cross-platform guarantee.
- Benchmark the intended body count and collision complexity before raising solver budgets.
- Bake collision sounds to an audio track from recorded contact events, then mux/mix through the existing delivery pipeline.

## Sources and status

[Upstream README](https://github.com/dimforge/rapier/blob/master/README.md), [TypeScript bindings guide](https://github.com/dimforge/rapier/blob/master/bindings/typescript/README.md) and [Apache-2.0 license](https://github.com/dimforge/rapier/blob/master/LICENSE) were reviewed. Keep required notices with distributed code. [Source metadata](references/upstream.json) records verified package families; integration remains on demand.
