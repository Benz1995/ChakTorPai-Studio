---
name: remotion-best-practices
description: "Remotion engineering rules for BigO templates: deterministic rendering, interpolate clamping, springs, calculateMetadata, asset loading, layer compositing and sprite sheets. Use when writing or reviewing Remotion code in content-studio; motion-remotion owns the project workflow and file locations."
---

# Remotion Best Practices — Official Video Engineering & Compositing

Standardized best practices distilled from the official `remotion-dev/skills` repository. Ensures all Remotion templates, scenes, and media exports in BigO Content Studio are 100% deterministic, free from visual glitches, and performant during headless rendering.

---

## 🔒 1. The Fundamental Law: Deterministic Rendering

วิดีโอไม่ใช่ Web Application ทั่วไป — วิดีโอใน Remotion คือลำดับของรูปภาพนิ่งที่ถูกเรนเดอร์ทีละเฟรม:

1. **ห้ามใช้เวลาในโลกจริง:** ห้ามใช้ `Date.now()`, `new Date()`, หรือ `performance.now()` ในการคำนวณตำแหน่งหรือความเคลื่อนไหว
2. **ห้ามใช้ Unseeded Randomness:** ห้ามใช้ `Math.random()` สุ่มค่า เพราะเฟรมที่ 5 กับเฟรมที่ 5 เมื่อเรนเดอร์ซ้ำจะได้ค่าไม่เหมือนกัน! ให้ใช้ seeded PRNG หรือ derive ค่าจาก `frame` เสมอ (เช่น `Math.sin(frame * 0.1)`)
3. **ห้ามใช้ Pure CSS Transitions:** หลีกเลี่ยง `transition: all 0.3s ease` บนเบราว์เซอร์ เพราะใน headless render เวลาของ CSS transition ไม่ sync กับ frame step ของ Remotion ให้คำนวณผ่าน `interpolate()` หรือ `spring()` เสมอ

---

## 🎚️ 2. The `interpolate()` Clamping Rule (กฎเหล็ก)

เมื่อใช้ `interpolate()` จาก Remotion ต้องใส่ `extrapolateLeft` และ `extrapolateRight` เป็น `"clamp"` เสมอ เว้นแต่จะมีเจตนาต้องการให้ค่าขยายออกนอกช่วงจริง ๆ:

```tsx
import { interpolate } from "remotion";

// ❌ อันตราย: ค่า opacity อาจทะลุเกิน 1 หรือติดลบ ทำให้เบราว์เซอร์เรนเดอร์เพี้ยน
const opacity = interpolate(frame, [0, 30], [0, 1]);

// ✅ ถูกต้อง: ปลอดภัย ไม่ว่าจะ seek ไปเฟรมที่ -10 หรือเฟรมที่ 500
const opacity = interpolate(frame, [0, 30], [0, 1], {
  extrapolateLeft: "clamp",
  extrapolateRight: "clamp",
});
```

---

## 🏎️ 3. Spring Physics Best Practices

ใช้ `spring()` เมื่อต้องการความนุ่มนวลแบบฟิสิกส์:

```tsx
import { spring, useCurrentFrame, useVideoConfig } from "remotion";

const frame = useCurrentFrame();
const { fps } = useVideoConfig();

const scale = spring({
  frame,
  fps,
  config: {
    damping: 12,    // ความหนืด (ยิ่งมากยิ่งหยุดเร็ว)
    mass: 0.5,      // มวล (ยิ่งน้อยยิ่งเบาและเร็ว)
    stiffness: 100, // ความแข็งของสปริง
    overshootClamping: false, // true ถ้าไม่ต้องการให้มีจังหวะเด้งเลย
  },
});
```

---

## ⏱️ 4. Dynamic Duration with `calculateMetadata`

ห้ามฮาร์ดโค้ดความยาวเฟรมเมื่อเทมเพลตต้องรองรับเสียงพากย์หรือเพลงที่มีความยาวเปลี่ยนแปลงได้:

```tsx
import { CalculateMetadataFunction } from "remotion";

export const calculateMyVideoMetadata: CalculateMetadataFunction<MyProps> = async ({
  props,
}) => {
  // ดึงความยาวเสียงพากย์จริง
  const audioDurationInSeconds = props.audioDuration ?? 15;
  const fps = 30;
  const paddingFrames = 30; // 1 วินาทีตอนจบคลิป

  return {
    durationInFrames: Math.ceil(audioDurationInSeconds * fps) + paddingFrames,
    fps,
    width: props.aspectRatio === "9:16" ? 1080 : 1920,
    height: props.aspectRatio === "9:16" ? 1920 : 1080,
  };
};
```

