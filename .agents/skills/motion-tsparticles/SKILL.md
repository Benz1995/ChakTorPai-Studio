---
name: motion-tsparticles
description: Design tsParticles confetti, snow, sparks and ambient effects for content, choosing a verified deterministic adapter or baked asset for reliable video export.
---

# tsParticles content effects

Use for particle systems whose presets or plugins materially improve the requested effect. A few decorative dots can stay in the existing frame-driven Remotion code.

Read [project integration](../motion-studio/references/project-integration.md) and the [render contract](../motion-studio/references/render-contract.md). This specialist is directly callable.

## Select only the needed features

- Specify particle count, emitters, lifetime, palette, motion field, density and safe areas for captions/product information.
- The current upstream quick start uses `@tsparticles/engine` plus `@tsparticles/slim`; use individual feature packages when that is smaller, and load plugins before their options.
- A React wrapper is optional. Verify matching package versions and React compatibility before introducing it.
- Reuse preset ideas with the project's brand and dimensions; do not install the complete plugin set for a simple confetti burst.

## Choose export behavior explicitly

The upstream browser quick start is a live animation. It does not by itself provide the arbitrary-frame seeking required by this studio.

1. Inspect the installed version's API for controlled stepping, reset, stable initialization and randomness. Do not invent a `seek(frame)` API.
2. If a supported deterministic integration exists, stop the live ticker and prove that each requested output frame is obtained from stable inputs with fixed steps and seeded variation.
3. Otherwise bake the effect once into a reviewed clip or image sequence and use that asset in Remotion. Keep its frame rate, duration, alpha format, settings and hash with the deliverable.
4. If transparent export is unavailable, choose an explicit background or supported compositing method and inspect edge quality before proceeding.
5. Load resources before capture and destroy particle containers, canvases and listeners after use.

A live container running in the Player is not evidence of a reproducible MP4. Never leave pointer interaction, background-tab throttling or refresh-rate-dependent motion in the final composition.

## Compose the content

- Bound particles to the scene duration. Define whether particles persist across cuts, fade out, or are intentionally cropped.
- Keep density low around Thai captions, product labels and CTAs; use masks or emitter placement to protect readability.
- Use aspect-aware dimensions. Do not stretch a baked portrait effect into landscape without checking particle scale and motion.
- Pair impact bursts with a pre-rendered sound asset rather than a browser sound callback.

## Validate

- For a deterministic adapter, render shuffled and repeated frames and compare the results. For a baked asset, verify stable playback/seek against its recorded frame rate and duration.
- Check the first and last visible particles, loop seams, clipping and alpha fringes at delivery resolution.
- Inspect a short MP4 export under the actual renderer. Record CPU/GPU cost and lower the particle budget before adding emitters.
- Preserve attribution for external textures, presets and audio separately from the MIT engine license.

## Sources and status

[tsParticles README](https://github.com/tsparticles/tsparticles/blob/main/README.md) and [MIT license](https://github.com/tsparticles/tsparticles/blob/main/LICENSE) were reviewed. [Metadata](references/upstream.json) documents the source snapshot. No deterministic export adapter or runtime installation is claimed by this skill.
