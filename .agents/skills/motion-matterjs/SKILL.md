---
name: motion-matterjs
description: Create collision-driven 2D content scenes with Matter.js, including falling products, stacked cards, constraints and kinetic typography, with reproducible video frames.
---

# Matter.js content physics

Use for 2D rigid-body motion whose collisions or constraints matter to the story. For a single decorative bounce, use the existing Remotion spring instead of adding a physics dependency.

Read [project integration](../motion-studio/references/project-integration.md) and the [render contract](../motion-studio/references/render-contract.md) before implementation. This skill can be invoked independently; the shared references describe the existing project, not a required orchestrator run.

## Choose the simulation

- Define the deliverable: scene dimensions, frame rate, duration, body count, gravity, colliders and readable end state.
- Model visual elements and collision geometry separately. Simplified rectangles, circles and compound bodies often produce clearer product motion than detailed outlines.
- Prefer explicit masses, restitution, friction and constraints over adding forces until the preview looks plausible.
- Install only `matter-js` and any types needed by the selected implementation when the actual task requires them; inspect the lockfile first.

## Integrate with this studio

1. Create the world from serializable scene inputs and a stable seed. Keep creation order stable; avoid process-global counters or random state determining content identity.
2. Pre-simulate from the same initial state using `Engine.update(engine, deltaMs)` with a fixed, suitably small step. Store positions and angles indexed by output frame, or use deterministic checkpoints plus replay.
3. Read frame N directly from the generated data. A request for frame 180 must not depend on whether frame 179 was rendered in that browser.
4. Render sampled transforms through React/SVG or a frame-driven canvas in a `TemplateDef`; register it in the existing template registry when a reusable template is requested.
5. Place caption and CTA regions outside the body field. Use collision filters or static barriers to preserve those regions.
6. Dispose engine worlds, event handlers and temporary canvas resources when their owning scene changes.

Do not start `Runner.run`, `Render.run`, `requestAnimationFrame`, timers or a live simulation loop inside the Remotion composition. The README's real-time demo loops are not the export integration.

## Validate the result

- Compare repeated frame renders and a shuffled sequence such as 90, 0, 180, 90; the two frame-90 results must match.
- Check resting stacks, fast bodies, constraints, clipping and the final frame. Reduce step size or simplify colliders if bodies tunnel or jitter.
- Test the chosen aspect ratio with long Thai labels and actual product geometry; preserve readable captions during impacts.
- Measure pre-simulation time and cache size before increasing body count or solver iterations. Record the seed and simulation parameters with the deliverable.
- For collision-triggered sound, export collision events to a timed audio asset rather than playing Web Audio from engine callbacks.

## Sources and status

Upstream: [Matter.js](https://github.com/liabru/matter-js), [Engine.update implementation](https://github.com/liabru/matter-js/blob/master/src/core/Engine.js). MIT license; retain applicable notices when distributing code. [Verified upstream metadata](references/upstream.json) records the review date and source URLs. The project now includes a focused baked-physics example in `scripts/motion-demo-physics.mjs` and `src/remotion/showcase/physics.json`; reuse it where appropriate rather than assuming a general physics editor exists.
