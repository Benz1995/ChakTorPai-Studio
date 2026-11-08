# Move library (คลังท่า)

A move is a reusable shot recipe: what the narration is telling, which GPT layers it
needs, what code does to them, the route and the usual failure. Moves are starting
points, not templates to paste: adapt the prop, material and timing to the story, but
keep each card's "Breaks when" checks.

The owner may refer to a move by ID or Thai name ("ฉาก 3 ใช้ M09", "เปลี่ยนเป็นท่าสมุดข่อยคลี่").

## Pick rules

1. Tag every narration line with one purpose from the index below.
2. Shortlist two or three moves for it. Choose the one whose visual event shows what
   the line says, then prefer kit assets over new generations, then variety.
3. Before the shot plan, choose the film's vocabulary: four to six moves plus one
   **signature move** that recurs as a motif (opening, middle, ending). Choose one or
   two transition moves for the whole film. A film that uses every move has no style.
4. Avoid repeating the same move on adjacent independent beats. Preserve a continuing
   action across a voice boundary when resetting it would break mechanical or spatial continuity.
5. A line with no event of its own (context, a bridge sentence) gets M20 Hold or lets
   the previous move continue. Do not spend a new generation on it.
6. Write the move ID in the `Move` column of `TREATMENT.md`.
7. A move invented on a job gets a new card here with status `trial`.

## Asset kit

ชุดภาพกลาง: generate once per film from one selected style frame, then let moves draw from it:

- the style frame itself (the reference for every later generation);
- one background plate per location, without people, with clearance for compositing;
- main-character cutouts: three-quarter front, back and side views. For a real person
  without a usable identity reference, back and side views only;
- a prop set of cutouts, including the signature-move prop;
- blank document material (paper, notebook, samut khoi panel, palm leaf);
- one foreground occluder per location (foliage, doorframe, crowd backs).

Mark kit rows `kit` in `assets/ASSETS.md`. The `+N` on each card counts generations beyond the kit.

## Index

| Purpose | Moves |
| --- | --- |
| Introduce a person or place | M01 Foreground reveal · M02 Rack focus · M03 Mural layers |
| Time or era changes | M04 Same frame, two eras · M05 Light pass · M06 Date flip |
| Place, route, journey | M07 Scene to map · M08 Route ride |
| Document, evidence, record | M09 Samut khoi unfolds · M10 Palm-leaf fan · M11 Paper insert · M12 Photo push-through |
| Cause and effect | M13 Rising element · M14 Baked chain reaction |
| Number, quantity, scale | M15 Count fill · M16 Scale ladder · M17 Stat over scene |
| Comparison | M18 Split worlds |
| Peak, emotion, weight | M19 Backlit silhouette · M20 Hold |
| Ending | M21 Pull back to the world · M22 Callback prop |
| Transition between beats | T01 Shape match cut · T02 Foreground wipe · T03 Noise-mask bleed · T04 Paper tear |

Status: `proven` = used in at least one reviewed film; `trial` = not yet reviewed in a film.

## Introduce a person or place

### M01 ม่านเปิด · Foreground reveal
- **GPT:** foreground occluder cutout, background plate, subject cutout (kit, +0).
- **Code:** the occluder leaves frame 1.5–3× faster than the background moves; the subject settles; the name is typeset only after the reveal completes. 3–5 s.
- **Route:** Opuscar Canvas.
- **Breaks when:** the occluder is cut from the same bitmap as the plate, its edge shows a halo, or the name arrives before the subject is visible.
- **Status:** trial. **Log:** planned in Seub treatment, 2026-11-05.

### M02 ดึงโฟกัส · Rack focus
- **GPT:** background plate and subject cutout on separate layers (kit, +0).
- **Code:** blur moves from the subject to the plate (or back) with a slight push in; blur from precomputed copies or a deterministic canvas filter. 2–4 s.
- **Route:** Opuscar Canvas, or a Remotion layer pair.
- **Breaks when:** both layers blur together because the subject was never separated, or blur pumps without a reason in the narration.
- **Status:** trial. **Log:** —

