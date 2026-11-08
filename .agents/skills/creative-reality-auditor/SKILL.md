---
name: creative-reality-auditor
description: Multi-agent creative quality assurance system auditing reality, physics, story logic, emotion, music, visual continuity, audience engagement, devil's advocate challenges, and chief judge verdicts across content, music, cartoon, drama, and storytelling.
---

# Creative Reality Auditor (CRA) — ระบบกรรมการ AI ตรวจคุณภาพผลงานสร้างสรรค์

ระบบ **Creative Reality Auditor (CRA)** คือกรอบการทำงาน Multi-Agent Creative Quality Assurance อิสระสำหรับคัดกรอง ตรวจสอบ โต้แย้ง ให้คะแนน และตัดสินคุณภาพผลงานก่อนเข้าสู่กระบวนการผลิต (Production) หรือเผยแพร่จริง

> **หัวใจสำคัญสูงสุด:**
> **"ความจริงและเหตุผลเหนือเสียงส่วนใหญ่ (Truth Over Consensus)"**
> ต่อให้กรรมการ AI 7 ตัวโหวตว่าผ่าน แต่หากมีข้อเท็จจริงผิดที่พิสูจน์ได้ หรือเกิดความขัดแย้งเชิงตรรกะที่ทำลายโครงสร้างเรื่อง (Critical Failure) งานนั้นต้องถูกส่งกลับไปแก้ไข (`REVISE`) หรือปฏิเสธ (`REJECT`) ห้ามปล่อยผ่านด้วยคะแนนเฉลี่ยเด็ดขาด

---

## 1. ขอบเขต 5 ประเภทผลงานที่รองรับ

ระบบจะเลือกชุดกรรมการ เกณฑ์ และน้ำหนักคะแนนตามโปรไฟล์ประเภทผลงานโดยอัตโนมัติ:

1. **[Content Creator](profiles/content.yaml):** TikTok, YouTube Shorts, Reels, วิดีโอเล่าเรื่อง, สารคดีสั้น และคอนเทนต์ให้ความรู้ (เน้นข้อเท็จจริงและความลื่นไหลในการดึงดูดผู้ชม)
2. **[Music & Lyrics](profiles/music.yaml):** เนื้อเพลง โครงสร้างเพลง ความหมาย สัมผัสคำ จำนวนพยางค์ ความต่อเนื่องของมุมมองผู้เล่า (POV) และความทรงพลังของ Hook
3. **[Cartoon & Animation](profiles/cartoon.yaml):** บทการ์ตูน, Chibi 3D series, Storyboard, Animation Prompt, ความต่อเนื่องของตัวละคร และการปฏิบัติตามกฎโลกสมมติ
4. **[Short Drama & Film](profiles/short-drama.yaml):** ละครสั้น หนังสั้น บทสนทนาภาษาไทยแท้ ความสมจริงทางจิตวิทยา พล็อต และความต่อเนื่องของฉาก
5. **[Creative Storytelling](profiles/storytelling.yaml):** นิยาย เรื่องเล่า สคริปต์เสียงบรรยาย (Audio Drama) และเรื่องแต่งเชิงสร้างสรรค์

---

## 2. คณะกรรมการ AI 8 บทบาท และประธานชี้ขาด

