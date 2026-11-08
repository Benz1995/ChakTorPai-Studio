---
name: campaign-matrix
description: "Build an ad campaign matrix in Content Studio from one structured brief (POST /api/contents/:id/campaign-matrix and contact-sheet): 18 deliverables (3 hooks × 3 aspect ratios × 2 CTAs) with analytical closed-form springs, decoupled motion math and a 5-pass QC pipeline with FFmpeg contact sheets. Use for a multi-variant ad campaign (แคมเปญโฆษณา, หลายเวอร์ชัน, A/B hook); single KinJi Shopee clips use shopee-affiliate."
---

# Campaign Matrix — Automated Programmatic Motion Design

Adapted from the automated motion-design method shared by VFX supervisor **@e1genqq** (notes: `content-studio/docs/automated-motion-system-eigen.md`), this skill turns BigO Content Studio into an automated commercial-grade motion campaign generator.

Instead of treating motion design as isolated manual keyframing or unpredictable generative AI video, this system models video as **deterministic code** (`seek(t)` frame math) driven by a structured brief. A single timeline compiles into **18 client-ready campaign deliverables** across 3 hooks, 3 aspect ratios, and 2 CTAs.

---

## The 6-Pillar Architecture

```
┌────────────────────────────────────────────────────────┐
│  Pillar 1: Structured Brief Compiler (campaign.json)   │
│  Brand safe zones • Strict anti-hallucination guard    │
└───────────────────────────┬────────────────────────────┘
                            ▼
┌────────────────────────────────────────────────────────┐
│  Pillar 2: Expensive-Motion Engine                     │
│  Closed-form springs • Edge asymmetry • Decoupled text │
└───────────────────────────┬────────────────────────────┘
                            ▼
┌────────────────────────────────────────────────────────┐
│  Pillar 3: Deterministic seek(t) Frame Clock           │
│  uTime = frame / fps • Seeded PRNG • Bit-identical     │
└───────────────────────────┬────────────────────────────┘
                            ▼
┌────────────────────────────────────────────────────────┐
│  Pillar 4: 5-Pass Automated QC + FFmpeg Contact Sheet  │
│  Layout • Timing • Mobile Legibility • Brand • 4x4 Grid│
└───────────────────────────┬────────────────────────────┘
                            ▼
┌────────────────────────────────────────────────────────┐
│  Pillar 5: Campaign Matrix (18 Deliverables)           │
│  3 Hooks × 3 Ratios (9:16, 1:1, 16:9) × 2 CTAs        │
└───────────────────────────┬────────────────────────────┘
                            ▼
┌────────────────────────────────────────────────────────┐
│  Pillar 6: Commercial Delivery & Ad Platform Handoff   │
│  campaign-manifest.json • Direct Response Ready        │
└────────────────────────────────────────────────────────┘
```

---

## 1. Pillar 1: Structured Brief & Anti-Hallucination Compiler

Never generate animations from unstructured prose or vague prompts. Video briefs are compiled into typed data structures:

```typescript
interface CampaignBrief {
  id: string;
  brand: {
    name: string;
    primaryColor: string;
    secondaryColor: string;
    fontFamily: string;
    safeZonePadding: number; // e.g. 80px for TikTok/Reels UI overlay
  };
  matrix: {
    hooks: [
      { type: 'problem'; text: string; subtext?: string },
      { type: 'result';  text: string; subtext?: string },
      { type: 'feature'; text: string; subtext?: string }
    ];
    body: {
      headline: string;
      features: string[];
      proofMetric?: { value: string; label: string };
    };
    ctas: [
      { type: 'direct'; text: string; urlText?: string },
      { type: 'value';  text: string; discountCode?: string }
    ];
  };
  settings: {
    fps: 30;
    durationInFrames: 300; // 10 seconds
  };
}
```

### ⚠️ Strict Anti-Hallucination Guardrail
- If the brief does not provide numerical statistics (e.g., "78% faster", "10k+ users"), the engine **MUST NOT invent numbers**. 
- Omit missing metrics or replace with qualitative benefits rather than generating plausible-sounding fake metrics.

---

## 2. Pillar 2: "Expensive-Looking" Motion Math

Avoid default linear or arbitrary cubic-bezier transitions. The `@e1genqq` framework dictates three mathematical rules for motion that looks high-end:

### Rule 2.1 — Analytical Closed-Form Springs
Evaluate motion at arbitrary time $t$ independently:
```typescript
import { closedFormSpring } from '../src/remotion/library/expensive-motion';

// Critically damped or slight overshoot closed-form spring:
// x(t) = 1 - exp(-omega * t) * (1 + omega * t)
const scale = closedFormSpring(t, 14, 0.08); // omega = 14 rad/s, 8% bounce
```

### Rule 2.2 — Leading vs. Trailing Edge Asymmetry
Containers stretch as they accelerate and compress as they settle. The leading edge (width expansion) moves before the trailing edge (settling back):
```typescript
import { useEdgeAsymmetry } from '../src/remotion/library/expensive-motion';

const { stretchScaleX, settleProgress } = useEdgeAsymmetry(frame, fps, 15);
// Gives organic physical stretch without expensive physics simulation
```

