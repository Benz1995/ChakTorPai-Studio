# Pose production and assembly

## Prompt: one uniform sheet

Replace the subject and style with the actual brief. Use an inspected style/identity
reference when one is available. Choose enough pixels per cell for the final use.

```text
Create one animation sprite sheet: exactly 3 columns × 3 rows, 9 equal cells,
read left to right then top to bottom. Same camera, scale, framing, lighting,
palette and subject identity in every cell. No cell borders, captions or numbers.

Subject: [subject and fixed design]. Art direction: [approved style frame].
Single action: [start state → action/contact → settle].
Pose list, one cell per pose: [explicit ordered list of 9 related poses].
Keep [anchor point] at the same local coordinates in every cell. Keep the full
silhouette and props within each cell with generous clearance. Change only the
parts required by the action. No duplicated props, changing face, camera motion,
background drift or subject spilling across cells.
Background: [actual alpha requested through the image tool, or a consistent plate].
If looping, make the last pose lead naturally into the first; do not duplicate
the first drawing as the last unless an extra hold is intentional.
```

For separate frames, keep the same invariants and reference, and request the specific
next pose by its action phase. Save each chosen frame with a stable ID. A sheet with
uneven cells, baked grid lines or tiny subjects needs correction; auto-cropping each
silhouette independently introduces positional and scale jitter.

## Assembly manifest

Paths resolve relative to the manifest. A sheet must have an exact uniform grid with
no gutters or outer margins; trim intentional layout margins explicitly before assembly.
Use a new output directory for each revision. `duration_ms` values must be positive
multiples of 10. `fps` is an integer between 1 and 60. If any pose would receive zero
video frames at that FPS, assembly refuses instead of silently dropping the pose.
The short-asset helper accepts 2–256 source poses, at most 64 million total decoded
source pixels and a cycle up to 60 seconds. Longer videos should compose multiple
shots using the existing timeline, rather than expand an entire film into this helper.

```json
{
  "sheet": {"file": "assets/steam-sheet.png", "columns": 3, "rows": 3, "count": 9},
  "duration_ms": 200,
  "mode": "loop",
  "fps": 30,
  "background": "#101820",
  "provenance": {"route": "imagegen", "prompt_file": "prompts/steam.txt"}
}
```

Alternatively supply ordered files, with optional per-pose durations:

```json
{
  "frames": [
    {"file": "assets/anticipation.png", "duration_ms": 200},
    {"file": "assets/action.png", "duration_ms": 100},
    {"file": "assets/settle.png", "duration_ms": 300}
  ],
  "duration_ms": 150,
  "mode": "once",
  "fps": 30,
  "background": "#101820"
}
```

`sheet` and `frames` are mutually exclusive. Frame dimensions must match. For a sheet,
`durations_ms: [100, 100, 200, ...]` optionally replaces the uniform duration, one value
per selected cell. Sheet order is row-major; `count` can omit unused trailing cells.
`mode: "pingpong"` plays `0, 1, …, n-1, n-2, …, 1`, with no doubled endpoints.

Output files:

- `frames/frame-0000.png`, …: normalized, source-resolution RGBA poses.
- `contact-sheet.png`: labeled for inspection, composited on the chosen matte.
- `animation.gif`: one action/cycle, looping only in `loop`/`pingpong` modes.
- `preview.mp4`: one action/cycle, H.264 at `fps`, no audio, composited on `background`.
- `receipt.json`: inputs/hashes, source frame count, playback order, GIF and video
  timing, crop boxes, source provenance as supplied, commands and technical checks.

GIF palette conversion can reduce color/alpha fidelity; PNGs remain the editable
master. GIF has binary transparency. MP4 pads an odd width/height by one matte pixel
for yuv420p compatibility; it does not stretch the image. Generated poses are assembled
as holds, without inventing in-between content.

The helper deliberately does not generate art, call an API, remove a background,
run optical flow, attach a voice or publish. Reuse the existing project workflows
for those operations. Test the helper with:

```powershell
python -B -m unittest discover -s .agents/skills/frame-sequence-animation/scripts -p "test_*.py"
```