### M03 จิตรกรรมฝาผนังแยกชั้น · Mural layers
- **GPT:** Thai mural-style scene generated as three layers on plain backgrounds: sky and architecture, figures, foreground foliage; then cut out (+3).
- **Code:** a slow lateral camera truck with per-layer parallax; figures stay still or move as whole groups, never bending. 4–8 s.
- **Route:** Opuscar Canvas.
- **Breaks when:** the layers are cut from one flattened mural (holes behind figures), figures are made to walk, or it is captioned as an actual temple mural.
- **Status:** trial. **Log:** —

## Time or era changes

### M04 เฟรมเดิมสองยุค · Same frame, two eras
- **GPT:** two plates of the same composition and camera, one per period, the second generated with the first as reference (+1).
- **Code:** register the plates (scale and offset), then wipe along a physical edge such as a shadow line or waterline, with the year typeset at the edge. 3–5 s.
- **Route:** Opuscar Canvas with a mask.
- **Breaks when:** horizons or buildings do not line up, or the edge cuts through a face.
- **Status:** trial. **Log:** —

### M05 แสงเปลี่ยนวัน · Light pass
- **GPT:** one plate (kit, +0).
- **Code:** colour grade and sky change from day to dusk or night; optional window lights fade in as code-drawn glows. 3–6 s.
- **Route:** Opuscar Canvas, or the app's sky shaders (`skyGolden`, `skySunset`, `skyNightStars`) behind a cutout.
- **Breaks when:** shadows baked into the plate contradict the new light for long. Keep it short or pick a soft-light plate.
- **Status:** trial. **Log:** —

### M06 วันที่พลิก · Date flip
- **GPT:** blank calendar sheet or ledger page, no printed numbers (+1, or kit paper).
- **Code:** pages flip with a hinge scale and shading; dates and the year are typeset per page; the final page holds with a rest. 2–3 s.
- **Route:** Opuscar Canvas.
- **Breaks when:** GPT-baked numbers show through, or the flip rate ignores the number of years spoken.
- **Status:** trial. **Log:** —

## Place, route, journey

### M07 ฉากกลายเป็นแผนที่ · Scene to map
- **GPT:** a plate containing a line feature (river, road, coastline) (kit, +0).
- **Code:** trace that line, fade the plate while the trace continues into Natural Earth geography, then focus the region; labels typeset. 4–6 s.
- **Route:** Opuscar Canvas plus a workspace `geography.json` with its source and licence.
- **Breaks when:** the map implies surveyed boundaries it does not have, or the traced line jumps position at the handover.
- **Status:** trial. **Log:** planned in Seub treatment (water contour into country map), 2026-11-05.

### M08 เส้นทางงอก · Route ride
- **GPT:** side-view vehicle or traveller cutout facing the direction of travel (+1).
- **Code:** a code-drawn route grows; the cutout follows the path tangent, eases at stops and mirrors when the direction reverses; place names appear as reached. 3–6 s.
- **Route:** Opuscar Canvas, or Paper.js for path construction.
- **Breaks when:** the vehicle drives backwards or sideways, the route is drawn ahead of the vehicle without a reason, or a boat crosses land.
- **Status:** trial. **Log:** —

## Document, evidence, record

### M09 สมุดข่อยคลี่ · Samut khoi unfolds
- **GPT:** a closed folded book and one blank panel texture, black or cream paper, no writing (+2, or kit document material).
- **Code:** panels unfold one hinge at a time with fold shading; text and simple drawings are typeset on each panel plane. 3–5 s.
- **Route:** Opuscar Canvas, or a Three.js plane chain (Opuscar `core/three`) when the folds need real perspective.
- **Breaks when:** GPT writes pseudo-Thai script, the text slides off the panel plane, or it is presented as a real manuscript.
- **Status:** trial. **Log:** —

