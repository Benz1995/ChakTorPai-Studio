---
name: animation-principles
description: "Direct believable motion with Disney's 12 principles, biomechanical joint limits, centre of mass, kinetic chains and motion archetypes for 2D cutout characters, product motion and motion graphics. Use to plan or critique timing and choreography before implementing it in Remotion, GSAP or another engine; it is guidance, not a Lottie integration."
---

# Animation Principles — Disney's 12 Principles & Biomechanical Physics

A philosophy-first, physics-grounded motion design director. Teaches AI models how to think like animation directors—applying Disney's 12 Principles of Animation grounded in **Classical Mechanics, Biomechanics, and Kinetic Chains** to eliminate mechanical, distorted, broken-jointed, or PowerPoint-like motion.

For professional production, physical realism, or criticism of crude/slide-like
animation, read [production-practice.md](references/production-practice.md). Use its
exercises and shot evidence to make decisions; reciting principles or passing
technical QC is not evidence the resulting film meets the visual brief.

## Scope: simulated animation versus generated live action

For photorealistic generated film, judge visible contact, support, object permanence,
clearance and continuity over time; do not impose cartoon squash/stretch, uniform
phase delays or 2D screen-angle limits on real-looking bodies. MovieSkit uses
`B:/ChatGPT/MovieSkit/08_PIPELINE/skills/movieskit-short-drama/references/flow-audio-and-physical-action.md`.
That workflow also preserves Google Flow's native dialogue and sound. These are
direction/review criteria: adding Matter.js/Rapier/Blender cannot fix an existing
generated MP4 unless a shot is deliberately rebuilt with actual geometry/simulation.

---

## 🔬 1. The Physical Foundations of Animation

แอนิเมชันที่ "ดูไม่เพี้ยน" และ "มีชีวิตจริง" ต้องไม่เกิดจากการมโนตัวเลข แต่ต้องเคารพกฎฟิสิกส์ 4 ข้อ:

1. **Newton's 1st Law (Inertia & Overlapping Action):**
   - มวลมีผลต่อความเฉื่อย แต่จังหวะเริ่ม/หยุดขึ้นกับแรงและแรงบิดที่กระทำด้วย ไม่ใช่วัตถุหนักต้องช้ากว่าเสมอ
   - ผม ผ้า และชิ้นส่วนยืดหยุ่นอาจตามแรงช้าหรือสั่นต่อ ขึ้นกับโครงสร้าง แรง และ damping; ไม่กำหนด delay คงที่ให้ทุกส่วนของร่างกาย
2. **Newton's 2nd Law ($F = ma$ & Timing/Spacing):**
   - เมื่อแรงลัพธ์เท่ากัน มวลมากมีความเร่งน้อยกว่า ($a = F/m$); ไม่อนุมานความหนืดจากมวล และไม่ทำวัตถุหนักตกช้ากว่าเพียงเพราะหนักเมื่อไม่นับแรงต้านอากาศ
3. **Newton's 3rd Law (Action-Reaction & Anticipation):**
   - ตรวจการออกแรงกับพื้น/อุปกรณ์และการตอบสนองที่ตามมา การย่อเตรียมเป็นตัวเลือกการกำกับที่เหมาะกับบาง action ไม่ใช่เงื่อนไขว่าทุกการเคลื่อนต้องย่อตัวก่อน
4. **Volume-aware stylization (Squash/Stretch):**
   - สำหรับรูปทรงการ์ตูนที่ตั้งใจรักษาปริมาตรโดยประมาณ ถ้ายืดแกน Y สามารถชดเชยสองแกนขวางด้วย:
     $$\text{scale}_X \approx \frac{1}{\sqrt{\text{scale}_Y}}$$
   - สูตรนี้เป็นเครื่องมือจัดรูปทรง ไม่ใช่กฎสำหรับเนื้อเยื่อทุกชนิดหรือขอบเขตกายวิภาค ภาพคนจริงต้องรักษารูปร่างกระดูก/ข้อและ contact ไม่ใช้เปอร์เซ็นต์ squash/stretch เป็นเกณฑ์ผ่าน

---

## 🦴 2. Biomechanical Joint Limits (ตารางขอบเขตข้อต่อตามสรีรวิทยาจริง)

ตารางนี้เป็นช่วงกำกับท่าทางโดยประมาณสำหรับ rig 2D ไม่ใช่ช่วงทางคลินิก ขอบเขตจริงขึ้นกับแกน 3D ท่าตั้งต้นและตัวละคร; มุมที่เห็นบนภาพไม่ใช่มุมข้อต่อจริงเสมอ:

