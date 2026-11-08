---
name: motion-remotion
description: "Create or extend frame-driven React video templates, scenes, captions, and MP4 renders in BigO Content Studio using its existing Remotion engine."
---

# Remotion content production

Use the installed Content Studio engine for React-authored videos, reusable motion templates, and batchable scene compositions.

## Project entry points

Read [project integration](../motion-studio/references/project-integration.md) before editing the app and [render contract](../motion-studio/references/render-contract.md) before animating.
Read [upstream evidence](references/upstream.json) when checking dependency or license decisions.

- Work from `content-studio/`; inspect `package.json` and the lockfile before adding packages.
- The current app pins its Remotion packages to the same version. Keep that alignment; do not upgrade the engine as a side effect of producing a clip.
- Extend `src/remotion/templates/` through `TemplateDef` in `src/remotion/core.ts` and register the result in `templates/index.ts`.
- Preview and export share `Main`. Keep narration, caption timing, transitions, and brand overlays in that shared path.
- Use the existing Content/Scene model, settings cascade, and render API rather than creating a second project database or render queue.

## Build the shot

Translate the requested idea into scene purpose, duration, focal object, narration, and one clear motion hierarchy.
Start with an existing template when it fits; introduce a new template only for reusable composition behavior.

- Derive animation from `useCurrentFrame()`, `useVideoConfig()`, interpolation, and Remotion springs.
- Express seconds as frames using the composition fps. Account for scene-local frames, voice lead-in, and transition overlap.
- Keep caption space, product labels, logos, and platform UI safe areas visible at the requested aspect ratio.
- Keep important text and product identity legible during transitions; motion should support the scene's claim.
- Use the existing image and voice adapters for media. An installed video engine does not imply a configured AI provider.
- Await image, font, and other asynchronous resources through the installed version's rendering APIs.
- Keep remote resources stable or prepare local assets for reproducible delivery.

## Verify and deliver

Use the existing still-preview path to inspect the opening, dense text, transition boundaries, and final CTA.
For a changed template, inspect at least the requested aspect and one substantially different aspect it claims to support.

- Run `npm run typecheck` after code changes.
- Produce a short representative render before a long or repeated batch.
- Check output metadata, duration, audio presence, caption timing, and visual clipping.
- Seek to frames out of order and compare a repeated frame; output must not depend on earlier playback.
- Report the actual output path and validation performed. A render completion flag alone is not editorial or publication approval.

## Source boundary

The upstream repository calls out a special Remotion license with free and company tiers; it is not a blanket permissive license.
Check the license shipped with the installed version when distribution or commercial eligibility matters.
This skill is an original project workflow; it does not install or replace upstream agent skills.