### M10 ใบลานแผ่ · Palm-leaf fan
- **GPT:** one blank palm-leaf strip with its binding cord, cut out (+1).
- **Code:** copies fan out or slide off a stack around the cord with seeded small variation; content is a modern typeset label or decorative lines. 2–4 s.
- **Route:** Opuscar Canvas.
- **Breaks when:** invented ancient inscriptions are shown as authentic text, or all leaves are identical clones in identical positions.
- **Status:** trial. **Log:** —

### M11 แทรกกระดาษ · Paper insert
- **GPT:** blank notebook, letter or form as a cutout (kit, +0).
- **Code:** the paper enters with rotation and a small settle; handwriting-style text draws on the page plane; the camera holds while text completes. 3–5 s.
- **Route:** Opuscar Canvas; keep the page facing the camera, or use a Three.js plane for perspective.
- **Breaks when:** the text floats above the page, the paper keeps wobbling after it lands, or an authored note looks like an archival document.
- **Status:** proven in bounded frame review (not owner approval). **Log:** used in the completed Seub sample; dense-frame evidence in Seub qc/VISUAL-REVIEW.md; originally planned in Seub treatment (field notebook), 2026-11-05.

### M12 พุ่งเข้าไปในรูปถ่าย · Photo push-through
- **GPT:** desk or wall plate plus an empty photo-frame cutout (+1). The photo itself is the next scene's plate, composited by code.
- **Code:** the camera pushes until the photo fills the frame, then the next scene continues live without a cut. 2–3 s.
- **Route:** Opuscar Canvas.
- **Breaks when:** the photo content is baked into the frame image, or the scale jump at the handover is visible.
- **Status:** trial. **Log:** —

## Cause and effect

### M13 สิ่งที่ค่อยๆ ขึ้นมา · Rising element
- **GPT:** plate plus the objects that end up above or below the surface (kit, +0–2).
- **Code:** a deterministic surface line (water, sand, smoke) rises behind a mask; objects ride, sink or are stranded in a consistent order. 4–8 s.
- **Route:** Opuscar Canvas.
- **Breaks when:** objects ignore the surface, the waterline differs between overlapping objects, or the surface jitters randomly per frame.
- **Status:** proven in bounded frame review (not owner approval). **Log:** used in the completed Seub sample; dense-frame evidence in Seub qc/VISUAL-REVIEW.md; originally planned in Seub treatment (Cheow Lan water and boat), 2026-11-05.

### M14 ปฏิกิริยาลูกโซ่ · Baked chain reaction
- **GPT:** three to six prop cutouts (kit, +0–2).
- **Code:** a fixed-step Matter.js simulation is baked to per-frame transforms; each contact lands on a spoken cause, with a sound cue per contact. 3–6 s.
- **Route:** [motion-matterjs](../../motion-matterjs/SKILL.md) baked into Opuscar or Remotion.
- **Breaks when:** the simulation runs live at render time (seeking changes the result), or contacts do not line up with the narration.
- **Status:** trial. **Log:** —

## Number, quantity, scale

### M15 ทำซ้ำจนเต็ม · Count fill
- **GPT:** one unit cutout (person, coin, tree, animal) (+1).
- **Code:** seeded instances fill a grid or shape with slight variation; a typeset unit key ("1 ตัว = 1,000 คน") and the total count up. 3–5 s.
- **Route:** Opuscar Canvas, or PixiJS for very large counts.
- **Breaks when:** a generated crowd image stands in for a specific number, or there is no unit key.
- **Status:** trial. **Log:** —

### M16 เทียบขนาด · Scale ladder
- **GPT:** reference objects of known real size as cutouts (bus, house, person) (+1–3).
- **Code:** objects are drawn to true relative scale; the camera zooms out step by step as each is named; sizes come from the claim record. 4–8 s.
- **Route:** Opuscar Canvas.
- **Breaks when:** relative sizes are eyeballed, or the step pace ignores the narration.
- **Status:** trial. **Log:** —

