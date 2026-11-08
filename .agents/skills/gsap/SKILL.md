---
name: gsap
description: "Use GSAP (on-demand) for multi-layer asset animation, 2D cutout character rigging, nested timeline choreography and 2.5D parallax, driven frame by frame inside Remotion templates. Use when a Content Studio scene needs many coordinated layers or a rigged cutout character."
---

# GSAP Skills — Physics-Grounded Timeline & 2D Cutout Rigging

Master the GreenSock Animation Platform (GSAP 3) for multi-layer asset animation, biomechanically sound 2D cutout character rigging, nested timelines, and deterministic video frame scrubbing in BigO Content Studio.

> **BigO status (on-demand):** `gsap` is not installed in `content-studio`. Add it there with an exact version only
> when a task needs GSAP, check its licence terms at install time, and follow
> [the render contract](../motion-studio/references/render-contract.md). Prefer Remotion `interpolate()`/`spring()` for
> simple moves; use [animation-principles](../animation-principles/SKILL.md) for timing and joint limits.

---

## 🎯 1. Core Vocabulary & Concepts

| คำศัพท์ | ความหมายและบทบาทใน GSAP |
| :--- | :--- |
| **Asset Animation** | การนำชิ้นส่วนภาพแยก (PNG/SVG) เช่น ก้อนเมฆ รถ วัตถุประกอบฉาก มาเคลื่อนไหวอย่างอิสระด้วยความเร็วและทิศทางที่ต่างกัน |
| **2D Cutout Animation** | การแยกตัวละครเป็นชิ้นส่วนย่อย (หัว, ลำตัว, แขนบน, แขนล่าง, มือ, ขา) กำหนดจุดหมุน (`transformOrigin`) แล้วสร้างแอนิเมชันความสัมพันธ์แบบ Parent-Child |
| **Motion Graphics** | การเคลื่อนไหวข้อความ รูปร่าง และกราฟิกเชิงเส้นผ่าน Keyframe และ Timelines ที่แม่นยำระดับมิลลิวินาที |
| **2.5D Parallax Animation** | การแบ่งฉากเป็นเลเยอร์ชัดลึก (Foreground, Midground, Background) แล้วเคลื่อนที่ด้วยสัดส่วนความเร็วต่างกันเพื่อสร้างมิติภาพยนตร์ |
| **Frame Scrubbing** | การหยุดการรันแบบ real-time (`tl.pause()`) แล้วสั่งเลื่อนหัวอ่านตามเฟรม (`tl.seek(frame / fps)`) เพื่อให้ Remotion เรนเดอร์วิดีโอแบบ Frame-Accurate 100% |

---

## ⚡ 2. Hard Physics Rules & Anti-Slop Guardrails

1. **Transform Properties Only:**
   - ใช้งานเฉพาะ: `x`, `y`, `scale`, `rotation`, `skewX`, `skewY`, และ `autoAlpha`
   - **ห้ามเด็ดขาด:** ห้ามทำแอนิเมชัน `top`, `left`, `margin`, `padding`, `width`, `height` เพราะทำให้เกิด Browser Layout Thrashing
2. **Anatomical Pivot Points & Joint Overlap Caps:**
   - สำหรับชิ้นส่วนข้อต่อ ต้องกำหนด `transformOrigin` ให้ตรงกับจุดหมุนทางกายวิภาคจริง:
     - คอ / ฐานกะโหลก: `transformOrigin: "50% 90%"` (ไม่อยู่กลางหัว)
     - หัวไหล่: `transformOrigin: "15% 15%"` (ไม่อยู่กลางท่อนแขน)
     - ข้อศอก: `transformOrigin: "15% 15%"` (ที่ปุ่มกระดูกข้อศอก)
     - ข้อมือ: `transformOrigin: "15% 15%"` (ที่รอยต่อฝ่ามือ)
   - **Joint continuity:** รอยต่อและจุดหมุนต้องต่อเนื่อง; caps/ระยะซ้อนเป็นวิธีเฉพาะของ asset บางแบบ ไม่ใช่ข้อกำหนดกายวิภาคหรือเปอร์เซ็นต์ตายตัว ใช้พิกัด pivot จาก asset จริง
3. **Biomechanical Joint Limits (ห้ามฝืนกายวิภาค):**
   - กำหนดแกนและขอบเขตของ rig จริง รักษาความยาวกระดูกและแก้ IK ภายในระยะที่เอื้อมถึง แยก perspective/การหมุนสามมิติออกจากข้อหลุดหรือหักผิดแกน
   - ใช้ช่วงกำกับตัวอย่างใน animation-principles ตามประเภทงาน ไม่ตีความทิศบนจอหรือเลของศาชุดเดียวเป็นขีดจำกัดทางคลินิกของทุกคน
4. **Energy Propagation in Kinetic Chains (การส่งผ่านพลังงานในข้อต่อ):**
   - เลือกการนำ/ตามจากแรงและข้อจำกัดจริง ไม่บังคับ delay เดียวให้ทุกข้อ มือกับวัตถุที่จับแน่นต้องรักษา grip offset ระหว่างเคลื่อน; ส่วนผมหรือผ้าที่หลวมอาจมี follow-through
   - Read [production-practice.md](../animation-principles/references/production-practice.md) for support, rig space, timing and temporal review before animating a difficult action.

---

## 🎬 3. Remotion Integration Formula (Deterministic Video)