| ข้อต่อ (Joint) | ชนิดข้อต่อ | ขอบเขตการเคลื่อนไหวจริง (Safe Range) | กฎเหล็กที่ห้ามละเมิดเด็ดขาด |
| :--- | :--- | :--- | :--- |
| **คอ / ศีรษะ (Neck/Head)** | Pivot / Condyloid | เอียงข้าง: $-15^\circ$ ถึง $+15^\circ$<br/>ก้ม-เงย: $-25^\circ$ ถึง $+30^\circ$ | รักษาคอเชื่อมกับฐานศีรษะ; ช่วงนี้เป็นตัวอย่าง rig ไม่ใช่ขีดจำกัดของคนจริง |
| **หัวไหล่ (Shoulder)** | Ball & Socket | กางแขน: $0^\circ$ ถึง $180^\circ$<br/>หมุนเดินแกว่ง: $-30^\circ$ (ถอยหลัง) ถึง $+60^\circ$ (ไปข้างหน้า) | จุดหมุนต้องอยู่ที่เบ้าหัวไหล่เสมอ ไม่ใช่กึ่งกลางรักแร้ |
| **ข้อศอก (Elbow)** | Hinge (บานพับ) | งอแขน (Flexion): $0^\circ$ (แขนตรง) ถึง $145^\circ$ (งอชิดไหล่) | ป้องกันการหักผิดแกน/ข้อหลุดใน rig; อย่าตัดสินแกนจากซ้าย-ขวาบนภาพเพียงอย่างเดียว |
| **ข้อมือ (Wrist)** | Ellipsoid | กระดกขึ้น-ลง: $-45^\circ$ ถึง $+60^\circ$<br/>สะบัดข้าง: $-20^\circ$ ถึง $+30^\circ$ | ข้อมือต้องเคลื่อนไหวต่อเนื่องเป็นระลอกคลื่นตามแรงส่งจากข้อศอก |
| **สะโพก / โคนขา (Hip)** | Ball & Socket | เดินแกว่ง: $-20^\circ$ (ไปข้างหลัง) ถึง $+50^\circ$ (ก้าวไปข้างหน้า) | จุดหมุนต้องอยู่ที่หัวกระดูกต้นขา (Femur head) |
| **หัวเข่า (Knee)** | Hinge (บานพับ) | ตัวอย่างการงอใน rig: $0^\circ$ ถึง $140^\circ$ | รักษาแกนข้อต่อและความต่อเนื่องของขา; เข่าเคลื่อนมาข้างหน้าระหว่างก้าว/ย่อได้ ไม่ใช่หลักฐานว่าข้อหัก |
| **ข้อเท้า (Ankle)** | Hinge | กระดกปลายเท้า: $-30^\circ$ ถึง $+20^\circ$ | เท้าต้องระนาบกับพื้นเมื่อรับน้ำหนัก (Ground contact) |

---

## ⚖️ 3. Center of Mass & Ground Reaction (จุดศูนย์ถ่วงและการถ่ายเทน้ำหนัก)

1. **Static Balance:** เมื่อยืนนิ่งโดยไม่มีแรง/อุปกรณ์พยุงอื่น ตรวจแนวศูนย์มวลกับฐานรองรับจริง; ศูนย์มวลเปลี่ยนตามท่า ไม่ใช้ตำแหน่งเชิงกรานตายตัว การเดิน/เร่ง/เบรกเป็นสมดุลแบบเคลื่อนที่ ไม่ต้องมีแนวศูนย์มวลอยู่ระหว่างเท้าทุกเฟรม
2. **Weight Shift (การถ่ายน้ำหนัก):**
   - ตอนยกขา/ขึ้นบันได ตรวจการถ่ายแรงไปยังเท้าที่รับน้ำหนักและการเคลื่อนของลำตัวให้สัมพันธ์กัน ไม่บังคับเลื่อนสะโพกเป็นเปอร์เซ็นต์เดียวทุกท่า
   - ตอนโน้มตัว ให้ตรวจฐานรองรับ มือที่พยุง และแรงที่สัมพันธ์กับท่า; ไม่ใช้สมการสมดุลนิ่งกับการเคลื่อนที่เร่งโดยตรง
3. **Foot Planting (การตรึงเท้ากับพื้น):**
   - จุดเท้าที่กำลังยึดพื้นต้องสัมพันธ์กับพื้นใน world/surface space ไม่ใช่พิกัดจอเมื่อกล้องขยับ ยอมให้ส้น/ปลายเท้าหมุนถ่ายน้ำหนักตามท่า; ปฏิเสธการไถล/ทะลุพื้นที่ไม่มีเหตุรองรับ

---

## 🌊 4. Kinetic Chains & Wave Propagation (โซ่จลนศาสตร์การส่งแรง)

การสะบัดแขน โบกมือ หรือแกว่งดาบ เป็นกระบวนการส่งผ่านโมเมนตัมตามโซ่กระดูก:

```
[ลำตัว / หัวไหล่]  ──(ส่งแรง)──>  [ท่อนแขนบน]  ──(ส่งแรง)──>  [ท่อนแขนล่าง]  ──(ส่งแรง)──>  [ฝ่ามือ]
มวลมาก / แอมพลิจูดน้อย          เริ่มขยับ t=0          หน่วง t=Δt             หน่วง t=2Δt / แอมพลิจูดสูงสุด
```