### M17 ตัวเลขบนฉาก · Stat over scene
- **GPT:** none beyond the plate (kit, +0).
- **Code:** a dimmed plate with a slow push and an app graphic: `scene.fx.graphic` `bigStat`, `lineChart`, `kpis` or `timeline`. 2–4 s.
- **Route:** existing Content Studio templates; the cheapest move.
- **Breaks when:** used for more than one beat in a row, or the card covers the event or the captions.
- **Status:** trial. **Log:** —

## Comparison

### M18 แบ่งจอสองโลก · Split worlds
- **GPT:** two plates with the same layout and camera (+1).
- **Code:** a divider moves with the narration and favours the side being described; labels are typeset per side. 3–5 s. Use the app's `comparison` graphic when the content is a list rather than a place.
- **Route:** Opuscar Canvas, or Content Studio for the list case.
- **Breaks when:** the two plates differ in horizon or scale, so the difference reads as an error.
- **Status:** trial. **Log:** —

## Peak, emotion, weight

### M19 เงาย้อนแสง · Backlit silhouette
- **GPT:** a bright plate and the subject cutout (kit, +0).
- **Code:** the subject darkens to a silhouette with a light bloom and rim; motion slows into a hold. 2–4 s.
- **Route:** Opuscar Canvas.
- **Breaks when:** used to dramatise a death or tragedy the film should treat quietly, or the bloom clips the captions.
- **Status:** trial. **Log:** —

### M20 นิ่ง · Hold
- **GPT:** none.
- **Code:** every layer stops for 1.5–2 s after a key fact; only grain or very small ambient motion remains. A deliberate move, not a missing animation.
- **Route:** any.
- **Breaks when:** used on filler lines, or so often that the film feels stalled.
- **Status:** proven in bounded frame review (not owner approval). **Log:** 2026-11-05 · Seub / Origins · deliberate narrative rests checked in representative final frames; no continuous human viewing claimed.

## Ending

### M21 ถอยกลับสู่โลก · Pull back to the world
- **GPT:** the opening plate (kit, +0).
- **Code:** return to the opening location; the camera retreats so the subject becomes small in the living world; long rest before the end. 4–6 s.
- **Route:** Opuscar Canvas.
- **Breaks when:** the ending plate differs in style from the opening, or text cards replace the world.
- **Status:** trial. **Log:** planned in Seub treatment (return to the living forest), 2026-11-05.

### M22 ของเดิมในสภาพใหม่ · Callback prop
- **GPT:** the signature prop in a changed state, generated with the original as reference (empty notebook now full, seedling now tree) (+1).
- **Code:** the prop returns in the same position and framing as its first appearance, then the change registers with a rest. 2–4 s.
- **Route:** Opuscar Canvas.
- **Breaks when:** the prop's identity drifts (shape, colour, material), or the change is not set up earlier in the film.
- **Status:** trial. **Log:** —

## Transitions

### T01 ตัดรูปทรงเหมือน · Shape match cut
- **GPT:** two plates planned together: a shape at the same frame position and size in both (clock and sun, wheel and moon) (+1).
- **Code:** a short push on the outgoing shape, then a cut or a 4–6 frame blend to the incoming shape. Under 1 s.
- **Breaks when:** the shapes sit at different positions, so the eye jumps.
- **Status:** trial. **Log:** —

### T02 ของผ่านหน้ากล้อง · Foreground wipe
- **GPT:** a foreground cutout large enough to cover the frame (boat, back of a person, tree trunk) (kit, +0–1).
- **Code:** the object crosses the frame and the scene change happens behind its widest point. 0.5–1 s.
- **Breaks when:** the object crosses too fast to read or the cut shows at its edges.
- **Status:** trial. **Log:** —

### T03 หมึกซึม · Noise-mask bleed
- **GPT:** none.
- **Code:** a seeded noise texture thresholded over time reveals the next plate like ink or watercolour soaking through paper. 0.7–1.5 s.
- **Breaks when:** the noise is unseeded and changes between renders, or the bleed is used for every transition.
- **Status:** trial. **Log:** —

