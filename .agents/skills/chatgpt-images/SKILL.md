---
name: chatgpt-images
description: Generate scene images, characters, product shots, cover art and native animated GIFs in ChatGPT on the web (chatgpt.com, the owner's signed-in account) through a browser, then download, file and attach them to Content Studio scenes. Use whenever Claude needs a GPT image or GPT GIF for BigO (เจนภาพ, สร้างรูป, ภาพประกอบฉาก, ตัวละคร, ภาพสินค้า, ทำ GIF, ภาพเคลื่อนไหว) — animestory, affiliate, mascot, gpt-motion-story or frame-sequence assets. Not for the OpenAI API provider or local SDXL unless the owner asks.
---

# ChatGPT web images

The owner directs everything through Claude, so Claude generates the images itself in
ChatGPT on the web with the owner's own account (owner, 26 Oct 2026). Do not ask the owner
to paste prompts. The app's OpenAI API provider (`generate_images` with `OPENAI_API_KEY`)
and local SDXL are optional routes only when the owner asks; SDXL cannot draw some styles
(stick figures). Codex agents use their `imagegen` skill instead of this one.

## 1. Pick the browser

| Order | Browser | Notes |
| --- | --- | --- |
| 1 | Built-in browser pane (`mcp__Claude_Browser__*`) | Usually signed out of ChatGPT. Ask the owner to sign in in the pane, or to import cookies for `chatgpt.com` only from the pane's ⋮ menu. It has no file chooser for uploads. |
| 2 | Claude in Chrome (`mcp__claude-in-chrome__*`) | The owner's real Chrome; was signed in and downloading fine on 4 Nov 2026. Offer it when the pane is signed out, and switch only when the owner agrees. Supports `file_upload` / `upload_image` for references. |
| 3 | Playwright MCP | Fallback per [playwright-mcp](../playwright-mcp/SKILL.md); `browser_file_upload` accepts only files under `B:\ChatGPT\BigO`. |

Never type the owner's password, and never switch accounts or buy a plan. If ChatGPT says
the image limit is reached, stop and tell the owner when it resets; do not move to a paid
provider silently.

## 2. Get the prompts

- `get_image_prompts` (= `GET /api/contents/:id/chatgpt-prompts`) returns the template's
  prompt per scene, the aspect, the art style, `mode` (`shared` = one image for all scenes)
  and `cutout` (the template wants transparent subjects).
- Add what the prompt lacks: the aspect ratio in words ("vertical 9:16"), palette and
  light, and "no text, no captions, no logos" — Thai text is added by the app in post;
  AI-drawn Thai, flags and maps are wrong.
- For a product, upload the shop photo as a reference and ask for a new scene that keeps
  the product's exact shape, colour, cap/lid and label spelling
  ([shopee-affiliate](../shopee-affiliate/SKILL.md) rule 2).

## 3. Keep characters consistent

Generate every image of one character or series in the **same conversation**, starting from
its approved character sheet, and record the conversation URL in the project notes. Known
conversations: KinJi mascot and girlfriend —
https://chatgpt.com/c/6aecc42c-d8d0-83ec-b611-771e92336ada. For a new character, make a
character sheet plus one main pose first and get the owner's approval before scenes.

## 4. Download and file

- Saving generated files needs no confirmation (owner, 31 Oct 2026), but every file must be
  moved into the BigO project folder — never left in Downloads or temp.
- The built-in pane saves to `C:\Users\usEr\Downloads\<uuid>.tmp`: copy the newest `.tmp`,
  detect the real type from its first bytes (`89 50 4E 47` PNG, `RIFF…WEBP`, `FF D8` JPEG)
  and give it that extension. Chrome's download button saves a named file to Downloads.
- Destination: the content's workspace `assets/` folder (gpt-motion-story), or
  `images/<project>/<batch>/` for affiliate/mascot work. Name files by role
  (`blanket-gag.png`, `hook.png`); keep rejected attempts with a `-v1` suffix.
- Measure the file: pixel size and aspect, and alpha when a cutout is needed. A chat
  download may be opaque even when transparency was requested; then follow the cutout
  steps in [gpt-motion-story](../gpt-motion-story/SKILL.md) (`upload_file` with
  `cutout: true`, needs `npm run images` in `content-studio`).

## 5. Attach and check

1. `set_scene_image` (or `upload_file` then set) for each scene.
2. `preview_frames` — framing under the template's cards and captions, character identity,
   product match against its reference, no baked text.
3. Record each image: file, prompt, conversation URL, date, size, alpha, status
   (selected / rejected). gpt-motion-story projects use `assets/ASSETS.md`.

## 6. Animated GIF in the web chat

GPT's image generator can output a native animated GIF. The owner wants this made in the
normal ChatGPT web chat too, not only through the API (owner, 7 Nov 2026). Default route:
the web chat with the owner's account, as for stills. The API route
(`output_format: "gif"`, `frame_count`, `frame_duration_ms`; see
[gpt-gif-workflow](../../../content-studio/docs/gpt-gif-workflow.md)) is only for when the
owner asks and `OPENAI_API_KEY` is set (it was empty on 7 Nov 2026).

1. Work in the series' own conversation, after its approved style or character image, so
   the GIF keeps that identity. A GIF is a short loop or a small action, not a whole scene
   with acting.
2. Ask the image generator itself for the GIF, with the numbers in words:
   ```text
   Create a seamless looping animated GIF with your image generator (native animated GIF
   output, not code), 12 frames, 120 ms per frame, vertical 9:16, in exactly the style
   and composition of the approved image above. Locked camera. Only this moves: [ash
   drifts down, cloud glow pulses, hair/scarf flutters, ears twitch]. Characters keep
   identical design and position. The loop returns to its start without a jump.
   No text, no letters.
   ```
   Start at 9–12 frames and stay ≤16 until a larger count is proven on the account.
3. If ChatGPT writes Python to stitch or warp frames instead, say once: "Please don't use
   code — use the image generator's native animated GIF output." Record what it actually
   did (native GIF, code-built GIF, or refusal) with its wording. A code-built GIF that
   only pans or warps one still is not a native GIF; keep it only as a labelled fallback.
4. Download and verify: the first bytes must be `47 49 46 38` (`GIF8`). Measure frame
   count, per-frame durations, total length and pixel size with Pillow, and look at the
   frames for identity drift, flicker, popping and the loop seam. File it as
   `assets/<shot>/gif/<name>.gif` in the content workspace and record prompt, conversation
   URL, route (web native / web code / API), date, frames, ms and size.
5. Attach with `set_scene_image` (or the scene's **อัปโหลดรูป / GIF** control). The scene
   loops the GIF for the scene length; Thai text and captions stay in the app's layers.
6. First web test (Day0 series, 7 Nov 2026): ChatGPT web made a native GIF on the first
   try, without code — 12 frames × 120 ms, looping, 816 KB — but only **356×345**, near
   square, although 9:16 was asked. Motion was subtle (cloud glow, dog ears, small body
   moves) with the identity kept. Treat a web GIF as a small loop or insert, not a 1080×1920
   full-frame shot; for full frame use layers (below). Asking for a "layer on a transparent
   background" also produced real RGBA PNGs at the full 941×1672 canvas, but the characters
   were redrawn look-alikes in new poses, so they stack into a new composition, not back
   into the original image.
7. If the web chat cannot make a native GIF, tell the owner what ChatGPT said and offer
   the alternatives: separate layers (background, atmosphere, each character, animals,
   props — the owner's preferred route for full-frame shots) or key poses assembled with
   [frame-sequence-animation](../frame-sequence-animation/SKILL.md), or the API with a key.
