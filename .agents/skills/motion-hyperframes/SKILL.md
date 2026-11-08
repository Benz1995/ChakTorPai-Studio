---
name: motion-hyperframes
description: "Author seekable HTML/CSS motion videos with HyperFrames as a separate render path when a content request calls for HTML-native video production."
---

# HyperFrames HTML video

Use for HTML/CSS-authored clips, seekable web-native motion, and deliberate experiments outside the current React composition path.

Read [project integration](../motion-studio/references/project-integration.md), [render contract](../motion-studio/references/render-contract.md), and [upstream evidence](references/upstream.json).

## Choose the path

HyperFrames is an alternative authoring and rendering path, not a drop-in Remotion template or an existing Content Studio backend provider.

- Keep a HyperFrames job in its own output/project directory under the requested content workspace.
- Keep the existing Remotion app working unless the user requested a migration.
- Inspect local availability first. If the actual production task needs HyperFrames, use a project-local pinned dependency or the verified CLI for that job.
- Upstream currently specifies Node.js 22+ and FFmpeg. Verify the chosen release and CLI help before executing it.
- Read the relevant upstream CLI/animation documentation for the installed version; do not import upstream skill instructions wholesale.

## Author a seekable composition

Define canvas dimensions, composition identity, track order, clip start/duration, and audio placement explicitly.
The upstream format uses HTML data attributes and seekable animation adapters.

- Keep animation timelines paused and externally seekable. The renderer must be able to request a timestamp without playing from zero in wall time.
- Use the renderer's supported adapter for GSAP, CSS, Anime.js, Three.js, or custom runtime behavior.
- Bind all visuals to the same composition time. Avoid independent CSS loops, browser timers, and uncontrolled simulation.
- Await fonts, images, video readiness, and shader resources before frame capture.
- Copy or resolve media into stable job assets; avoid CDN changes becoming part of a deliverable.
- Declare narration and music as timed audio tracks so the renderer can mix them; browser speaker playback is not an export track.

## Integrate only what the task requires

For a standalone content job, deliver the HTML source, local assets, configuration, and rendered MP4 together.
If Content Studio needs the result, integrate through a documented media or render adapter after reviewing the existing Scene and VideoProps contracts.

- Do not silently write HyperFrames state into `data/db.json`.
- Do not promise the current preview or queue can inspect native HyperFrames compositions.
- Reuse approved narration, brand tokens, and editorial structure across the authored deliverable where the user requested it.

## Verification

Run the installed CLI's validation/lint and inspect representative frames before final export.
Check first/last frames, timeline boundaries, typography, audio placement, duration, and exact dimensions.

Render a short sample and request the same timestamp twice, including after a backward seek.
Record the exact engine/package versions and output files.
Distinguish a standalone rendered deliverable from a completed integration into the current app.

## Upstream terms

The checked repository is Apache-2.0. Preserve relevant notices when distributing its code.
Third-party media and adapters have their own terms; the framework's license does not cover those assets.