### T04 กระดาษฉีก · Paper tear
- **GPT:** one torn-paper edge strip, cut out (+1).
- **Code:** the outgoing frame splits along the strip and the halves separate to reveal the next scene, with paper shading on the edges. 0.6–1 s.
- **Breaks when:** the tear edge repeats visibly on both halves, or it clashes with a non-paper visual style.
- **Status:** trial. **Log:** —

## Log format

After a film's review, update each used card: set `proven` once a reviewed film used it,
and append to **Log** `YYYY-MM-DD · project · worked / failed because … · link to the review note`.
Record failures too; they keep the next film from repeating them.

## Object and mechanism recipes added during Origins production

These cards extend the narrative library to short factual explanations. The review logs distinguish bounded frame evidence from continuous viewing; technical
checks and owner viewing remain separate. Camera stays locked while contact or a mechanism carries the explanation.

### M23 แยกชิ้นให้เห็นโครงสร้าง · Exploded prop
- **GPT:** compatible empty shells, separated internal parts or leaf sheaths as alpha layers (kit).
- **Code:** separate along a clear axis, retain count and identity, then rest. 2–4 s.
- **Breaks when:** a shell retains the extracted parts, an anatomy diagram implies wood rings, or separation has no causal point.
- **Status:** proven in bounded frame review (not owner approval). **Log:** 2026-11-05 · Origins 003/027/029 · coffee V1 failed because beans remained inside the emptied shells; retained V1 and generated corrected V2. See Origins `08_rebuild_20261105/qc/REVIEW.md`.

### M24 ประกอบคำ · Word construction
- **GPT:** only the meaningful object or blank physical tile (kit).
- **Code:** typeset verified word components and relations; short stagger followed by a readable hold. 2–4 s.
- **Breaks when:** visual resemblance is presented as etymology, generator lettering becomes a source, or the stagger delays reading.
- **Status:** proven in bounded frame review (not owner approval). **Log:** 2026-11-05 · Origins 022–025 · authored word components, original pictograms and retained primary-source claim records; review in `09_next10_20261105/qc/REVIEW.md`.

### M25 เกิดเป็นวัสดุ/โครงสร้าง · Formation reveal
- **GPT:** clean final specimen and any distinct source materials (kit).
- **Code:** directed fibres, image sections or a surface callout resolve into the specimen. 2–4 s; explain the diagram's scale and limits in the claims/treatment.
- **Breaks when:** a rectangular image grid purports to count biological units, a film thickness is drawn as calibrated without evidence, or weak random seeds create artificial stripes.
- **Status:** proven in bounded frame review (not owner approval). **Log:** 2026-11-05 · Origins 018/028/031 · paper fibre RNG correlations corrected before final encode; pineapple image sections are explicitly illustrative, not fruitlet counts.

### M26 เลื่อนแล้วขบ · Controlled fastener
- **GPT:** slider and familiar finished product (kit).
- **Code:** alternating fixed-pitch teeth follow the same Y-shaped channel as the slider; close and reverse without a discontinuity. 3–5 s.
- **Breaks when:** teeth remain separated at closure, pitch changes, the slider detaches from the junction, or a drawn schematic is claimed as manufacturing simulation.
- **Status:** proven in bounded frame review (not owner approval). **Log:** 2026-11-05 · Origins 029 · excessive closed-tooth spacing failed proof; corrected before export. Moving proof `09_next10_20261105/qc/zipper-moving-proof.mp4` plus dense frames.

### M27 กดแล้วลอก · Pinned peel
- **GPT:** compatible hook and loop textile surfaces (kit).
- **Code:** keep one edge and the lower support fixed; deform the upper strip continuously along a smooth peel curve. 3–5 s.
- **Breaks when:** separately rotated strips expose seams, both parts float, or the pinned edge drifts.
- **Status:** proven in bounded frame review (not owner approval). **Log:** 2026-11-05 · Origins 030 · independent slice rotation failed with visible seams; tangent-sheared overlapping strips replaced it. Dense frames in `09_next10_20261105/qc/peel-proof`.

