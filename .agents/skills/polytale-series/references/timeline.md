# timeline.json reference

One file per episode, in the episode folder. Paths are relative to that folder. Every script
loads it through `scripts/tl.py`, which resolves relative timing — run
`python scripts/tl.py <ep>` to print the resolved shot times. The full working example is
`workspaces/video/PolyTale/series/day0/ep01/timeline.json` (ep00 shows the older absolute form,
which still works).

## Timing model (use it — it keeps sync when a line is re-voiced)

- Shots are listed in order with `len` (minimum seconds); start/end are computed.
- A shot with `"vo": "audio/vo-03.mp3"` plays that line at shot start + `vo_at` (0.2) and grows
  to fit it (+ `vo_pad` 0.4). Its `th` / `en` become the subtitle automatically.
- Other items take `"shot": "<id>"` and their `at` / `start` / `end` / `t0` / `t1` count from
  that shot's start. A value may also be `{"shot": "<id>", "at": 1.5}` (any shot), or
  `"end": "shot_end"`. Audio `dur` may be `"to_shot_end"`; `"end_at": {"shot", "at"}` sets the
  duration so audio stops exactly at that moment (e.g. music cut on the flash).
- `length` defaults to the end of the last shot.

## Top level

| Key | Meaning |
| --- | --- |
| `id` | output name `render/<id>.mp4` |
| `look` | series grade for every frame: `sat`, `contrast`, `tint` [r,g,b], `tint_a`, `grain` (0.03–0.07) |
| `shots` | list, see below |
| `vo` | extra voice lines not owned by a shot: `{file, shot, at, gain}` |
| `lines` | character lines made directly with ElevenLabs by `audio_gen.py`: `{file, text, voice, pitch}` (child = adult female voice + pitch 1.15–1.2) |
| `subs` | extra subtitles `{shot, start, end, th, en}` (Thai `\N` = line break) |
| `sfx` | real sound effects: `{id, prompt, gen_dur, influence, shot, at, dur, gain, fade_in, fade_out}`; `file` instead of `prompt` to place an existing file (e.g. a music cue) |
| `music` | score under the voice, ducked automatically: `{prompt, length, file, at, dur or end_at, gain 0.25–0.35, fade_in, fade_out}` |
| `music_extra` | more cues for `audio_gen.py` to make: `{prompt, length, file}` (place them with `sfx` entries) |
| `sfx_bed` | procedural bed from `sound.py` (`audio/sfx-bed.wav`); `null` when real SFX cover everything |
| `countdown` | timer top-right: list of segments `{t0, t1, v0, v1 (seconds shown), hold}`; values interpolate, so time can be compressed |
| `stamp` | top-left label, e.g. `วันที่ 0 · 07:42` |
| `alert` | phone alert card that slides down: `{title, body}` |
| `cards` | centred text cards `{text, y}` |
| `lessons` | teaching card(s) `{shot, start, end, title ("ถ้าเจอจริง"), y, items: [{text, src (sources for this step), at (s after start), h (px)}], source (scope line)}` — dims the frame; items appear when spoken |
| `choice` | viewer-choice end card: `{question, a, b, cta}` (dims the frame) |
| `cut_sfx` | one transition sound on every cut: `{prompt, file, gain 0.3, lead 0.35 (s before the cut), skip: [shot ids]}`; per shot `cut_gain` or `"cut_sfx": false` |
| `follow` | animated follow button on the end card, never with the channel name: `{shot, start, end, tap (s after start), y, label "+ ติดตาม", done "ติดตามแล้ว"}`; pair it with a `tap` sfx at the tap time |
| `title` | episode title card `{badge, title, note}` (dims the frame) |

## Shots

Common: `id`, `len` (or `start`/`end`), `type`, `vo`/`th`/`en`/`vo_at`/`vo_pad`,
`transition: "whip"` (+ `whip_dir` 1 or -1) for a whip-pan entrance, `dip: false` to skip the
2-frame dark dip at cuts (use inside montages), `fg` foreground layer (+ `fg_drift`, `fg_blur`)
that moves faster than everything else for depth. Images are centre-cropped to 1080×1920
(`fit: "cover"`) or stretched (`fit: "stretch"` for ~9:16 layers).

### push — one full-frame image
| Field | Default | Meaning |
| --- | --- | --- |
| `image` | — | the picture |
| `zoom` | `[1.04, 1.12]` | start → end scale; reverse it (`[1.18, 1.06]`) for a pull-out |
| `anchor` | `[0.5, 0.5]` | zoom centre as fractions (put it on the eyes); several shots on one image with different anchors = a montage of crops |
| `pan` | 0 | horizontal drift in px |
| `dof`, `dof_time` | none, 0.6 | rack focus: blur radius start → end over that share of the shot (`[8, 0]` = pull into focus, `[6, 14]` = drift out behind a card) |
| `dim` | 0 | darken 0–1 (behind cards) |
| `buzz` | false | phone vibration |
| `pulse`, `pulse_hz`, `pulse_alpha` | none, 2.0, 35 | flashing colour wash (alarm red `[255,20,20]`) |
| `end_shake` | 0 | shake building over the last 1.2 s |
| `ash` | false | falling ash |

### run — characters running/walking toward the camera
`plate`, `poses` (2–4 transparent layers in order), `steps_per_sec` 3.4, `bob` 22,
`scale` `[0.84, 0.94]`, `shake` 7, `speed_lines` 0.8 (0 = off).

### reveal / layers — characters in a place, optional big event
| Field | Default | Meaning |
| --- | --- | --- |
| `bg` | — | background |
| `chars` | — | transparent character layers, back to front |
| `blink` | `{}` | `{"<index>": "eyes-closed layer"}`: blinks every ~3.7 s |
| `swaps` | `[]` | `[{"at": 2.0, "chars": [...]}]`: replace the layers at that moment (turn heads, react) |
| `tremble` | `[]` | indexes that shiver |
| `cloud`, `cloud_base`, `cloud_width` | none, `[700,560]`, 600 | prop on the skyline that rises after the flash; keep it away from faces |
| `flash_at` | none | white flash + heavy shake + regrade + prop rises + ash |
| `pre_grade`, `post_grade`, `char_pre_grade` | see shots.py | colour before/after the flash |
| `bg_push`, `char_push` | 0.04, 0.08 | parallax push |

## Platform safe zones (1080×1920)

Keep faces, subtitles and cards out of: the top 220 px (app header), the bottom 380 px
(caption and buttons) and the right 140 px between y 900 and 1540 (like/comment buttons).
`subs.py` already places Thai subtitles to end at y≈1440 and English at y≈1510 within
x 150–930; `qc.py` tints these zones red on `review/strip.png`.