| บทบาทกรรมการ | เอกสารอ้างอิง | ภารกิจหลักในการตรวจสอบ |
| :--- | :--- | :--- |
| **JUDGE 01 — Reality & Fact** | [agents/reality-judge.md](agents/reality-judge.md) | ข้อเท็จจริงโลกจริง วันที่ สถานที่ ข้อมูลประวัติศาสตร์ วิทยาศาสตร์ ป้องกันการอ้างอิงปลอม (ติดป้าย `UNVERIFIED`) |
| **JUDGE 02 — Physics & Feasibility** | [agents/physics-judge.md](agents/physics-judge.md) | กฎฟิสิกส์ แรงโน้มถ่วง ขีดจำกัดร่างกายมนุษย์ ความเร็ว/เวลา รองรับ 5 โหมดโลก (Realistic, Stylized, Fantasy, Sci-Fi, Absurd Comedy) |
| **JUDGE 03 — Story Logic & Continuity** | [agents/story-logic-judge.md](agents/story-logic-judge.md) | เหตุและผล ช่องโหว่พล็อต (Plot Holes) เส้นเวลา แรงจูงใจ ความต่อเนื่องของสิ่งของ บาดแผล และสถานะตัวละคร |
| **JUDGE 04 — Emotional & Human Behavior** | [agents/emotion-judge.md](agents/emotion-judge.md) | ความสมจริงทางอารมณ์ จิตวิทยาพฤติกรรมมนุษย์ บทสนทนาภาษาไทยแท้ไม่แปลตรงตัว ([thai-craft](../thai-craft/SKILL.md)) |
| **JUDGE 05 — Music & Lyrics** | [agents/music-judge.md](agents/music-judge.md) | ความหมาย สัมผัส วรรคตอน จังหวะพยางค์ โครงสร้างเพลง (Verse/Chorus/Bridge) **ห้ามตัดสินเรื่องเสียงร้องหากไม่มีไฟล์เสียงจริง** |
| **JUDGE 06 — Visual & Scene Continuity** | [agents/visual-judge.md](agents/visual-judge.md) | อัตลักษณ์ตัวละคร (หน้า/ผม/ชุด/พร็อพ) ทิศทางแสง กฎ 180 องศา โครงสร้างมือ AI **ห้ามอ้างว่าตรวจภาพหากไม่มีไฟล์ภาพจริง** |
| **JUDGE 07 — Audience & Engagement** | [agents/audience-judge.md](agents/audience-judge.md) | พลังของ Hook 3 วินาทีแรก จุดคนดูสับสนหรือกดข้าม (Drop-off) จังหวะดำเนินเรื่อง (Pacing) |
| **JUDGE 08 — Devil's Advocate** | [agents/devils-advocate.md](agents/devils-advocate.md) | ผู้คัดค้านอิสระ ท้าทายสมมติฐาน ค้นหาข้อบกพร่องที่กรรมการอื่นมองข้าม และดักจับการโหวตตามกันโดยไร้หลักฐาน |
| **Supreme Chief Judge** | [agents/chief-judge.md](agents/chief-judge.md) | สังเคราะห์หลักฐาน ไกล่เกลี่ยข้อโต้แย้ง คำนวณคะแนนถ่วงน้ำหนัก ตรวจสิทธิ์ Veto ข้อผิดพลาดร้ายแรง และออกคำตัดสินสุดท้าย |

---

## 3. ขั้นตอนการทำงาน Multi-Agent Workflow

```
[INPUT CREATIVE WORK]
        │
        ▼
[1. CLASSIFY & PROFILE]  ── โหลด Profile, World Mode, และกำหนดน้ำหนักคะแนน
        │
        ▼
[2. INDEPENDENT REVIEW] ── กรรมการแต่ละท่านตรวจแยกอิสระ ห้ามเห็นคะแนนกันก่อน
        │
        ▼
[3. DEVIL'S ADVOCATE]   ── ตรวจจับ Groupthink, เสนอ Counterexamples และท้าทายสมมติฐาน
        │
        ▼
[4. EVIDENCE CHECK]     ── กรองข้อมูล UNVERIFIED, ตัดข้ออ้างเท็จ, พิสูจน์หลักฐานเชิงประจักษ์
        │
        ▼
[5. WEIGHTED SCORING]   ── คำนวณคะแนนตามสัดส่วนร้อยละ (เต็ม 100)
        │
        ▼
[6. CHIEF JUDGE VERDICT]── บังคับใช้ Critical Failure Veto, ออกคำตัดสิน และจัดทำ Minimal Fix Plan
        │
        ▼
[OUTPUT REPORT]         ── ส่งมอบ Markdown Report และ JSON Schema
```

---

## 4. กฎและนโยบายกำกับดูแล (Core Policies)