### M28 เติบโตจากจุดยึด · Anchored growth
- **GPT:** actual plant shoot, pod or section (kit).
- **Code:** grow a path from a visible anatomical attachment toward its target; only reveal the later state when the path reaches it. Preserve the grown state at the next beat. 3–5 s.
- **Breaks when:** roots, stems and pegs are confused, the shoot floats above the soil, or the next beat resets growth.
- **Status:** proven in bounded frame review (not owner approval). **Log:** 2026-11-05 · Origins 026/027 · ground support and peg continuity corrected in proof; condensed illustrative growth, not calibrated botany time-lapse.

### M29 วางเทียบชิ้นจริง · Specimen comparison
- **GPT:** two or three matched cutouts, shared light/texture (kit).
- **Code:** staged lateral reveal on a coherent baseline, optional divider or restrained relation path; hold for the factual comparison. 2–4 s.
- **Breaks when:** props drift without support, unknown scale implies measured size, or every sentence becomes a comparison card.
- **Status:** proven in bounded frame review (not owner approval). **Log:** 2026-11-05 · Origins material and word series · representative-frame staging review; no scale calibration claimed.

### M30 น้ำและการรบกวน · Schematic water
- **GPT:** harbour, boat and optional seabed/forest material (kit).
- **Code:** coherent waterline, restrained hull motion and a labelled disturbance/wave diagram. Avoid arbitrary spray or unverified amplitudes. 3–6 s.
- **Breaks when:** a boat floats above its waterline, a photographic surf wave stands in for tsunami mechanics, or diagram timing is presented as a forecast.
- **Status:** proven in bounded frame review (not owner approval). **Log:** 2026-11-05 · Seub / Origins 025 · water and habitat story / word-origin diagram. Approximate contours are not measured inundation or warning guidance.

### M31 ตั้งชิ้นงานให้เห็น · Specimen reveal
- **GPT:** one clean specimen or prop, with actual alpha and a consistent view/light (kit).
- **Code:** a short translation/rotation settles onto a fixed baseline or deliberate specimen framing. No repeated slow zoom. 0.6–1 s entry, then a purposeful rest.
- **Breaks when:** the object stays unsupported, every beat uses this instead of explaining a change, or a flat bitmap is bent to fake articulation.
- **Status:** proven in bounded frame review (not owner approval). **Log:** 2026-11-05 · Origins 001–031 · restrained object entry and rest, paired with topic-specific explanatory events. M13 remains the water/surface recipe, not a generic prop reveal.

### M32 เชื่อมพื้นที่แบบแผนผัง · Schematic map relation
- **GPT:** optional region/ingredient cutout (kit).
- **Code:** draw a relationship between labelled approximate regions using verified map geometry. A path may explain diffusion without pretending to be a traced voyage. 2–4 s.
- **Breaks when:** country fill implies an unsupported native range, a route is treated as a first-arrival record, or vehicle direction pretends to meet the stricter M08 path-tangent recipe.
- **Status:** proven in bounded frame review (not owner approval). **Log:** 2026-11-05 · Origins origins series · neutral country fills and approximate origin markers after review; exact trade routes and surveyed sanctuary borders are not claimed.

### M33 หมุนตรงจุดสัมผัส · Rolling contact
- **GPT:** whole-object specimen, enlarged tip and reservoir material (kit).
- **Code:** fix the contact plane; couple angular displacement to surface travel with θ=d/R. Leave the trace behind the actual contact point; a camera attached to the tip can let the paper move instead. 3–5 s.
- **Breaks when:** the ball spins independently of translation, the trace grows by a different distance, or the sphere penetrates/floats over the paper.
- **Status:** proven in bounded frame review (not owner approval). **Log:** 2026-11-05 · Origins 039 · corrected an initial travel/trace scale mismatch; moving proof and dense contact frames retained in `11_next10_20261105/qc/`.

