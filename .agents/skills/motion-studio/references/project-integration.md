# BigO project integration

Paths below are relative to the workspace root `B:/ChatGPT/BigO`; resolve the root
from this file when the checkout moves. Run application commands in `content-studio/`.

## Existing application contracts

| Location | Responsibility |
| --- | --- |
| `content-studio/src/shared/types.ts` | `Project`, `Content`, `Scene`, `Voice`, `RenderJob`, `VideoProps` |
| `content-studio/src/shared/settings.ts` | Defaults -> project ancestors -> content overrides; `buildVideoProps` |
| `content-studio/src/shared/timing.ts` | FPS, lead-in, scene lengths, transition overlap, Thai tokenization |
| `content-studio/src/shared/pronounce.ts` | Spoken pronunciation differs from displayed original text |
| `content-studio/src/remotion/core.ts` | `TemplateDef`, `SceneRenderProps`, layout and speech helpers |
| `content-studio/src/remotion/templates/index.ts` | Template registry used by gallery and renderer |
| `content-studio/src/remotion/Main.tsx`, `Root.tsx` | Composition assembly and calculated metadata |
| `content-studio/src/app/components/MainPreview.tsx` | Same `Main` composition inside Remotion Player |
| `content-studio/server/index.ts` | Express API: content, assets, voice, image, render |
| `content-studio/server/render.ts` | Bundle cache, still frames, sequential render queue, H.264 MP4 |
| `content-studio/server/tts/`, `server/images/` | Provider adapters; inspect interfaces before extending |
| `content-studio/server/media.ts` | Media path containment, audio conversion, duration probing |
| `content-studio/mcp/server.mjs` | MCP wrapper around the same API |
| `content-studio/src/remotion/effects/`, `src/remotion/library/` | Effects library: frame-driven WebGL shaders, pattern wipes, graphic cards (`scene.fx`, `settings.overlayId`); see `content-studio/docs/effects-library.md` |
| `content-studio/server/recap.ts`, `server/recap/` | Local video/link ingestion, ASR, draft review and ordinary content creation |
| `content-studio/src/shared/recap.ts`, `src/app/components/RecapPage.tsx` | Typed recap jobs and the dedicated source-to-export UI |

`data/db.json` is app-owned persistence. `storage/` contains uploaded media, voices,
generated audio/images, and renders. Inspect through API/MCP while the app runs;
editing JSON externally can be overwritten by its in-memory state. Do not expose
`.env` values or put secrets in prompts, catalogue metadata, output notes, or logs.

The project has Remotion `4.0.538` packages and FFmpeg integration at authoring time.
The `motion-showcase` demo additionally uses a baked Matter.js simulation and
Three.js math projected to SVG. These are focused demo integrations, not general
physics/3D editor features. See the catalogue for current integration status.
Check `package.json` and lockfile on each integration; keep all Remotion package
versions aligned. Entries marked on-demand are documented capabilities,
not proof of installation, tested compatibility, or provider readiness.

## Enter through the available interface

- Read-only HTTP: `GET /api/state`, `/api/options`, `/api/renders?contentId=...`.
  Development API defaults to `http://localhost:3001`; web to port `5173`.
- Local health endpoints default to `http://127.0.0.1:8765/health` for F5-TTS and
  `http://127.0.0.1:8766/health` for images. Honor configured endpoint overrides.
  A healthy/loaded response does not prove generation or GPU capacity for a new job.
- MCP: inspect available tool schemas, then use `list_projects`, `get_content`,
  `list_options`, `create_content`/`update_content`, `voice_content`,
  `preview_frames`, `render_content`, and `list_renders` as needed.
  All MCP data tools using the shared API helper can start the API if absent,
  including `list_projects`, `get_content`, and `studio_status`. A read-only tool
  annotation does not guarantee process-free inspection. For an explicitly
  no-start check, use direct HTTP GET against an existing service or inspect source
  and a read-only data snapshot. Do not start a second server on an occupied port.
- MCP `get_image_prompts`/`set_scene_image` can exchange prompts and local image
  files. Browser control depends on separately available tools and access; the MCP
  server does not itself provide a logged-in browser.
