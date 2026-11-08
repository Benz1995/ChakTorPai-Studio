---
name: frame-sequence-animation
description: Create reusable short animations for BigO videos from ordered image frames or a sprite sheet (ภาพหลายเฟรมต่อกัน, flipbook, stop motion, pose sequences, looping GIF). Plan the action, generate consistent art through the available image workflow, assemble timed GIF/MP4 assets, and integrate them with existing templates. Use for actual subject pose changes or economical repeated loops; use gpt-motion-story for a whole illustrated narrative and native motion tools for editable diagrams or long articulated action.
---

# Frame sequence animation

Turn a small set of well-designed poses into a moving shot. This is a reusable video
asset workflow, not merely a contact sheet, nor a claim that crossfading stills creates
convincing motion. It can serve ads, explainers, music visuals and narrative inserts
when the project's own rules permit the chosen style and provider.

For professional production or a quality rebuild, read
[professional-production.md](references/professional-production.md): pixel budget,
RGBA masters, drawing exposures, support anchors, compositing and edit review. Use
its read-only `scripts/audit.py` before scaling a small sheet into a hero shot. GIF
is a useful review/delivery derivative; keep full-color source frames for compositing.

## Choose the shot and route

Inherit the project's brief, assets, brand, voice, budget and publication scope. Follow
the shared [integration](../motion-studio/references/project-integration.md) and
[render contract](../motion-studio/references/render-contract.md). Read
[animation-principles](../animation-principles/SKILL.md) for action timing and contact;
use [art-motion](../art-motion/SKILL.md) for visual direction rather than primitive
stand-ins. For a whole illustrated story, combine with
[gpt-motion-story](../gpt-motion-story/SKILL.md).

| Shot requirement | Good starting route | Main tradeoff |
| --- | --- | --- |
| Consistent framing, one brief action or looping subject | One grid sprite sheet, then slice cells | Fewer generation requests, but fewer pixels per pose and possible uneven cells |
| Detailed poses, complex silhouette or larger final framing | Separate numbered frames using the same style/identity reference | More requests and more opportunity for identity/camera drift |
| Steam, light, a blink or a decorative loop; direct GIF tool actually available | Generate GIF, inspect its real frames and timing, then use the existing GIF workflow | Tool/account availability and output controls vary; do not assume every image tool emits GIF |
| Editable labels, maps, charts, precise transforms | Existing Remotion / vector / shader tools | Often more controllable than generating each frame |
| Sustained acting, speech, intricate contact, moving camera | A rig, 3D or the project's approved video workflow | A few unrelated poses will not substitute for the required action |

## Plan before generating

Write a compact shot record: purpose, start/end state, key poses, contact/occlusion,
camera lock, light/palette, aspect, background/alpha, unique poses, pose durations,
playback mode and reuse. Pick a visual style appropriate to the audience; mature
channels retain their existing art direction. Use a representative style frame and
inspect it before requesting the rest. Keep Thai captions and labels in the compositor.

For efficiency, first try the smallest pose set that reads clearly at delivery size.
For example, a subtle 1–2 second loop might need 6–12 distinct drawings; an intentional
stop-motion look may hold each drawing longer. These are starting points, not a
quality threshold. Source-pose rate and the final video's FPS are different: exporting
8 drawings at 30 FPS repeats drawings, it does not create 30 new poses per second.

Use the available `imagegen` skill/tool for GPT raster generation, preserving its
current route and reference-image rules. A sprite sheet is one raster request for
related animation poses, not a batch of unrelated pictures. If a reference is a local
file, inspect it before using it in an edit. Do not switch to a paid API, purchase
credits or switch accounts just because this skill exists. Only read the
[prompt and manifest reference](references/production.md) when generating or assembling.

Lock identity, proportions, palette, light, lens, canvas dimensions, subject anchor
and prop count across poses. Describe preparation → action/contact → settle, with
small comprehensible changes. For a sheet specify equal cells, exact grid and reading
order, empty clearance, no labels/borders and no subject spilling into another cell.
Verify the actual grid; prompting does not guarantee correct geometry. For individual
frames use explicit manifest order; never rely on a directory's lexical sort.

## Assemble with the included helper

Use Python 3.10+, Pillow and FFmpeg/ffprobe already present in the selected environment.
Check imports/binaries; do not modify global Python or install packages as a side effect.
From the repository root:

```powershell
python .agents/skills/frame-sequence-animation/scripts/assemble.py --manifest <shot.json> --out <new-output-directory>
```

The [manifest reference](references/production.md#assembly-manifest) defines both sheet
and ordered-frame inputs. The helper slices a uniform sheet or reads explicit frames,
preserves RGBA PNGs, makes a contact sheet, GIF and opaque MP4 preview, then probes and
fully decodes the MP4. Output must be a new directory. No provider calls or content DB
writes occur. Existing sources are never overwritten. It records hashes, crop boxes,
pose order, requested/encoded timing, commands and output metadata in `receipt.json`.

Choose `once`, `loop` or `pingpong` deliberately. Ping-pong fits reversible movement
such as a sway; it makes poured liquid flow backwards and is wrong for irreversible
actions. A loop should omit a duplicate endpoint unless it is an intentional hold.
GIF duration uses 10 ms units. MP4 timing is quantized to the requested output FPS
with cumulative rounding; inspect `video_holds` in the receipt. The MP4 contains one
cycle; looping is a composition decision. Its matte color is explicit in the manifest.
Keep the PNG frames/GIF when alpha matters; H.264 MP4 does not preserve transparency.

## Integrate and review

- **GIF:** upload through `set_scene_image` or the scene's **อัปโหลดรูป / GIF** control.
  Read [GPT GIF workflow](../../../content-studio/docs/gpt-gif-workflow.md). The current
  scene-image player repeats GIFs; for an action that must play once, use a video shot
  or explicit frame selection instead. Do not claim the GIF's loop flag overrides it.
- **MP4:** import unchanged with MCP `import_3d_asset` or `/api/three/upload`, then set
  `scene.videoUrl` and `videoDurationSec` through the content API/MCP in a template that
  reads them (for example `video-recap`). Inspect that template's looping semantics.
  Generic `/api/upload` converts video into audio and is unsuitable for this path.
- **Editable frame composition:** when needed, use [motion-remotion](../motion-remotion/SKILL.md)
  to choose an image from cumulative holds using scene-local `useCurrentFrame()` and
  FPS. Hold via `Img`, preload the required sources and verify out-of-order seeking.
  Never use timers or browser autoplay as the exported animation clock.

Review one moving proof at delivery size before generating a batch. Inspect silhouettes,
identity, alignment, body/prop contact, popping textures, cropping, alpha halos and
the transition from last to first pose. Use dense frames around contact and the loop
join, plus playback when available; say if only frames were inspected. A contact sheet
and clean decode do not establish appealing motion. Repair or regenerate the failed
poses; do not mask anatomical or continuity failures with interpolation or crossfades.

Only add in-between drawings where timing or pose spacing needs them. Optical-flow
interpolation is optional, not the default; if deliberately used, inspect its new
frames for warped hands, edges and props. Loop reuse reduces repeated work, but does
not make a long repeated sequence narratively appropriate.

Deliver the moving file plus the manifest/receipt and asset provenance (route,
verbatim prompts/references, attempts, selected/rejected status). Record unique poses,
generation attempts, reusable assets, measured render time if comparing efficiency,
and remaining review limits. Do not invent price or speed savings, listening approval,
rights clearance or publication from successful assembly.
