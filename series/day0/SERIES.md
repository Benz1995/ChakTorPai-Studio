# วันที่ 0 (Day 0) — series bible

Channel: PolyTale. Skill: `.agents/skills/polytale-series/SKILL.md`.
Master Thai Craft: `.agents/skills/thai-craft/SKILL.md` (ironclad rule: dynamic flow, zero English calques, native Thai dialogue registers, human gate before voice).

**Logline:** one ordinary morning every phone rings at once — war has begun and you have
15 minutes. You, your little brother ต้นกล้า (8) and the dog ข้าวตู must survive the
fallen world and reach the "survivor centre" heard on the radio. Fiction; no real
countries or leaders.

| Item | Value |
| --- | --- |
| ChatGPT conversation (all images of this series) | https://chatgpt.com/c/6aee0d87-9e90-83ec-858f-6c64f613fc89 |
| Content Studio main project | `6Q9g7R_TFm` "วันที่ 0 (Day0)" (voice `FfrJDiyJZK`, 9:16) |
| Badge on covers/title | "วันที่ N" (day counter) instead of "ตอนที่ N" |
| Style | low-poly chibi Option C — `assets/style-options/option-c.png` |
| Narrator voice | Content Studio `FfrJDiyJZK` = ElevenLabs `XELzaccf66eUgLtL3BV1` (use the latter in `lines` for single re-takes) |
| Child voice (ต้นกล้า) | ElevenLabs `w3e1Jn4F37O7wDwETrJ9` + pitch 1.18 |
| Content Studio contents | ep00 `6_FyU76Uha`, ep01 `F2382pG3tg` |

## Series devices (keep every episode)

- Top-left stamp `วันที่ N · HH:MM`; top-right timer or counter (ep01: countdown 15:00 → 00:00; later: radiation counter).
- The plush dinosaur appears at every emotional turn.
- Episodes end on an A/B viewer choice; the next episode follows the majority (record it below).
- Smash to silence before every big event.

## Characters and layers (`characters/`)

| File | Who | Notes |
| --- | --- | --- |
| `boy.png` | you (teen boy) | spiky dark hair, olive jacket, backpack + bedroll, white scarf-mask, bandaged right hand |
| `brother.png` | ต้นกล้า | red pompom beanie, beige jacket, green plush dinosaur |
| `dog.png` | ข้าวตู | brown Thai dog, upright ears, dark collar |
| `bg-plate.png` | ruined street (after the blast) | 941×1672 |
| `cloud.png` / `cloud-lowpoly.png` | mushroom cloud props | use the low-poly one |
| `boy-blink.png`, `brother-blink.png` | eyes-closed variants | for `blink` |
| `boy-look.png`, `brother-look.png`, `dog-look.png` | turned toward the sky, reacting | for `swaps` |
| `fg-debris.png` | foreground rubble corners | `fg` depth layer |
| `kru-ek.png` | ครูเอก full body | introduced in ep01 |

Planned additions: หัวหน้าหน้ากาก (gas-mask gang leader). ครูเอก: thin old man ~65, grey messy hair, round glasses, brown vest over white shirt, old Geiger counter.

## Episodes

| Ep | Badge | Title | Beat | Status |
| --- | --- | --- | --- | --- |
| 00 | วันที่ 0 | ไซเรน (opening) | phones ring, war declared, run, flash | done: `ep00/render/day0-ep00-opening.mp4` |
| 01 | วันที่ 0 | ไซเรน | hook question, calm morning, alerts, 15-min countdown, packing, dinosaur, run, ครูเอก, fork A/B, flash | final v5 2026-11-07: `ep01/render/day0-ep01.mp4` (97.8 s, earshot 23/23) + `day0-ep01-summary.png`; not yet heard by the owner; choice asked: A ร้านซ่อมวิทยุ / B สถานีใต้ดิน (result: pending) |
| 02A | วันที่ 0 | ใต้ดิน (ร้านครูเอก) | basement of radio shop, seal vents, 24 h rule, knock on the door | final v3 2026-11-08: `ep02/render/day0-ep02.mp4` (147.5 s, -14.4 LUFS, voiceover-first, extended outro 8.5s); choice asked: A แง้มประตูรับคนเจ็บ / B ปิดตาย 24 ชม. |
| 02B | วันที่ 0 | สถานีใต้ดิน (Bad End) | crowd crush, power cut, shutter locks, blast wave caught outside | final v3 2026-11-08: `ep02_badend/render/day0-ep02-badend.mp4` (125.4 s, -14.3 LUFS, voiceover-first, separate outro 7.5s); lesson: F1/F2 Any building is safer |
| 03 | วันที่ 1 | เคาะ (สายรอด) | neighbour coated in ash knocks on hatch, Kru Ek teaches decontamination protocol | final v2 2026-11-08: `ep03/render/day0-ep03.mp4` (140.9 s, -14.4 LUFS, voiceover-first, strict 1:1 visual coherence, clean cards, extended outro 8.0s); lesson: F9/F10/F11 (decontamination, gentle wash, no sanitizer); choice: A เสี่ยงออกไปหาเสบียงและน้ำ / B กักตัวต่อจำกัดน้ำ |
| 03B | วันที่ 1 | ปิดตาย (Bad End) | vote B chose to keep hatch deadlocked for 24h, Uncle Somsak dies from untreated radiation | final v3 2026-11-08: `ep03_badend/render/day0-ep03-badend.mp4` (108.3 s, -14.7 LUFS, voiceover-first, strict 1:1 visual coherence generated directly in series ChatGPT thread for exact canon character consistency: Kru Ek peeking hatch, Somsak collapsed in ash, Ton Kla crying with dino, clean cards, extended outro 8.0s); lesson: prompt decontamination saves lives |
| 04 | วันที่ 2 | ฝนดำ | black rain, brother thirsty | ข้าวตู is gone |
| 05 | วันที่ 3 | วิทยุ | radio: survivor centre at the northern dam | second voice: "don't trust the army trucks" |
| 06 | วันที่ 4 | เมืองเถ้า | walk through the silent ash city, counter clicks faster | ข้าวตู returns with someone's name tag |
| 07 | วันที่ 5 | ซุปเปอร์ | scavenging an abandoned supermarket | torches between the shelves |
| 08 | วันที่ 5 | หน้ากาก | gang leader wants the dog for food | ครูเอก stays as hostage |
| 09 | วันที่ 6 | ไข้ | brother sick, hair falling, need iodine | brother collapses |
| 10 | วันที่ 7 | โรงพยาบาล | raid the empty hospital | someone in the drug room knows your name |
| 11 | วันที่ 8 | ด่าน | survivor centre checks radiation | "the sick can't enter" |
| 12 | วันที่ 9 | ฟ้าใหม่ | inside; the radio voice was a tape recorded before Day 0 | "who knew?" — ask viewers about season 2 |

## Known weak spots (from ep00)

- Standing character layers face each other; make a "turn to look at the flash" layer for ep01.
- Run poses A/B differ little; ask for clearer opposite leg phases.