---

## 🖼️ 5. Asset Preloading with `delayRender()` & `continueRender()`

เพื่อป้องกันไม่ให้เฟรมแรก ๆ แวบ (Flicker) เพราะรูปภาพหรือฟอนต์ยังโหลดไม่เสร็จใน Headless Chromium:

- รูปใน JSX ให้ใช้ `<Img>` จาก `remotion` (และ `<OffthreadVideo>`/`<Audio>` สำหรับสื่อ) ซึ่งรอโหลดให้อัตโนมัติ ไม่ต้องเขียน `delayRender()` เอง
- ใช้ `delayRender()`/`continueRender()` เองเฉพาะ asset ที่ไม่ใช่ element เช่น ฟอนต์, JSON, texture ของ canvas/WebGL ตามตัวอย่างนี้ และเรียก `cancelRender(err)` เมื่อโหลดไม่สำเร็จ แทนที่จะปล่อยให้เรนเดอร์ภาพว่าง

```tsx
import { cancelRender, continueRender, delayRender, staticFile } from "remotion";
import { useEffect, useState } from "react";

export const SafeImageScene: React.FC = () => {
  const [handle] = useState(() => delayRender("Loading hero asset"));

  useEffect(() => {
    const img = new Image();
    img.src = staticFile("character-body.png");
    img.onload = () => {
      continueRender(handle); // ปลดล็อคให้ Remotion เริ่มเรนเดอร์เฟรมได้
    };
    img.onerror = () => {
      cancelRender(new Error("Failed to load character-body.png"));
    };
  }, [handle]);

  return <img src={staticFile("character-body.png")} />;
};
```

---

## 🎞️ 6. Compositing & Layer Architecture

เมื่อรวมหลายเลเยอร์ (Compositing) ใน Remotion:

```tsx
import { AbsoluteFill, Sequence, Audio, staticFile } from "remotion";

export const CompositedMasterScene: React.FC = () => {
  return (
    <AbsoluteFill style={{ backgroundColor: "#0f172a" }}>
      {/* Layer 1: Background & 2.5D Ambience */}
      <AbsoluteFill style={{ zIndex: 1 }}>
        <BackgroundParallaxLayer />
      </AbsoluteFill>

      {/* Layer 2: Main 2D Cutout Character / Assets */}
      <AbsoluteFill style={{ zIndex: 2 }}>
        <CutoutCharacterRig />
      </AbsoluteFill>

      {/* Layer 3: Foreground Debris & Overlays */}
      <AbsoluteFill style={{ zIndex: 3, pointerEvents: "none" }}>
        <CinematicLightingOverlay />
      </AbsoluteFill>

      {/* Layer 4: Captions & UI Safe-Zone Overlays */}
      <AbsoluteFill style={{ zIndex: 4 }}>
        <SafeZoneCaptions />
      </AbsoluteFill>

      {/* Layer 5: Synchronized Audio Tracks */}
      <Audio src={staticFile("voiceover.mp3")} volume={1.0} />
      <Audio src={staticFile("bgm.mp3")} volume={0.15} />
    </AbsoluteFill>
  );
};
```

---

## 🎞️ 7. Frame-by-Frame Animation (Sprite Sheet)

สำหรับการทำ Frame-by-Frame Animation จากรูปเรียงเฟรมหรือ Sprite Sheet:

```tsx
import { useCurrentFrame } from "remotion";

interface SpriteProps {
  sheetUrl: string;
  totalFrames: number;
  frameWidth: number;
  frameHeight: number;
  fpsDivider?: number; // ตัวหารเฟรม เช่น 2 = ขยับทุก ๆ 2 เฟรม (On Twos)
}

export const SpriteAnimation: React.FC<SpriteProps> = ({
  sheetUrl,
  totalFrames,
  frameWidth,
  frameHeight,
  fpsDivider = 2,
}) => {
  const frame = useCurrentFrame();
  const currentSprite = Math.floor(frame / fpsDivider) % totalFrames;

  return (
    <div
      style={{
        width: frameWidth,
        height: frameHeight,
        backgroundImage: `url(${sheetUrl})`,
        backgroundPosition: `-${currentSprite * frameWidth}px 0px`,
        backgroundRepeat: "no-repeat",
      }}
    />
  );
};
```
