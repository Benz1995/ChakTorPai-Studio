---
name: shopee-affiliate
description: Make KinJi Shopee Video affiliate clips (คลิปปักตะกร้า, คลิปขายของ, Shopee Affiliate, 11.11/12.12) in Content Studio — pick products from the affiliate dashboard, write a comedy hook, cast the KinJi mascot / อิงเอย / the couple, regenerate the real product image from the shop photo, render one clip per product, then hand the owner a posting table with ≤150-character captions. Use for any Shopee affiliate clip, batch, caption or posting table; campaign-matrix is for an 18-variant ad matrix.
---

# Shopee affiliate clips (KinJi)

The owner's Shopee Video account is **KinJi** (@wirunkemmonta). Clips are produced in
Content Studio project **ขายของ: Shopee Affiliate** (`T6hY-sypjr`: template `affiliate`,
9:16, voice `FfrJDiyJZK` = the owner's own ElevenLabs voice). The owner posts by hand;
this skill ends at a posting table, never at an automated post.

## Owner rules (hard gates — check every clip)

1. **One clip = one product, and the real product is visible** (owner, 5 Nov 2026).
2. **No seller or reviewer media in the clip.** Save the shop's product photo only as a
   reference in the batch's `ref/` folder, then regenerate a new image (see
   [chatgpt-images](../chatgpt-images/SKILL.md)) that matches the product **exactly** —
   shape, colour, cap/lid, label and print spelling ("ห้ามเพี้ยน"). Compare against the
   reference before use; the first lip balm came out as a stick instead of a squeeze tube
   and had to be redone. Use the owner's own phone footage whenever they supply it — their
   real-use clips outperformed AI-image posts.
3. **Never state a price, discount or "% off"** — in narration, on screen or in captions.
   Prices change constantly. Say "ดูราคาในตะกร้า" / "กดตะกร้าเลย" instead.
4. **Fun first & Native Thai Craft.** Scripts must follow `.agents/skills/thai-craft/SKILL.md`
   (natural Thai humor, dynamic flow, zero robotic calques, 3-second spoken test). A presenter is optional; the clip must be genuinely entertaining: a
   relatable comedy hook (e.g. "กรุงเทพฯ 23 องศา หนาวจะตาย") and a gag that the product
   solves. A spec list is not a concept.
5. **No fake testimonial.** Never script "ฉันซื้อมาใช้แล้ว" for an AI character. Product
   facts come from the listing only; keep listing claims separate from verified facts and
   never invent specs, models or sizes.
6. **No on-screen AI badge, no "AI" in the caption** (owner, 6 Nov 2026: captions only
   allow 150 characters). Set the content `handle` to `"none"` — an empty handle inherits
   "@mychannel" from the main project.

## Characters

Alternate between the mascot, his girlfriend and the couple, picking whoever fits the gag
(lip care → her, blanket tug-of-war → the couple). Generate all scenes in the same ChatGPT
conversation so the faces stay consistent:
https://chatgpt.com/c/6aecc42c-d8d0-83ec-b611-771e92336ada