### Rule 2.3 — Decoupled Container & Typography Timing
Typography must **never** animate into a bounding box while the box is still resizing, otherwise text wraps erratically and looks amateur:
```tsx
import { DecoupledContainer } from '../src/remotion/library/expensive-motion';

<DecoupledContainer
  startFrame={15}
  minThreshold={0.7} // Content enters only after box is 70% expanded
  containerStyle={{ background: '#1e1b4b', borderRadius: 24, padding: 32 }}
>
  <h1 className="font-bold text-white text-3xl">High Converting Hook</h1>
</DecoupledContainer>
```

---

## 3. Pillar 3: Deterministic `seek(t)` Engine

- **Single Clock Source:** `uTime = frame / fps`.
- **Zero Live Non-Determinism:** Never use `Math.random()` inside components. If procedural variation is needed, use seeded hash:
  ```typescript
  function seededRandom(seed: number) {
    const x = Math.sin(seed++) * 10000;
    return x - Math.floor(x);
  }
  ```
- Any frame on any render node can be requested out of order (`frame 45` then `frame 12`) and yields bit-identical output.

---

## 4. Pillar 4: The 5-Pass Automated QC Protocol

Before any render is exported to a client, it must pass 5 automated and visual quality gates:

| Pass | Phase | Criteria | Automated Tool / Verification |
| --- | --- | --- | --- |
| **Pass 1** | Storyboard / Static | No text clipping, padding ≥ safeZone (80px), zero NaN transforms | Layout bounds check |
| **Pass 2** | Motion / Timing | Spring duration ≤ 25 frames, no motion overlaps with scene cuts | Velocity graph inspection |
| **Pass 3** | Mobile Legibility | Downscale to 360px wide; main headline readable in < 1 second | Visual test at 360×640 |
| **Pass 4** | Brand Compliance | Contrast ratio ≥ 4.5:1, exact hex matches, logo safe zones intact | Color contrast check |
| **Pass 5** | Video Contact Sheet | 16-frame 4×4 contact sheet of the full video timeline | `POST /api/contents/:id/contact-sheet` |

### Automated FFmpeg Contact Sheet Command:
```bash
ffmpeg -i input.mp4 -vf "fps=0.5,scale=360:-1,tile=4x4" -frames:v 1 contact_sheet.png
```
This generates a single 16-tile overview image showing the complete story arc at a glance.

---

## 5. Pillar 5: The 18-Variant Campaign Matrix

A standard campaign exports 18 variations from a single codebase:
- **3 Hooks:**
  1. `problem`: Call out customer pain point ("Still resizing every ad by hand?")
  2. `result`: Lead with tangible outcome ("Turn briefs into 18 video ads in 5 minutes.")
  3. `feature`: Highlight unique capability ("Analytical spring math built into code.")
- **3 Aspect Ratios:**
  1. `9:16` (1080×1920) — TikTok, IG Reels, YouTube Shorts
  2. `1:1` (1080×1080) — Instagram Feed, Facebook Feed, LinkedIn
  3. `16:9` (1920×1080) — YouTube, Desktop Web, TV Ads
- **2 CTAs:**
  1. `direct`: "Tap the basket to see it — link in bio"
  2. `value`: "Get Free Campaign Template"

> **BigO rules:** hooks and CTAs never state prices, discounts or "% off" (Shopee affiliate rule), and
> affiliate campaigns use only the owner's own footage, never seller or review media.

**Matrix Size:** $3 \times 3 \times 2 = 18$ deliverables.

### Generating the Matrix via API:
```bash
curl -X POST http://localhost:3001/api/contents/<CONTENT_ID>/campaign-matrix \
  -H "Content-Type: application/json" \
  -d '{
    "hooks": [
      { "type": "problem", "text": "Are you wasting weeks on video edits?" },
      { "type": "result", "text": "18 production-ready ads in 60 seconds." },
      { "type": "feature", "text": "Code-driven motion with analytical springs." }
    ],
    "ctas": [
      { "text": "Get Instant Access Now" },
      { "text": "Download Free Template" }
    ]
  }'
```

The server writes `storage/campaigns/<CONTENT_ID>/campaign-manifest.json` tracking all 18 deliverables.

---

## 6. How to Run & Verify

1. **Check System Health:**
   ```bash
   node scripts/motion-skills.mjs list
   ```
2. **Build Matrix Manifest:**
   Call `POST /api/contents/:id/campaign-matrix` to generate the 18 variant specs.
3. **Generate Visual Contact Sheet:**
   Call `POST /api/contents/:id/contact-sheet` with `{ "fps": 0.5, "tile": "4x4", "scaleWidth": 360 }`.
4. **Inspect in Playwright Preview:**
   Verify framing, safe zones, and text legibility across all three aspect ratios (`9:16`, `1:1`, `16:9`).
