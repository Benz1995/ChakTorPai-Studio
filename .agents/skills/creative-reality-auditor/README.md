# Creative Reality Auditor (CRA)

> **ระบบกรรมการ AI ตรวจสอบคุณภาพผลงานสร้างสรรค์แบบ Multi-Agent Quality Assurance**  
> มุ่งเน้น: **"ความจริงและเหตุผลเหนือเสียงส่วนใหญ่ (Truth Over Consensus)"**

---

## สารบัญ
1. [ภาพรวมของระบบ](#1-ภาพรวมของระบบ)
2. [สถาปัตยกรรมคณะกรรมการ AI](#2-สถาปัตยกรรมคณะกรรมการ-ai)
3. [โปรไฟล์การให้คะแนน 5 ประเภทผลงาน](#3-โปรไฟล์การให้คะแนน-5-ประเภทผลงาน)
4. [กลไกตรวจจับข้อผิดพลาดร้ายแรง (Critical Failure Veto)](#4-กลไกตรวจจับข้อผิดพลาดร้ายแรง)
5. [การติดตั้งและใช้งานบนแพลตฟอร์มต่างๆ](#5-การติดตั้งและใช้งานบนแพลตฟอร์มต่างๆ)
6. [ผลการทดสอบระบบ (Test Results)](#6-ผลการทดสอบระบบ)
7. [ตัวอย่างผลการตรวจงานจริง](#7-ตัวอย่างผลการตรวจงานจริง)
8. [ข้อจำกัดและแนวทางในอนาคต](#8-ข้อจำกัดและแนวทางในอนาคต)

---

## 1. ภาพรวมของระบบ

Creative Reality Auditor (CRA) ถูกสร้างขึ้นเพื่อแก้ปัญหาที่ AI มัก "เออออตามผู้ใช้" (Sycophancy) หรือปล่อยให้ข้อผิดพลาดสำคัญหลุดรอดไปเพียงเพราะบทสนทนาฟังดูไพเราะหรือคะแนนเฉลี่ยส่วนใหญ่โหวตให้ผ่าน

CRA จำลองกองบรรณาธิการ ทีมตรวจสอบข้อเท็จจริง ผู้เชี่ยวชาญด้านฟิสิกส์ ผู้กำกับภาพ นักแต่งเพลง และผู้คัดค้านอิสระ (Devil's Advocate) ที่ตรวจสอบผลงานอย่างเป็นกลาง โดยแยกกระบวนการตรวจสอบออกเป็นอิสระก่อนนำมาอภิปรายและตัดสินโดยประธานชี้ขาด (Chief Judge)

---

## 2. สถาปัตยกรรมคณะกรรมการ AI

```
                        [Creative Work Input]
                                  │
         ┌────────────────────────┴────────────────────────┐
         ▼                                                 ▼
[Reality & Fact Checker]                         [Physics & Feasibility]
(ความจริงโลกจริง/ไม่แต่งหลักฐาน)                   (แรงโน้มถ่วง/ขีดจำกัดมนุษย์/โหมดโลก)
         │                                                 │
         ▼                                                 ▼
[Story Logic & Continuity]                       [Emotional & Human Behavior]
(พล็อตโฮล/เส้นเวลา/แรงจูงใจ)                       (จิตวิทยาตัวละคร/ภาษาไทยแท้)
         │                                                 │
         ▼                                                 ▼
[Music & Lyrics Judge]                           [Visual Continuity Judge]
(สัมผัส/วรรค/POV/ไม่มโนเรื่องเสียง)                 (หน้าตาตัวละคร/แสงเงา/ไม่มโนเรื่องภาพ)
         │                                                 │
         └────────────────────────┬────────────────────────┘
                                  ▼
                     [Audience & Engagement]
                     (Hook 3 วิแรก/Pacing/จุดดรอป)
                                  │
                                  ▼
                       [Devil's Advocate]
                       (ค้นหาจุดบอด/ท้าทายสมมติฐาน/ดักจับ Groupthink)
                                  │
                                  ▼
                        [Supreme Chief Judge]
                        - ชั่งน้ำหนักหลักฐาน
                        - คำนวณคะแนนถ่วงน้ำหนัก (0-100)
                        - บังคับใช้สิทธิ์ Veto (Critical Fail)
                        - ออกคำตัดสิน: PASS | PASS_WITH_NOTES | REVISE | REJECT
```

---

## 3. โปรไฟล์การให้คะแนน 5 ประเภทผลงาน

| ประเภทผลงาน | เกณฑ์และน้ำหนักคะแนนเริ่มต้น | ไฟล์โปรไฟล์ |
| :--- | :--- | :--- |
| **Short Drama & Film** | Story Logic 25% • Emotion 25% • Feasibility 20% • Pacing 20% • Visual 10% | [profiles/short-drama.yaml](profiles/short-drama.yaml) |
| **Music & Lyrics** | Meaning & Story 25% • Emotion 25% • Singability 20% • Structure 20% • Originality 10% | [profiles/music.yaml](profiles/music.yaml) |
| **Cartoon & Animation**| World Logic 25% • Character Continuity 25% • Story 20% • Visual 20% • Pacing 10% | [profiles/cartoon.yaml](profiles/cartoon.yaml) |
| **Content Creator** | Factual Accuracy 30% • Engagement 25% • Structure 20% • Clarity 15% • Fit 10% | [profiles/content.yaml](profiles/content.yaml) |
| **Creative Storytelling** | Narrative World 25% • Depth 25% • Pacing 20% • Voice Craft 20% • Engagement 10% | [profiles/storytelling.yaml](profiles/storytelling.yaml) |

---

## 4. กลไกตรวจจับข้อผิดพลาดร้ายแรง

CRA แบ่งระดับปัญหาออกเป็น 5 ลำดับ: `INFO`, `LOW`, `MEDIUM`, `HIGH`, `CRITICAL`

> **กฎเหล็ก Veto Power:**
> หากพบปัญหาในระดับ **`CRITICAL`** ที่ยืนยันได้ เช่น:
> - ตัวละครตายแล้วเดินกลับเข้ามาในฉากต่อเนื่องโดยไม่มีเหตุผล
> - ข้อมูลข้อเท็จจริงสำคัญในวิดีโอให้ความรู้ผิดพลาดอย่างสิ้นเชิง
> - มุมมองผู้เล่าในเพลงขัดแย้งกันเองจนทำลายสาระสำคัญ
>
> **ผลงานจะถูกสั่ง `REVISE` หรือ `REJECT` ทันที แม้คะแนนรวมจะได้ 80-90+ คะแนนก็ตาม**

---

## 5. การติดตั้งและใช้งานบนแพลตฟอร์มต่างๆ

### ก. การใช้งานใน BigO / Antigravity
สกิลนี้ได้รับการติดตั้งไว้ใน `.agents/skills/creative-reality-auditor/` และพร้อมถูกเรียกใช้งานโดย Agent อัตโนมัติ หรือเรียกผ่าน Slash Commands:
- `/creative-audit` — สั่งตรวจงานอัตโนมัติเต็มรูปแบบ
- `/audit-story` — เน้นตรวจบทและพล็อต
- `/audit-lyrics` — เน้นตรวจเนื้อเพลง
- `/audit-cartoon` — เน้นตรวจการ์ตูน
- `/audit-reality` — เน้นตรวจความสมจริงและข้อเท็จจริง

### ข. การใช้งานร่วมกับ Claude Code
รันสคริปต์ซิงก์ของ BigO เพื่อสร้าง Claude Code Entrypoint:
```powershell
node scripts/motion-skills.mjs sync
node scripts/motion-skills.mjs check
```

### ค. การรันผ่าน CLI หรือ Automated Pipeline
สามารถเรียกใช้งานได้โดยตรงด้วย Node.js:
```powershell
# ตรวจสอบผลงานจากไฟล์ JSON พร้อมบันทึกผลเป็น Markdown Report
node .agents/skills/creative-reality-auditor/scripts/audit-engine.mjs audit <input.json> --output-md report.md --output-json report.json
```

---

## 6. ผลการทดสอบระบบ (Test Results)

ระบบมาพร้อมชุดทดสอบอัตโนมัติ 12 กรณีศึกษา ครอบคลุมทั้งกรณีข้อผิดพลาดร้ายแรง, การป้องกันผลบวกเท็จ (False Positives), ตรรกะโลกแฟนตาซี, และงานข้อมูลไม่ครบถ้วน:

```powershell
node .agents/skills/creative-reality-auditor/scripts/run-tests.mjs
```

**สรุปผลการทดสอบ (12/12 ผ่าน 100%):**
- `TEST-01`: ละครสั้นที่มี Plot Hole ตัวละครตายแล้วฟื้น (`REVISE`, Critical Fail: `true`)
- `TEST-02`: ละครสั้นสมจริงและผ่านเกณฑ์ (`PASS`, Total: `90.9/100`)
- `TEST-03`: เนื้อเพลงที่มุมมองผู้เล่าขัดแย้งกันเอง (`REVISE`, Critical Fail: `true`)
- `TEST-04`: เพลงที่ใช้ภาษาเปรียบเทียบเชิงกวี — ไม่ติด False Positive ฟิสิกส์ (`PASS`)
- `TEST-05`: การ์ตูนแฟนตาซีที่มีกฎเวทมนตร์ชัดเจน — ผ่านเกณฑ์ตามกฎโลกสมมติ (`PASS`)
- `TEST-06`: การ์ตูนที่มีโมเดลตัวละครกลายพันธุ์ข้ามช็อต (`REVISE`)
- `TEST-07`: คอนเทนต์สารคดีที่ระบุปีและประวัติศาสตร์ผิด (`REVISE`)
- `TEST-08`: คอนเทนต์ที่มีการอ้างสรรพคุณเกินจริง — ติดป้าย `UNVERIFIED` ป้องกันการมโนหลักฐาน (`PASS_WITH_NOTES`)
- `TEST-09`: การโต้แย้งระหว่าง Devil's Advocate กับกรรมการทั่วไปเรื่องการสแกนลายนิ้วมือศพ (`PASS_WITH_NOTES`)
- `TEST-10`: งานที่ได้คะแนนสูง 82.3 แต่มีข้อเท็จจริงพิษไซยาไนด์ผิดระดับ CRITICAL — ติดสิทธิ์ Veto บังคับตีกลับ (`REVISE`)
- `TEST-11`: งานขอตรวจภาพ AI แต่วิดีโอ/รูปภาพไม่ถูกแนบ — ออกคำตัดสิน `INSUFFICIENT_EVIDENCE` ไม่มโนตรวจเอง
- `TEST-12`: งานเขียนคุณภาพสูงแบบ Slow Burn — ป้องกันไม่ให้ AI สั่งเขียนใหม่โดยพลการ (`PASS`, `95.3/100`)

---

## 7. ตัวอย่างผลการตรวจงานจริง

ระบบมีตัวอย่าง Input และรายงานผลสมบูรณ์ในโฟลเดอร์ `examples/`:
1. [ละครสั้นคดีกระจกเงา (Short Drama Sample Report)](examples/short-drama-sample.md)
2. [เพลงกอดลมหนาว (Music Sample Report)](examples/music-sample.md)
3. [โพลีเทลเอาชีวิตรอดในป่าฝนกรด (Cartoon Chibi Sample Report)](examples/cartoon-sample.md)
4. [3 ความจริงของกาแฟคั่วเข้มคั่วอ่อน (Content Sample Report)](examples/content-sample.md)
5. [เสียงหวูดรถไฟขบวนสุดท้าย (Storytelling Audio Drama Sample Report)](examples/storytelling-sample.md)

---

## 8. ข้อจำกัดและแนวทางในอนาคต

1. **การวิเคราะห์ไฟล์มัลติมีเดีย (Media Grounding):** การตรวจสอบเสียงร้อง คีย์เพลง หรือภาพ ต้องอาศัยเครื่องมือเฉพาะทาง (เช่น Earshot สำหรับตรวจเสียง หรือโมเดล Vision สำหรับตรวจรูปภาพ) หากไม่มีไฟล์แนบ ระบบจะจำกัดการตรวจเฉพาะตัวบทข้อความอย่างเคร่งครัด
2. **การอัปเดตข้อเท็จจริง (Live Web Research):** ข้อเท็จจริงโลกจริงที่เกิดขึ้นใหม่ล่าสุด ควรเชื่อมต่อกับเครื่องมือค้นหาข้อมูลออนไลน์เพื่อยืนยันแหล่งที่มาที่น่าเชื่อถือ
3. **อำนาจตัดสินขั้นสุดท้ายเป็นของมนุษย์ (Human Final Authority):** คำตัดสินของ AI ทุกบทบาทเป็นเพียงข้อเสนอแนะเชิงบรรณาธิการ ผู้สร้างผลงานมีสิทธิ์ Override คำตัดสินได้เสมอพร้อมการบันทึกเหตุผล