| Character | Look | Files |
| --- | --- | --- |
| **KinJi mascot** (from the owner's selfies) | chibi anime, bold outlines, vibrant; chubby/heavy body (~105 kg), round face, narrow monolid eyes, thick black side-swept fringe, full lips; white tee + navy plaid open shirt, or white shirt + striped tie. Friendly, never mocking. | `images/kinji-mascot/character-sheet.png`, `character-main.png` |
| **Girlfriend อิงเอย** (cartoon) | same chibi style, adult (20+), covered cozy outfits only: cream cable-knit cardigan, floral high-collar top, long brown pleated skirt, flower pendant | `images/kinji-mascot/girlfriend-sheet.png` |
| **Couple** | both of the above | `images/kinji-mascot/couple-main.png`, scenes in `images/kinji-mascot/scenes/` |

The realistic อิงเอย presenter (Google Flow UGC) has its own rules: canonical references in
`B:\ChatGPT\PagePilotStarterKit\assets\selected\ingoei_v2\REFERENCE_RULES.md` (read first;
never use its `child/` folder for affiliate; covered outfits only). Produce those shots with
[google-flow](../google-flow/SKILL.md).

## 1. Pick products

- The owner signs in to the Shopee Affiliate dashboard; read it only (no clicks that
  change anything). Shopee shows verify/captcha pages to automation — stop and ask the
  owner rather than retry.
- Rank offers by commission × monthly sales; prefer **Mall / Preferred** with **EXTRA COMM**.
- Record each pick in `workspaces/research/<date>-<campaign>/affiliate-offers.md`: product,
  offer ID, shop type, commission seen (with date), monthly sales.
- Offer page: `https://affiliate.shopee.co.th/offer/product_offer/<offerId>`.
  Product link for the owner: `https://shopee.co.th/product/<shopid>/<itemid>` (itemid =
  offer ID; the owner cannot search offer IDs in the app, so always give the link).
  Commission shown changes day to day — tell the owner to re-check at "เอาลิงก์".

## 2. Build the clip (proven 11.11 recipe)

Duplicate a previous per-product content (`POST /api/contents/0G0Qt_ZllZ/duplicate`) or
create one in project `T6hY-sypjr` (`create_content`) with these settings:

```json
{ "templateId": "animestory", "aspectId": "9:16", "artStyleId": "chibi", "themeId": "shopee",
  "fontId": "kanit", "captionStyleId": "karaoke", "transitionId": "pushCut",
  "overlayId": "snow", "voiceId": "FfrJDiyJZK", "handle": "none", "musicVolume": 0 }
```

`overlayId` follows the season/gag (`snow` for the cold-weather set, `none` otherwise).
Three scenes, one delivery tag each (narration rules in [thai-voiceover](../thai-voiceover/SKILL.md)):

| Scene | Purpose | Image | `fx.graphic` used |
| --- | --- | --- | --- |
| 1 Hook | the relatable situation, first 1–2 s | character in the situation | `breakingNews` (position top) |
| 2 Gag | the struggle the product solves | character + product in the gag (`<product>-gag.png`) | `questHud` |
| 3 Product | what it is, 2–3 listing facts, CTA "กดตะกร้า" | the regenerated real product (`<product>-real.png`) | `checklist`, position top, scale 0.75 |

Then: attach images (`set_scene_image`), add SFX where the gag lands, `preview_frames`
(cards clear of captions, product matches `ref/`), `voice_content`, run
`npx tsx scripts/retention-check.ts <contentId>` in `content-studio`, render, verify the MP4.

Batch folder: `images/affiliate/<batch>/` holding `NN-<product>.mp4`, `<product>-gag.png`,
`<product>-real.png`, `ref/` (shop photos, reference only) and `captions.txt`.

Other routes when they fit better: the owner's own footage (`video-recap` template with the
product set), Flow UGC with อิงเอย (`clip-highlights`, transition `none`), the BotAutoFlow
template bank (`node scripts/aff-bank.mjs search <word>`; borrow structure only — never its
preview media, and strip any price lines), or [campaign-matrix](../campaign-matrix/SKILL.md)
for hook/ratio variants.

## 3. Hand over the posting table

After every batch, extend the posting table (`images/affiliate/ตารางโพสต์-1111.md`; start a
new file per campaign) and show it in chat, in Thai:

| # | วัน-เวลา | ไฟล์คลิป | สินค้าที่แนบ | ลิงก์สินค้า | ค่าคอมฯ | สถานะ |

Under the table, one fenced code block per post holding the ready-to-paste caption with
the hashtags at the end, so the owner copies it in one go. Rules:

- **≤150 characters including hashtags.** Aim for 130–140 with 4 tags
  (`#<product> #<problem> #<campaign> #ShopeeVideo`). Measure both counts:
  `python -X utf8 -c "s=open('cap.txt',encoding='utf-8').read().strip(); print(len(s), len(s.encode('utf-16-le'))//2)"`
- No price, no "AI". Write the length next to each post heading.
- Suggested times: lunch (12:00) and evening (20:00); say they are suggestions.
- When the owner says a clip is posted, update its status.

Never automate the posting itself; there is no affiliate posting API and Shopee blocks bots.