- For API endpoints not named here, read `server/index.ts`; do not invent routes.

Current bulk image generation can choose OpenAI automatically when a key is ready.
Select a provider consistent with the user's budget rather than accidentally
spending through a default. Reuse any existing session authorization; routine
local production does not need an additional permission checkpoint. Reconcile an
uncertain provider job before retrying it. Mock media must be identified as mock.

## Extend a template

1. Read a comparable template and `TemplateDef`/`SceneRenderProps`.
2. Add its component under `src/remotion/templates/`, with a stable ID, sample
   scenes, recommended settings, and editor guide only where useful.
3. Register it in `TEMPLATES`. Use `layout.s` and dimensions for all supported
   aspects; UI and export must consume the same component and asset URLs.
4. When a feature needs stored fields, update shared types, API validation and
   serialization, editor input, and `buildVideoProps` together. An unknown field
   added only in the browser can be dropped by the current API scene mapper.
5. Read [render-contract.md](render-contract.md) before choosing an animation clock.

For generated audio, keep the original authored script in `Scene.text`, actual
source text in `audioText`, measured duration in `audioDurationSec`, and timing
provenance accurate. Resolve the project's selected `voiceId` and inspect that
profile before choosing a provider. Some seeded voices are explicitly demos;
available F5 hardware does not justify switching an inherited ElevenLabs voice or
substituting a demo speaker. Local F5 is an existing Thai voice path. Replacing it
or adding Chatterbox is an implementation task, not a side effect of reading a skill.
The general content PUT intentionally preserves server-owned audio fields; use
the scene voice/audio endpoints to change audio. An ASR integration that persists
`Scene.words` requires an explicit validated endpoint/adapter change.

## Save, render, and verify

The UI's current autosave/flush can swallow a failed save. Before expensive work,
read back content and confirm that the relevant scene text/settings were persisted;
do not infer success from a spinner stopping. `rendered` status does not establish
that an earlier export contains the latest visual settings. Render jobs currently
refer to content by ID, not an immutable snapshot; keep that content stable until
the job finishes, or implement snapshotting when that feature is requested.

An exact target duration must follow `timing.ts`: measured scene audio takes
precedence over manual `durationSec`. Fit the narration and scene plan while
accounting for lead-in, tail, minimum scene duration, frame rounding and transition
overlap; setting `durationSec` alone cannot force a voiced clip to the target.

Use `npm run typecheck` after TypeScript changes. Use `preview_frames` when MCP is
available; sample stills alone do not establish motion quality. The existing CLI
`npx tsx scripts/template-stills.ts <templateId> [aspectId]` renders built-in samples
and assumes the API/media origin in that script; inspect it for custom ports.
For an actual content use the API still/render endpoints and verify the matching
render job ID plus output file. Interrupted render jobs become errors on restart;
the current queue does not resume them automatically.

For final delivery, inspect first/last frames and transitions, listen to the actual
export when feasible, and use ffprobe/FFmpeg for stream and decode checks. Distinguish
metadata/decode checks, visual review, and human listening in the delivery note.

## Source-video recaps

For a link/upload -> transcript -> reviewed narration -> source-footage recap,
open `/#/recap` or use `start_recap`/`get_recap_job`/`create_recap_contents`.
Read the [Recap Studio guide](../../../../content-studio/docs/recap-studio.md) first.
Use the dedicated recap upload route: the general `/api/upload` converts video
uploads to audio and is not a raw-video import route.

`Scene.videoUrl` and `videoDurationSec` describe pre-cut local footage used by the
`video-recap` template. Preserve these fields when editing narration. The source
audio is muted; narration and captions still use the shared production contracts.
Review ASR errors and source shot ranges. The default draft is extractive selection,
not LLM rewriting or translation. Local-model inference is optional and must report
actual availability. Review before committing production; existing task authorization
can cover that review and production without an extra approval checkpoint.

One reviewed recap creates one content per chosen aspect and reuses audio files.
The resolved voice is frozen per job. Job `done` means creation/queue submission;
only the corresponding render jobs and files establish completed MP4 exports.