- **สูตรหน่วงเวลา (Phase Delay):**
  $$\theta_n(t) = A_n \cdot \sin(\omega t - n \cdot \delta) \cdot e^{-\gamma t}$$
  โดยที่:
  - $\delta$ เป็น phase offset; จะแปลงเป็นเวลาได้เมื่อทราบความถี่ ($\Delta t = \delta/\omega$) จึงไม่เท่ากับ 2–4 เฟรมโดยตัวมันเอง
  - เลือก amplitude/phase ตาม action และข้อจำกัดของ rig ไม่บังคับว่ามือต้องแกว่งมากกว่าต้นแขนเสมอ โดยเฉพาะมือที่กำลังจับวัตถุอยู่

---

## 🌟 5. 4 Motion Personality Archetypes

| Archetype | Timing / Easing | Overshoot / Bounce | Damping Ratio ($\zeta$) | บริบทการใช้งาน |
| :--- | :--- | :--- | :--- | :--- |
| **Playful** | 200–350ms, `back.out(1.5)` | 10–18% overshoot | $\zeta \approx 0.5$ (Underdamped) | คอนเทนต์เด็ก, มาสคอต, สติกเกอร์, การ์ตูนสดใส |
| **Premium / Elegant** | 450–700ms, `power3.out` | 0% (ไม่มี overshoot) | $\zeta = 1$ critically damped; $\zeta > 1$ overdamped | แบรนด์หรู, เพลง Lo-Fi, สารคดี, ยานยนต์ |
| **Energetic / Punchy** | 120–220ms, `expo.out` | 3–6% คมชัด ฉับไว | $\zeta \approx 0.7$ (Light bounce) | ไฮไลท์เกม, คอนเทนต์กีฬา, TikTok Hooks |
| **Functional / Clean** | 150–250ms, `quad.out` | 0% เรียบง่าย ตรงจุด | $\zeta = 1.0$ (No oscillation) | ชาร์ตข้อมูล, แดชบอร์ด, คำบรรยาย |

---

## 🛡️ 6. Real Physics Verification Gate (เกณฑ์ตรวจความสมจริงทางฟิสิกส์ 8 ประการ)

The archetype timings above are starting points for short graphic/UI transitions,
not physical constants, universal film timing, or proof of a premium appearance.
Choose action duration from distance, forces/constraints, intent and reference.

ก่อนปล่อยงานแอนิเมชัน ต้องผ่านการตรวจสอบ 8 ข้อนี้:

1. [ ] **Joint Continuity (รอยต่อไม่หลุด):** รักษาจุดหมุน ความยาวกระดูก และรอยต่อของรูปทรง ไม่เห็นช่องว่างหรืออวัยวะหลุด; circular caps เป็นเพียงวิธีทำ cutout บางแบบ ไม่ใช่กายวิภาคหรือข้อกำหนดของทุกสไตล์
2. [ ] **Hinge Direction Check:** ข้อไม่หลุดหรือหักผิดแกนกายวิภาค; แยกการหมุน 3D และ perspective ออกจากการหักผิดจริง
3. [ ] **Support:** มีพื้น/ที่นั่ง/มือพยุงที่อธิบายแรงได้ ใช้ contact shadow ประกอบเมื่อแสงและมุมมองทำให้เห็น ไม่ตัดสินการลอยจากการไม่มีเงาเพียงข้อเดียว
4. [ ] **Ground Contact (เท้าไม่สไลด์):** เท้าหลักต้องยึดแน่นกับพื้น ไม่ไถลแบบไม่มีแรงเสียดทาน
5. [ ] **Shape and permanence:** ความยาวแขนขาและรูปทรงวัตถุไม่ละลาย/หาย/งอกซ้ำ; squash/stretch ใช้เฉพาะสไตล์ที่ตั้งใจ
6. [ ] **Contact and timing:** มือจับติดกับวัตถุจนปล่อย เท้ารับแรงก่อนยกตัว ประตูเปิดมีระยะผ่าน ช้อนสัมผัสอาหารก่อนยก; ไม่มีการทะลุหรือ teleport และไม่บังคับ delay เท่ากันทุกส่วน
7. [ ] **Balance and forces:** ตรวจฐานรับน้ำหนัก โมเมนตัม และแรงพยุงจริง; การเอน/เร่งแบบเคลื่อนที่ไม่ต้องรักษาสมดุลนิ่งทุกเฟรม และอาจมีโต๊ะ มือ หรือที่นั่งช่วยรับแรง
8. [ ] **No Clipart Slop (ไม่ใช้รูปทรงเด็กอนุบาล):** ห้ามนำสี่เหลี่ยมเรขาคณิตดิบ ๆ มาเรียงต่อกันเป็นตัวละคร ต้องมีรูปทรงกายวิภาคที่ถูกต้อง (ความโค้งกล้ามเนื้อ ข้อต่อ ลายเส้นระดับงานออกแบบมืออาชีพ)

ตรวจทั้งช่วงเคลื่อนไหวที่ใช้จริงและรอยต่อ พร้อมดูทีละเฟรมรอบ contact ที่สงสัย บันทึก source/final timestamps, วิธีดูและหลักฐาน ภาพนิ่งไม่กี่จุดหรือคะแนน QC รวมไม่ทำให้การทะลุวัตถุผ่านได้; หากไม่มีมุม/หลักฐานพอตัดสินให้ระบุว่ายังไม่ยืนยัน
