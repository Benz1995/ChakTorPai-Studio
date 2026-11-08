# Visual formats: turn a claim into an event

Use when the request calls for a specific explanatory format, or a style-led draft
has attractive surfaces but fails to explain its subject. These are authoring
recipes using BigO's tools, not newly installed templates or tested productions.
Preserve the channel's established look, voice, budget and publication scope.

## Choose the mechanism

Start from what the viewer must understand: a change, a route, a cause, a hidden
part, or evidence in footage. Then choose the smallest relevant route below.
Use live `list_options` / `GET /api/options` and the effects library for IDs;
use `use_template_sample` only on a requested working draft, since it fills content.
Inspect the selected template's source/sample before promising new behavior.

Priority is a local recommendation, not a measured business forecast. Difficulty
and code complexity are relative estimates for a first representative shot.
Value, revenue applicability, reuse and novelty are qualitative judgments (H/M/L).
All rows require actual visual review before production use.

| Rank | Format and viewer benefit | Existing starting point | Smallest work / limit | Difficulty / code | Value / revenue / reuse / novelty |
|---|---|---|---|---|---|
| 1 | One chart, one finding: see where a trend changes | `lineChart`, `bigStat`, `motion-remotion` | Author sourced data and timed reveal; confirm axes/units | Low / low | H / M / H / L |
| 2 | Architecture journey: follow one request and its failure path | `nodes`, `motion-remotion`, SVG | Existing template has consecutive links/pulses; branch/cache/retry semantics need authoring | Medium / medium | H / M / H / M |
| 3 | Exploded object: understand what each part does | `studio3d`, `motion-threejs`, existing callout graphics | Author separable geometry, trajectories and projected labels | Medium / medium | H / H / H / M |
| 4 | Annotated replay: see the precise moment supporting a claim | Recap/Highlight source workflow + `motion-remotion` SVG | Author freeze/slow segment and marks with matching source timestamps | Medium / medium | H / M / H / M |
| 5 | Evidence collage: connect a document/detail to a conclusion | `collage`, `callout`, `gpt-motion-story` for illustration layers | Stage cleared sources; animate evidence, preserve attribution | Low / low | H / M / H / L |
| 6 | Layered cutaway: reveal a hidden process | `cutout-motion`, SVG or `motion-threejs` | Author masks/parts and causal order; verify factual internals | Medium / medium | H / H / H / M |
| 7 | Geographic route: understand where and how far | `motion-remotion` SVG / `motion-threejs`, `locationPin` | Author geographic transform and route from sourced coordinates; no verified tile importer | Medium / medium | H / M / H / M |
| 8 | Shadow theatre: read character intent through silhouette | `art-motion`, `animation-principles`, frame sequences or rigs | Design silhouettes, pivots and light; keep contact legible | Medium / medium | M / M / H / M |
| 9 | Isometric process: see dependencies and movement through space | `motion-threejs`, `studio-3d` | Author geometry, occlusion and path; not a dedicated process editor | Medium / medium | M / H / H / M |
| 10 | Real terrain flyover: understand landform and scale | `motion-threejs`, `studio-3d`, bounded [Terrarium fetch helper](../scripts/fetch-terrain.py) | Elevation acquisition is available; author the shot, attribution and camera clearance. Satellite texture is optional and has separate terms | High / high | H / M / H / H |

All formats still need shot-specific authoring. For factual content, research the
subject and reuse suitable real sources before defaulting to synthetic examples.
Rank 10 has a small bounded elevation helper; it is not a general GIS editor.
Do not install a map stack or enable billable services merely to load this reference.

## Direct one shot before batching

Record this compact plan in the existing production note, using prose or a table:

- **Claim and evidence:** what the image demonstrates; source, date, unit and
  whether the data/model is measured, approximate, schematic or fictional.
- **Visible event:** initial state → change → readable result. Name the moving
  subject, fixed anchors and camera purpose; a camera move alone may not explain it.
- **Timing:** the spoken phrase and its reviewed scene-audio interval. Use measured
  audio/word timing when available; otherwise label planned cues as estimates and
  revise after voice generation. Preserve the shared lead-in/scene-offset contract.
- **Route:** existing template/effect, authored extension and any missing capability.
- **Review:** the difficult interval and a short encoded motion proof at delivery
  aspect. Check phone UI/caption clearance and label readability during motion.

These are planning fields, not new API properties. Persist app-owned content through
its existing API/MCP; inspect shared types/validation before adding stored fields.

### A. One chart, one finding

Use one clear question and source-backed values. Reveal the relevant range, pause
at the change, then introduce a callout that states what the chart supports. Keep
units, date range, missing values and axis choices visible enough to interpret.
Do not interpolate across missing observations as though measured. A rising counter
is an entrance effect, not additional data. Separate correlation from causal claims.