- **[Reality Rules](rules/reality-rules.md):** การจัดประเภทข้อมูล (Verified, Fiction, Opinion, UNVERIFIED) และการห้ามแต่งหลักฐานเท็จ
- **[Physics & World Rules](rules/physics-rules.md):** การผ่อนปรนตามโหมดโลก (Fantasy ตรวจตามกฎของเรื่อง ไม่บังคับใช้ฟิสิกส์โลกจริง)
- **[Narrative Logic Rules](rules/narrative-rules.md):** นิยาม Plot Hole 3 รูปแบบ และสัญญาความรู้ตัวละคร (Character Knowledge Contract)
- **[Critical Failures Taxonomy](rules/critical-failures.md):** การจัดระดับ INFO, LOW, MEDIUM, HIGH, CRITICAL และการใช้สิทธิ์ Veto
- **[Voting & Debate Policy](rules/voting-policy.md):** หลักการ Truth Over Consensus, ขอบเขตการอภิปราย 2 รอบ และบันทึก Human Override

---

## 5. คำสั่งและ Triggers ในการเรียกใช้งาน

รองรับทั้ง Slash Commands และ Natural Language Prompt:

| คำสั่ง (Command) | การทำงาน |
| :--- | :--- |
| `/creative-audit` | สแกนและตรวจคุณภาพผลงานอัตโนมัติแบบ Full Multi-Agent Panel |
| `/audit-story` | ตรวจเฉพาะตรรกะพล็อต เส้นเวลา และความสมเหตุสมผลของตัวละคร |
| `/audit-lyrics` | ตรวจเนื้อเพลง สัมผัส จำนวนพยางค์ ความต่อเนื่องของมุมมอง (POV) |
| `/audit-cartoon` | ตรวจบทการ์ตูน กฎโลกสมมติ และความต่อเนื่องของภาพตัวละคร |
| `/audit-reality` | ตรวจสอบข้อเท็จจริงโลกจริง ข้อมูลวิทยาศาสตร์ ประวัติศาสตร์ และตัวเลข |
| `/audit-continuity`| ตรวจความต่อเนื่องของพร็อพ เสื้อผ้า แสงเงา และสถานะตัวละคร |
| `/audit-debate` | เปิดรอบโต้แย้งระหว่างกรรมการทั่วไปกับ Devil's Advocate |
| `/audit-fix` | เสนอแนวทางแก้ไขแบบ Minimal Fix First ก่อนเขียนใหม่ |
| `/audit-compare` | เปรียบเทียบผลงานก่อนและหลังแก้ไขแบบ Before / After |

---

## 6. สัญญาข้อมูล Input และ Output (Data Contracts)

- **Input Schema:** [schemas/input.schema.json](schemas/input.schema.json)
- **Report Schema:** [schemas/report.schema.json](schemas/report.schema.json)
- **Report Template:** [templates/quality-report.md](templates/quality-report.md)
- **Actionable Revision Template:** [templates/revision-plan.md](templates/revision-plan.md)

---

## 7. เครื่องมือประมวลผลและการรันระบบ (CLI & Tests)

ระบบมีสคริปต์อัตโนมัติพร้อมรันในโปรเจกต์ BigO โดยไม่ต้องติดตั้งแพ็กเกจภายนอกเพิ่ม:

```powershell
# 1. รันการตรวจสอบผลงาน
node .agents/skills/creative-reality-auditor/scripts/audit-engine.mjs audit <input.json> --output-md report.md --output-json report.json

# 2. รันชุดทดสอบคุณภาพ 12 กรณีศึกษา (Automated Test Suite)
node .agents/skills/creative-reality-auditor/scripts/run-tests.mjs
```

ดูตัวอย่างผลการตรวจจริงได้ในโฟลเดอร์ [examples/](examples/)
- [ตัวอย่างละครสั้น](examples/short-drama-sample.md)
- [ตัวอย่างเนื้อเพลง](examples/music-sample.md)
- [ตัวอย่างการ์ตูน Chibi](examples/cartoon-sample.md)
- [ตัวอย่างคลิปสั้นให้ความรู้](examples/content-sample.md)
- [ตัวอย่างเรื่องเล่าสคริปต์เสียง](examples/storytelling-sample.md)
