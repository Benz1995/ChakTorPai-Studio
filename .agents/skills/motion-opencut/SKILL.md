---
name: motion-opencut
description: Prepare an editable handoff or perform requested timeline edits in OpenCut using verified features of the selected release. Use for optional finishing work, not as an assumed API or replacement for the existing Remotion editor.
---

# OpenCut editing handoff

Read [project integration](../motion-studio/references/project-integration.md) and the [render contract](../motion-studio/references/render-contract.md). Consult [upstream verification](references/upstream.json) before selecting the application branch.

## Establish which OpenCut is available

- The requested `OpenCut-app/OpenCut` README, verified on 2026-10-26, says the application is being rewritten.
- That README describes the Editor API, plugin architecture, MCP server, and headless mode as upcoming work. Do not assume those are available integrations.
- It points current users to `opencut-app/opencut-classic` and says `opencut.app` runs the classic version. Inspect the actual release/application before promising import, export, automation, or timeline interchange.
- Record which app/version is used. A later version may change this snapshot; recheck upstream when implementing against it.

## Select a useful editing boundary

- Keep Content Studio as the owner of its project/scene data and deterministic Remotion render.
- Use a separate editor when the user wants manual clip trimming, arrangement, or a finishing pass that the current scene model does not represent.
- Decide whether the handoff is a finished MP4 or separately rendered scenes with audio and caption sidecars. A single flattened MP4 cannot preserve independent text, image, or animation layers.
- Inspect supported import/export formats in the actual app; do not invent an interchange JSON schema from its repository name.

## Prepare and edit

1. Create a dedicated handoff directory with clearly named source clips, audio, caption sidecars, and a manifest recording FPS, aspect, duration, order, and asset origins.
2. Preserve existing masters. Work on derivatives or an editor project copy so a finishing pass remains reproducible.
3. Match editor sequence dimensions and FPS to the requested delivery. Account for Remotion scene transition overlaps when exporting individual scenes.
4. Import through features observed in the selected application. If a desired feature is absent, finish that operation through Remotion/FFmpeg and document the handoff boundary.
5. Save the editable editor project when the selected version supports it, then export a uniquely named derivative.
6. Keep local media local when using an installed workflow; inspect actual upload/storage behavior before handing private assets to a hosted application.

## Integrate only demonstrated interfaces

- This skill does not add OpenCut as a dependency, embed it in the React app, or make an upcoming MCP/headless endpoint exist.
- A future adapter should target documented, released interfaces and maintain the same input/output manifest used by the handoff.
- Avoid starting the rewrite's development server on this project's Vite port 5173; inspect occupied ports and configure an isolated environment when development is requested.
- Treat an editor's project save, export completion, and final delivery as separate observable states.

## Verify observable output

- Reopen the saved project or handoff and check that media resolves without accidental absolute-path dependencies.
- Probe the export for dimensions, frame rate, codecs, duration, and audio tracks.
- Watch all edited cuts and text-heavy frames; listen for pops, truncated words, and A/V drift.
- Deliver the exported derivative and available editable sources with clear provenance. Exporting does not publish the video.

## Sources

[OpenCut current status and development README](https://github.com/OpenCut-app/OpenCut/blob/main/README.md), [license](https://github.com/OpenCut-app/OpenCut/blob/main/LICENSE).
