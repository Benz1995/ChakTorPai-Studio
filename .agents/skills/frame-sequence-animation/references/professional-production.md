# From a loop to a directed video shot

Use for professional-quality production or a substantial quality rebuild. These are
BigO production recommendations; the vendor references below establish format/tool
behavior, not a certification that a film is professionally finished.

## Preserve the right master

Keep original full-color RGBA PNG frames and a separate exposure/shot record as the
editable master. Make GIFs for quick loop review or an actual GIF destination. GIF
uses indexed color and a transparent color index rather than a continuous alpha
channel; its delay unit is 1/100 second. A GIF-only source cannot recover colors,
edge alpha or missing drawings just by being decoded into PNGs. See the
[GIF89a specification](https://www.w3.org/Graphics/GIF/spec-gif89a.txt) and
[Remotion quality guide](https://www.remotion.dev/docs/quality).

For an existing GIF, preserve its real timing and disposal/compositing behavior when
decoding. Use it as an economical small loop when it looks sufficient at delivery
size. For a large hero character or intricate contact shot, return to full-resolution
drawings/parts or the appropriate rig/video route instead of enlarging a weak loop.

If a finishing editor needs transparent video, consider a tested ProRes 4444 handoff
or PNG sequence, alongside a normal MP4 preview. Verify alpha in that editor and
the actual local encoder; a .mov extension alone proves nothing, and browser/App
playback support is separate from an encoder's ability to produce the file.
[Remotion transparent export](https://www.remotion.dev/docs/transparent-videos) and
[ProRes output](https://www.remotion.dev/docs/prores) document those render options.
Do not change BigO's normal H.264 delivery format merely to add a handoff master.

## Budget pixels before asking for a sheet

Plan the largest visible subject height after camera scale, not just the export size:

```text
required native subject height >= display height × largest camera scale
required cell height >= required native subject height / subject occupancy
sheet height >= cell height × number of rows
```

Use the actual returned file dimensions. A requested 2048px image is not evidence
that the tool returned it. A 4×4 sheet distributes its pixels over sixteen drawings.
If cells are too small, generate fewer poses per sheet or separate frames with a
shared style/identity reference. Generate only poses/in-betweens the shot needs;
compare actual attempts, usable pixels and measured work before claiming savings.
Upscaling may be an intentional style choice, but it does not create native detail.

Audit source frames before a costly batch or render:

```powershell
python -B .agents/skills/frame-sequence-animation/scripts/audit.py --manifest <shot.json> --display-height 650 --shot-seconds 16 --receipt <assembly/receipt.json> --out <new-audit.json>
```

Omit `--receipt` before assembly. The read-only helper reports native subject bounds,
display enlargement, exact duplicate rasters, border alpha, declared timing and cycle
budget. A provided receipt must match the manifest and current source hashes and
record completed assembly. The bounds depend on its alpha threshold; they are not
anatomical segmentation, a matte certificate or an automatic quality score.

## Direct the action and exposure

Break a shot into readable preparation, action/contact, response and outcome. Record
the key drawings, their exposure in final frames, contact/support anchors, occlusion
and any necessary in-betweens. Leave room for deliberate rests; do not continuously
move every layer just to register pixel changes. For dance, plan distinct phrases
and the ending against the music grid, rather than repeating one exercise throughout.

BigO currently uses 30 FPS. At that output rate, 10 drawings/second can hold for three
frames, while 15 can hold for two. Eight evenly timed drawings/second require a mix
of three/four-frame holds. A separate 24 FPS production could hold eight drawings for
three frames or twelve drawings for two, but do not change the app's global FPS to
force that cadence. Check the actual delivery contract first. These are arithmetic
cadences, not prescriptions for appealing motion or reasons to generate every frame.

Animate transforms and drawings separately: a camera may move smoothly at output FPS
while the drawing intentionally holds. Use frame-driven `Img` selection from exposure
data or `AnimatedImage` for a suitable existing loop. Verify seeking, offsets and
play-once/hold behavior. [AnimatedImage](https://www.remotion.dev/docs/animatedimage)
documents timeline synchronization and looping controls; BigO's current SceneImage
wrapper deliberately loops GIFs, so one-shot action needs another explicit path.

Optical flow is an optional finishing experiment after source poses work. FFmpeg's
[minterpolate](https://ffmpeg.org/ffmpeg-filters.html#minterpolate) offers frame
duplication, blending and motion-compensated interpolation. Our production judgment:
none of those modes is evidence of corrected anatomy, grip or occlusion. Inspect new
frames around hands, hair, crossing silhouettes and cuts; reject warped results.

## Composite as a scene

- Split background, subject, foreground occluders, props and effects only where they
  need independent motion. Keep a coherent lens, perspective, light and scale.
- Maintain world contact anchors, not an automatic per-frame silhouette crop. For
  supported poses lock the appropriate foot/prop; explicitly release it for a hop.
  The lowest opaque pixel may be hair or a prop, so a bbox alone cannot identify feet.
- Test cutouts on light, dark and the actual production plate. Distinguish unwanted
  matte haze from useful fine edges; a universal alpha threshold can destroy hair.
- Track straight versus premultiplied alpha through the chosen compositor. PNG
  commonly stores straight alpha; misinterpretation can alter edges. Consult
  [Blender's image alpha settings](https://docs.blender.org/manual/en/latest/editors/image/image_settings.html)
  when using that route. Do not assume all renderers use the same color/alpha math.
- Set labels/captions in the compositor, preserve the existing Thai text contracts,
  and keep effects subordinate to the visible event. A new angle must have sufficient
  source detail; enlarging the same tiny drawing is not a new close-up asset.

## Finish through one reviewed path

For app-owned work, prefer shared Remotion preview/export components and persisted
API/MCP content. A custom baked render is allowed as an asset, but importing it into
a template with extra titles, grading or framing does not make that preview equivalent
to the original MP4. Identify the authoritative master and review the actual path.
Do not store shot-planning annotations as invented Scene API fields.

Keep the existing `earshot`/audio checks, authored script and subtitle contracts.
Build a short moving proof of the hardest action at intended size, plus dense contact
and boundary frames. Review the edited sequence for identity drift, repetitive
phrases, contact, pacing, readable labels and sync. If only frames were inspected,
state that limitation. Check final streams, dimensions, FPS, duration, decode, audio
levels and representative encoded frames; these do not establish editorial approval.

Separate: editable frames/exposure data, optional transparent handoff, approved-looking
review copy, encoded delivery and actual publication state. Retain source hashes and
failed/superseded takes. Do not repeatedly recompress GIF→MP4→MP4 or call a sharper
export a creative rebuild. Style approval and motion review remain human/agent
judgments with stated limits; no diagnostic tool proves the complete result.

Research checked 6 Nov 2026. Blender and FFmpeg content was retrieved directly from
the primary sites/source after browser retrieval failed. Toon Boom search results
were not used as read evidence because the pages could not be retrieved.