### M34 ช่องว่างมีหน้าที่ · Layer/gap explanation
- **GPT:** complete specimen, inner vessel and truly empty outer shell halves (kit).
- **Code:** separate the layers, then reveal a qualitative section with side and bottom clearance. Directed traces explain transfer without inventing a measured rate or claiming perfect insulation. 3–5 s.
- **Breaks when:** both bottoms accidentally touch, liquid overlaps a wall, or reducing transfer is represented as eliminating every possible heat path.
- **Status:** proven in bounded frame review (not owner approval). **Log:** 2026-11-05 · Origins 040 · corrected the initial shared-bottom geometry; retained a visible bottom gap and bounded the heat claim.

### M35 สปริงกับตัวรับ · Spring and catch
- **GPT:** closed/open reference specimens and an isolated empty catch (kit).
- **Code:** retain the actual pivot and constant leg length; drive opening/closure deterministically, and draw the catch as a foreground occluder when the tip seats. 3–5 s.
- **Breaks when:** the leg disconnects from the coil, changes length, crosses the cover, or a whole photographed pin is stretched to fake the mechanism.
- **Status:** proven in bounded frame review (not owner approval). **Log:** 2026-11-05 · Origins 041 · coil attachment and clasp occlusion corrected; moving latch proof plus dense frames retained. Qualitative schematic, not a stress/force simulation.

### M36 ยกให้ผ่าน แล้วเรียง · Ordered process example
- **GPT:** optional context specimen only; example counters/numerals stay code-native.
- **Code:** lift the crossing counter completely clear, slide neighbours along their baseline, then return it to the new position. Keep identities and count fixed. 2–4 s.
- **Breaks when:** simultaneous trajectories hide labels/intersect, counters change identity, or a simple ordering illustration is claimed as a specific historical algorithm or physics simulation.
- **Status:** proven in bounded frame review (not owner approval). **Log:** 2026-11-05 · Origins 034 · increased clearance and sequenced lift/move/lower after tracing the initial crossing paths; representative moving frames retained separately.

### M37 ฟันขบ หมุนสวน · Meshed external gears
- **GPT:** orthographic blank metal texture and context specimens; never trust generated tooth counts for contact geometry.
- **Code:** construct matching involute profiles with shared module/pressure angle. Keep centre distance at the sum of pitch radii and axes fixed. Couple rotations with θ₂ = phase − (N₁/N₂)θ₁; phase a tooth against a gap. Put stationary bearings in front, and preserve rotation phase across adjacent narration beats. 4–6 s explanatory intervals.
- **Breaks when:** incompatible tooth pitch, incorrect initial phase, arbitrary independent spin, moving axles, conflicting direction arrows, or implying all internal/planetary arrangements rotate in opposite directions.
- **Status:** proven in bounded geometry/frame review (not owner approval). **Log:** 2026-11-05 · Origins 044 · 20/30 teeth, 20° pressure angle, module 16 px, 400 px centre distance; 72 mesh phases at 8x raster silhouette resolution and a 5-second moving proof with dense contact frames retained in `12_next3_20261105/qc/`. This is kinematics, not load/force/stress simulation or manufacturing validation.

### Additional bounded move review · 2026-11-05
- **M24 / M29 / M20 / M31:** Origins 042, a fruit label transfers into a colour role; the swatch exists before its label. English etymology only. Representative frames and the delivered moving film are in `12_next3_20261105/`.
- **M28 / M29 / M31 / M20:** Origins 043, reached stolon endpoint precedes terminal tuber swelling; the macro bud remains attached while a separate shoot/leaf layer grows. Corrected a note overlapping the tuber. Final cut sampling exposed a leaf appearing early because the asset helper overwrote inherited alpha; changed alpha assignment to multiplication and delayed leaf reveal until the shoot endpoint (also tuber swelling until the stolon endpoint). Selected five-second growth-v2 and shoot proofs/dense frames retained; not measured time-lapse or human playback approval.
- **M15 / M24 / M29 / M20:** Origins 044 exact tooth labels and 3:2 example support M37, with a final static context rest. The generated watch is illustrative, not an authenticated historical specimen.
