---
name: motion-react-spring
description: "Design spring-based React UI motion with React Spring and translate approved motion into deterministic frame-driven video behavior."
---

# React Spring motion

Use for responsive editor interactions, interactive presentation prototypes, or spring-style motion studies.
For a Content Studio export, prefer the existing Remotion spring unless React Spring itself is needed.

Read [project integration](../motion-studio/references/project-integration.md), [render contract](../motion-studio/references/render-contract.md), and [upstream evidence](references/upstream.json).

## Choose a target

The upstream library has distinct web and Three.js targets.
Inspect the installed React and package versions, peer dependencies, and target before introducing a dependency.

- Use `@react-spring/web` for DOM-based editor/UI motion.
- Use `@react-spring/three` only with a deliberate Three.js/React renderer integration.
- Do not install all targets merely to produce one animated card.
- Keep animated state local to the component; preserve the existing editor's save and media workflow.

## Interactive motion

Use explicit source/destination states, stable element keys, and intentional interruption behavior.
Choose tension, friction, mass, damping, or duration behavior based on the visual goal supported by the installed API.

- Test rapid repeated interactions rather than only a complete entrance.
- Respect reduced-motion preferences for app UI and keep focus/navigation usable while elements move.
- Avoid layout shifts that change a button or text field's hit area during input.
- Stop and clean up controllers/listeners when the component leaves the page.

## Exported video motion

An ordinary `useSpring` animation advances with a runtime clock.
It does not automatically become a seekable Remotion animation.

- Express the approved motion with Remotion's frame-based `spring` when that achieves the requested result.
- Treat a parameter conversion as a visual retuning task; libraries do not guarantee identical spring parameter semantics.
- If React Spring must generate the motion, verify a manual fixed-step advancement API in the chosen version, sample from a known initial state, and store results by frame.
- Rebuild or sample independently of render order; seeking backward must not use the previous controller state.
- Keep capture values indexed by fps, duration, seed, and spring configuration.
- Do not run live controllers or requestAnimationFrame as an export clock inside the Remotion composition.

## Verification

For UI work, test repeated toggles, interruption, keyboard interaction, and reduced motion.
For export work, inspect onset, peak overshoot, settling, and the final hold.

Compare the same sampled frame after forward and backward seeking.
Check that preview remounting does not multiply controllers.
Run type checking for changed integration code and render a short video through the intended engine.

Record whether the delivered behavior is interactive React Spring or sampled/frame-driven video motion.
Preserve the MIT notice if distributing library code.
