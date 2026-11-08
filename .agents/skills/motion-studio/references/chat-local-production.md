# AI chat → local files → Director Studio

Use this workflow for reusable page/content recipes, style comparisons and assets
made through Cowork, Codex Work or the current AI chat. The owner's primary route
combines tools available in that chat with local assembly and review. It does not
require an external API key. Existing channel/provider decisions still apply.

## Prepare a saved recipe and real references

Open **Director Studio** (`ProductionStudioPage`) and choose or create a recipe in
**สูตรเพจ**. Set the actual subject, style, palette, character, action, location,
camera, aspect, duration and sound requirements. The built-in starter recipe is
`director-studio-courier-walk`. Save edits before copying or handing off so the
recipe ID and revision identify the brief being produced.

Open the selected style image and character/location references. Preserve the
requested characters and subject; the style image's example scene supplies visual
direction only. Record immutable traits, outfit and proportions in the character
record. A quality profile describes preparation and review work, not an automatic
model switch or a quality guarantee.

**ก็อปปี้สูตร + ref V2** produces a textual `BIGO_PRODUCTION_REF_V2` brief. For
portable work between chats, use **สร้างโฟลเดอร์งานสำหรับ AI** in the Cowork/Codex
handoff panel. It snapshots the saved recipe and copies the actual references,
including any bound motion preview, into:

```text
content-studio/out/production-handoffs/<jobId>/
  TASK.md
  production-ref.json
  references/<hash>.<extension>
  outputs/
    RESULTS.schema.json
```

The handoff uses relative file references and includes hashes, so the receiving
chat can work from the folder without a running localhost website. The button
prepares this package; open the folder in the intended chat and use **ก็อปปี้คำสั่งงาน
+ โฟลเดอร์** to pass the task. If the receiving chat cannot access that filesystem,
attach the actual task/reference files through its supported interface. A pasted
local path alone does not give a remote chat access to the bytes.

`TASK.md` and `production-ref.json` are checked against the job receipt when
collecting. Keep them intact; save changes to the brief as a new recipe version
and create a new handoff. Resume an existing job from **เปิดคำสั่ง** when its inputs
are unchanged.

## Produce in the chat, assemble locally

Use the current chat's image generation/editing tool when available and preserve
its real output files. An available chat tool can generate images without setting
up an API key in this project. Record the tool and creation method actually used;
do not imply that the app invoked a provider or conditioned a model on a reference
merely because the reference was attached. Inspect edit inputs before use.

Choose the motion route that the assets can support:

| Route | Actual source needed | What the current player can establish |
| --- | --- | --- |
| `rig` | Built-in `courier-blocky`, body type `blocky`, style `graphic-blocky-avatar` and a supported built-in action/world | Articulated idle, walk, wave, clap, held-heart prop or dance, plus true 3D cameras |
| `frames` | Ordered source images of the chosen character doing the action, with positive per-pose exposures and a loop choice | The supplied pose sequence, holding the final frame when loop is disabled |
| `layers` | An actual image, `idle` subject action and a supported 2D camera move | Crop, pan or zoom on that image; an orbit requires spatial assets |
| `video` | An actual locally imported video explicitly selected in the recipe's reference assets | Playback of that chosen footage with the selected source-loop behavior; motion preview clips remain demonstrations |

A new reference image, character name, body-type label or uploaded GLB does not
automatically acquire the courier's rig. For another character/style, prepare its
own pose frames or video, or author a compatible rig as explicit implementation
work. `layers` currently displays a single flattened image; separate cutout
articulation needs the relevant GSAP/rig template. The live player does not
repaint an existing rig into every style or rebuild a world from its photo.

For a pose sequence, use
[frame-sequence-animation](../../frame-sequence-animation/SKILL.md): retain RGBA
masters, choose consistent camera/scale and ordered poses, direct contact and
exposures, then assemble a GIF/MP4 preview with local tools. Derive exposures from
the source pose rate when equal timing fits the action. Keep source pose rate
separate from export FPS. A generated sheet needs actual cell extraction and
action review before it becomes a usable motion asset.

Use Remotion, FFmpeg, GSAP, Three.js/Blender or Opuscar according to the chosen
shot, following their project skills. Generate expensive assets outside the render
loop and keep exported motion driven by frame/time/seed. When a chat tool is
unavailable, use suitable existing assets or a supported local production route;
report the concrete missing capability before changing the owner's provider plan.
The handoff and collector themselves make no external generation calls. They do
not measure subscription usage or prove that a chat provider has zero cost.

Bind real imported music, ambience or effects to sound cue slots when wanted.
Unbound cue slots remain silent. Respect a no-narration brief, and retain
actual audio provenance; a cue name is not evidence of an audio file.

## Return real files and collect

Write finished files inside the handoff's `outputs/` directory, preserving source
masters and production notes. Create `outputs/RESULTS.json` using the provided
`RESULTS.schema.json`. For example:

```json
{
  "version": 1,
  "outputs": [
    {
      "file": "courier-wave.mp4",
      "name": "Mika wave — local motion render",
      "styleId": "graphic-blocky-avatar",
      "notes": "Original rig rendered locally; silent clip. Describe actual source tools and remaining review here."
    }
  ]
}
```

`file` is a relative path inside `outputs/`, using forward slashes for subfolders.
List the real files to import, up to 16 entries per result manifest; keep additional
masters alongside them and import larger ordered frame sets through the supported
media/motion library workflow. The current collector accepts supported media and
JSON files, not an arbitrary directory or archive. Each returned file is limited
to 50 MB and the collection to 100 MB. Do not place placeholders in the manifest
as completed work.

For an A/B style comparison, return one actual image per selected `styleId`, keep
the subject and character consistent, and label each result with its matching
style ID. The comparison accepts image candidates; motion previews are separate
assets. Leave the winner for the owner's review.

Use **เก็บผลจากโฟลเดอร์** to inspect and register the returned bytes in the managed
asset library. If `RESULTS.json` is absent, the job stays pending; creating the
handoff alone is not generated work. Collection validates the files and retains
hashes/provenance, imports assets as `unreviewed`, and reuses an unchanged result
receipt. A completed receipt is immutable: revised outputs need a new handoff.

For agent operation, the corresponding local application endpoints are:

- `GET /api/production/recipes/:id/brief`
- `POST /api/production/handoffs` with `recipeId`, a stable `requestId`, and an
  optional `comparisonId`
- `GET /api/production/handoffs/:id` to resume its task/folder
- `POST /api/production/handoffs/:id/collect` to register actual returned files

Use these application interfaces for owned records. Writing the designated output
files is part of the handoff contract; editing the app's persistence JSON is not.

## Bind, review and finish

After collection, choose the actual assets in the character, motion and location
records. Set ordered frame IDs/exposures and loop choice for `frames`. For `video`,
select the actual source video in the recipe's references; its motion demonstration
is not substituted as footage. Use a new recipe version for changed bindings.
Check a representative moving shot in the player, then choose **เปิดเป็นคอนเทนต์**
with the intended destination project and finish the content through the normal
editor/render workflow. A collected image or clip is not automatically a complete
editable story or a new character rig.

Verify source detail at the largest shot scale, identity/outfit continuity, hand
and foot contact, joint motion, loop joins, aspect framing and actual sound cue
timing. Inspect direct/backward seeks for frame independence, then probe and fully
decode the exported media. Use earshot/ASR where relevant and distinguish those
checks from human visual/listening approval. Report the real output paths,
dimensions/duration, production method, tests and remaining review. Export and
collection do not establish platform publication.