นี่คือโครงสร้างมาตรฐานในการนำ GSAP มาใช้ในเทมเพลต Remotion ของ BigO Content Studio เพื่อเรนเดอร์ออกเป็น MP4 ได้อย่างราบรื่น:

```tsx
import React, { useLayoutEffect, useRef } from "react";
import { useCurrentFrame, useVideoConfig } from "remotion";
import gsap from "gsap";

export const GsapRemotionScene: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const containerRef = useRef<HTMLDivElement>(null);
  const timelineRef = useRef<gsap.core.Timeline | null>(null);

  useLayoutEffect(() => {
    const ctx = gsap.context(() => {
      // 1. กฎเหล็ก: ต้อง paused: true เพื่อไม่ให้ GSAP รัน RAF แย่งกับ Remotion
      const tl = gsap.timeline({ paused: true });

      // 2. Kinetic Chain Timeline (ส่งแรงจากต้นแขนสู่ปลายนิ้ว)
      tl.to(".upper-arm", {
        rotation: -45,
        duration: 0.6,
        ease: "power2.out",
      })
      .to(".forearm", {
        rotation: 35, // งอศอกตามกายวิภาค
        duration: 0.5,
        ease: "power2.out",
      }, "<0.08") // หน่วงตามหลังไหล่ 80ms
      .to(".hand", {
        rotation: 20, // ข้อมือสะบัดตามแรงส่ง
        duration: 0.4,
        ease: "back.out(1.5)",
      }, "<0.06");

      timelineRef.current = tl;
    }, containerRef);

    return () => ctx.revert();
  }, []);

  // 3. ขับเคลื่อนเวลาตามเฟรมของ Remotion แบบ Deterministic: seek หลัง DOM พร้อมทุกเฟรม
  //    (รวมถึงตอน mount ใหม่ระหว่างเรนเดอร์หลายแท็บ) ห้าม seek ระหว่าง render เพราะ timeline ยังไม่มีในเฟรมแรก
  useLayoutEffect(() => {
    timelineRef.current?.seek(frame / fps);
  }, [frame, fps]);

  return (
    <div ref={containerRef} style={{ width: "100%", height: "100%", position: "relative" }}>
      {/* Renders hierarchical SVGs / PNG layers */}
    </div>
  );
};
```

---

## 🦴 4. 2D Cutout Rigging Architecture

ลำดับชั้นโครงกระดูก (Kinematic Hierarchy) และจุดหมุน (Pivots):

```
Character Root (Base x, y)
 ├── Contact Shadow (Scale & opacity tied to Torso Y)
 └── Torso (CoM Pivot: 50% 85%) [Squash & Stretch: Sy, Sx = 1/√Sy]
      ├── Head (Pivot: 50% 95% at Neck C7)
      │    ├── Facial Features (Nose, Brows, Ears)
      │    ├── Eyes (Blink animation)
      │    └── Mouth (Speech phonemes)
      ├── Arm_L (Behind Torso, Pivot: 20% 15% at Glenohumeral Joint)
      │    └── Forearm_L (Pivot: 15% 15% at Olecranon Elbow)
      │         └── Hand_L (Pivot: 15% 20% at Carpal Wrist)
      ├── Arm_R (Front of Torso, Pivot: 80% 15% at Shoulder)
      │    └── Forearm_R (Pivot: 85% 15% at Elbow)
      │         └── Hand_R (Pivot: 85% 20% at Wrist)
      ├── Thigh_L (Pivot: 35% 10% at Femoral Head)
      │    └── Shin_L (Pivot: 20% 10% at Patella Knee)
      │         └── Foot_L (Pivot: 20% 40% at Ankle)
      └── Thigh_R (Pivot: 65% 10% at Femoral Head)
           └── Shin_R (Pivot: 80% 10% at Knee)
                └── Foot_R (Pivot: 80% 40% at Ankle)
```

### ฟิสิกส์การซ้อนทับของข้อต่อ (Seam Masking):
เพื่อไม่ให้มองเห็นรอยต่อที่แตกออกจากกันเมื่อท่อนแขนหมุน:
- ปลายบนของ `Forearm` ต้องทำเป็นรูปครึ่งวงกลม (Radius = ครึ่งหนึ่งของความกว้างแขน)
- ปลายล่างของ `Upper Arm` ทำเป็นเบ้าครอบที่มีขนาดเท่ากัน
- เมื่อหมุนรอบจุดกึ่งกลางของวงกลมนั้น รอยต่อจะคงความกลมกลืนและแนบสนิท $100\%$ เสมอ

---

## ⚖️ 5. Physics-Informed Harmonic Oscillation Formula

เมื่อขยับชิ้นส่วนแบบลูป (เช่น การหายใจ, ชายผ้าสะบัด, การทรงตัว) ห้ามใช้ฟังก์ชัน `Math.sin()` เพียว ๆ โดยไม่มีการสลายแรง ให้ใช้ **Damped Harmonic Motion**:

$$y(t) = A \cdot e^{-\gamma t} \cdot \cos(\omega t - \phi)$$

โดยที่:
- $A$: แอมพลิจูดเริ่มต้น
- $\gamma$: ค่าสัมประสิทธิ์การหนืด (Damping factor) $\approx 0.3–0.6$
- $\omega$: ความถี่เชิงมุม $\omega = 2\pi f$
- $\phi$: เฟสหน่วงตามความยาวของชิ้นส่วน (Phase lag)