Start with `lineChart`/`bigStat` from the effects library. Confirm their current data
contract and supported reveal controls. If they cannot express a required marker or
axis, author a small frame-driven SVG extension rather than imply the option exists.

### B. Follow a request through a system

Start with the `nodes` sample: it already links consecutive bullets and draws a
travelling pulse. For an architecture lesson, explicitly identify client, service,
cache/database and response direction; adapt layout/edges when the model differs
from a chain. Use a single request first. Show a cache hit or failure only when the
narration reaches that event, and keep the original request identifiable across
branches. Treat packet speed as illustrative unless it is driven by measured time.
Review whether viewers can follow the request without relying on the caption.

### C. Reveal and reassemble an object

Use separate meshes or authored layers with stable IDs. Define the assembled
transforms, a clear separation axis/path and a return to those transforms. Bind one
part's reveal to the phrase describing its function; project leader lines from the
actual part into screen-space labels and check overlap at camera extremes.

Real product internals require supplied or verified references. Label a conceptual
model as schematic rather than inventing teardown evidence. Review separation,
occlusion and reassembly in motion. Deterministic keyframes are usually sufficient;
a physics solver is optional when the event actually depends on collision.

### D. Annotate source footage

Keep source time and edit time distinct. Freeze or slow the relevant interval,
draw a deliberate arrow/circle/path, then resume with a clear transition. Anchor
marks to the subject for the used interval, or confine them to a freeze frame;
screen-fixed marks can drift away from moving evidence. A speed change needs a
deliberate audio treatment consistent with the source workflow. Preserve MovieSkit
native sound rules when that workflow applies. Separate observation from inference;
the annotation is commentary, not proof that the inferred event occurred.

### E. Travel over a map or terrain

For a requested real location, read [real-geography.md](real-geography.md). A browser
capture of Google Maps can be an editorial source when its use fits Google's
current guidelines. It can be cut together with a separately sourced DEM shot;
do not treat the lack of an app map plugin as a reason to invent the geography.

For simple geography, start with a sourced vector outline and coordinate transform.
Record coordinate order, projection and units, then test known landmarks. A drawn
route is schematic unless actual routing data establishes the path; do not invent
distance, travel time or an operational disaster forecast from animated geometry.

Terrain is a separate data integration: verify the elevation and imagery providers'
own current terms, attribution, geographic coverage, acquisition dates, resolution
and height reference before fetching. Record any vertical exaggeration and derived
height uncertainty. Cache permitted inputs outside per-frame rendering, check camera
clearance against the mesh and keep labels readable above ridges. Do not infer that
an attractive flyover shows current satellite imagery or survey-grade heights.

## Reuse the production core

Keep narration, captions, audio mix, encoding and provider receipts in the existing
pipeline. A style recipe should supply visual data and choreography; it should not
duplicate provider wrappers or replace an inherited voice. Record actual attempts
and known costs in the current ledger; mark unavailable prices as unknown. A local
render has no per-call provider fee by itself, but still consumes compute/time.

Keep evidence levels separate: documentation read, source code inspected, runtime
resolved, still reviewed, motion reviewed, audio checked and final export verified.
Choose relevant checks rather than inventing a universal automated quality score.

## Inspiration and evidence boundary — 6 Nov 2026

Read [AI วันละเจค's Facebook post](https://www.facebook.com/groups/1745892855948687/permalink/2396845724186727/)
and public [Genhaha skills catalogue](https://videos.genhaha.com/skills). The post
announces multi-host skills/MCP and future integration tutorials; its popularity
claims are the author's statements, not BigO validation.

The [exploded-3D description](https://videos.genhaha.com/skills/exploded-3d) describes
part reveals tied to narration and labelled 3D layers. The
[terrain description](https://videos.genhaha.com/skills/map-terrain) describes staged
elevation/imagery inputs and per-sentence cameras. These public descriptions inspired
the locally authored recipes above. The downloadable packages were not inspected,
installed or executed, and the example films were not reviewed in motion. Provider
licenses, benchmark results and Windows compatibility were not independently tested.
Do not repeat the site's broad free/offline/copyright claims as verified facts.

Local inventory: `GET /api/options` exposed the named template starting points;
`Nodes.tsx` contains consecutive links and travelling pulses. `motion-skills doctor`
resolved Remotion 4.0.538, Three.js and the existing FFmpeg binaries; GSAP and
HyperFrames were not resolvable. Resolution establishes availability, not that any
new recipe has passed an actual render. No new provider, purchase or dependency
is required by this documentation update.
