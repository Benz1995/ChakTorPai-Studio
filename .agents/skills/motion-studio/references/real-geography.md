# Real geographic sources and map editing

Use for actual places, routes, regional explainers and terrain shots. The owner
explicitly accepts web research and Google Maps captures combined with other
media. Research the location and relevant primary facts, then acquire the source;
do not stop at a synthetic mountain because no importer was preinstalled.

## Choose a route for the requested shot

| Need | Smallest useful route |
|---|---|
| Locate a place, show roads or add editorial pins | Capture a small number of views through Google Maps' real browser UI; preserve original provider credits |
| Reveal landform, orbit a ridge or inspect height | Fetch an appropriate open DEM, generate a reduced mesh, and drive the camera from timeline frames |
| Photographic surface | Use permitted satellite imagery as its own source, or a map capture as a separate edit shot; verify vintage and license for the intended use |

Google Maps imagery and elevation are separate inputs. Do not reconstruct 3D
geometry from Google Earth/Maps output or imply that a screenshot contains usable
DEM measurements. A captured still with a camera pan remains a moving still;
describe the separate DEM shot as the actual spatial camera move.

## Capture and edit

Use supported browser controls; inspect the visible map after it finishes loading.
Confirm the place/pin, view type and scale before saving. Avoid capturing account
menus, personal locations, search history or unrelated sidebars. Keep the original
image, source URL, capture date, viewport and visible attribution in a receipt.

For a map-only shot, deliver the map surface without browser controls, account
avatars, side panels or an added explanatory title/callout. Keep the map labels
and provider attribution; use additional editorial annotations when the brief
calls for them. If reframing, keep a nearby legible source-credit strip.

For a video, keep Google/provider attribution visible for every frame containing
the map. Do not crop, obscure or leave it only in end credits. If an edit makes
the original credit too small, also reproduce the exact credit close to the map
at a readable size. Add labels, pointers and narrative context without misleadingly
altering the underlying imagery. A capture date is not the imagery acquisition date.

Google's [Geo Guidelines](https://about.google/brand-resource-center/products-and-services/geo-guidelines/)
were checked on 6 Nov 2026: educational/instructional/recreational/entertainment
online videos can use Maps with the stated attribution requirements. Advertising
and promotional uses have additional approval restrictions; satellite imagery has
the Earth restrictions. Street View has separate screenshot/context restrictions.
Verify the current rules for the specific intended output, rather than treating
this reference as an all-purpose rights clearance.

## Bounded terrain acquisition

The local [fetch-terrain.py](../scripts/fetch-terrain.py) downloads documented public
[Terrain Tiles on AWS](https://registry.opendata.aws/terrain-tiles/), caches originals,
decodes Terrarium RGB into metres, and exports a geographic JSON grid with hashes
and provenance. It requires existing Pillow and the standard Python library; no
provider key or billing is configured. Keep raw sources out of git.

Run from the repository root, choosing bounds for the actual location:

```powershell
python -X utf8 .agents/skills/motion-studio/scripts/fetch-terrain.py `
  --bounds 98.42 18.53 98.55 18.65 --zoom 12 --grid 65 `
  --landmark 18.5880431 98.4870612 --out content-studio/out/real-map-inthanon
```

Bounds are west/south/east/north; optional landmark is latitude/longitude. Requests
are capped at 16 source tiles per invocation. Invalid bounds, excessive requests,
unexpected image dimensions and invalid/flat heights fail explicitly. Review the
extent instead of repeatedly subdividing to evade this bounded sample workflow.

The 6 Nov 2026 Doi Inthanon run downloaded nine z12 tiles, about 36 m source pixel
spacing, then sampled a 65×65 mesh over approximately 13.7×13.4 km. This reduced mesh
is coarser than the source. The helper also ran from its cache. The known summit
coordinate sampled about 2,574 m from the source, while the government's published
peak elevation is 2,565 m. Preserve the difference; do not change the DEM to force
agreement. Local source vintage and vertical datum were not independently verified.

Render in local metric coordinates, keep north/south orientation consistent and
retain any exaggeration factor (the demonstration uses vertical ×2). Credit
Mapzen/AWS Terrain Tiles and applicable underlying sources per the dataset's
[attribution documentation](https://github.com/tilezen/joerd/blob/master/docs/attribution.md).
Do not call a shaded elevation mesh satellite imagery or survey-grade measurement.

## Acquisition evidence and review

Retain URLs, retrieval time, original hashes, bounds, projection/resampling, mesh
resolution, landmark source, image date limits and credit text. Review the location
against the map and known landmarks, then inspect occlusion, camera clearance and
start/end framing. Decode the actual video and report its dimensions/duration.
Keep source verification, technical render checks and editorial approval separate.

Sources for the Doi Inthanon example:

- [Thai government PRD: peak elevation](https://thailand.prd.go.th/en/content/category/detail/id/2078/iid/541938)
- [Terrain registry](https://registry.opendata.aws/terrain-tiles/)
- [Terrarium format and decoding](https://github.com/tilezen/joerd/blob/master/docs/formats.md)
- [Google map location](https://www.google.com/maps/search/?api=1&query=18.5880431,98.4870612)

The source code and per-attempt receipts for the local demonstration are under
`content-studio/out/real-map-inthanon/`. This output directory is a local artifact,
not an installed app template, publication receipt or durable upstream fixture.
