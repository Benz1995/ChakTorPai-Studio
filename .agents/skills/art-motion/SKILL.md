---
name: art-motion
description: "Direct art styles and storytelling grammars for code-driven animation: 35 art style cards, 9 visual explainer grammars (Kurzgesagt, Vox, 3Blue1Brown, etc.) and automated QC. Use when choosing or critiquing the look of a code-made explainer or motion graphic (สไตล์ภาพ, แนวภาพ, สไตล์การเล่า), or when graphics look generic or slide-like; GPT-illustrated narratives use gpt-motion-story."
---

# Art Motion — 35 Art Styles & 9 Storytelling Grammars (Huashu Art Motion)

Code-driven art direction and visual storytelling grammar for AI coding agents. Transforms scripts, concepts, and voiceovers into distinctive artistic animations using SVG, Canvas, WebGL, and Remotion/Playwright headless rendering.

For production-quality work or rejected simplistic graphics, use the art-direction
and exercise sections in [production-practice.md](../animation-principles/references/production-practice.md).
The style catalogue below is a vocabulary, not a quality certificate. Choose a
coherent visual proposition, design the assets, and review a moving proof before
batching. A style name or borrowed motion preset does not establish professional craft.

---

## 🎨 1. The 35 Art Style Cards

เลือกสไตล์ภาพให้สอดคล้องกับเรื่องเล่าและอารมณ์ของช่อง:

### หมวดที่ 1: ประวัติศาสตร์และศิลปะคลาสสิก (Historical & Classical)
1. **Cave Paintings (ศิลปะถ้ำ):** โทนสีดินแดง โอเคอร์ ถ่านหิน พื้นผิวผนังหินขรุขระ ลายเส้นหยาบ ขยับแบบตัดเฟรมกระตุก (On Threes)
2. **Ancient Egyptian (อียิปต์โบราณ):** มุมมองแบบ Profile ด้านข้าง สีทอง ลาพิสลาซูลี และเทอร์ควอยซ์ ลวดลายอักษรไฮโรกลิฟิก
3. **Ukiyo-e (ภาพพิมพ์แกะไม้ญี่ปุ่น):** เส้นหมึกคมชัด คลื่นสึนามิ สีกรมท่า เบจ แดงชาด ลวดลายกระดาษวาชิ
4. **Impressionism / Monet (อิมเพรสชันนิสม์):** แปรงแต้มสี แสงสะท้อนผิวน้ำ โทนสีพาสเทลละมุน แอนิเมชันแบบสั่นไหวเล็กน้อย (Wobble)
5. **Van Gogh (โพสต์อิมเพรสชันนิสม์):** ลายแปรงหมุนวน (Swirl) สเปกตรัมสีเหลืองทองและน้ำเงินเข้ม การเคลื่อนไหวแบบไหลวนตลอดเวลา
6. **Munch / Expressionism (เอ็กซ์เพรสชันนิสม์):** คลื่นเส้นสายบิดเบี้ยว ถ่ายทอดความวิตกกังวลหรือลึกลับ สีส้มเพลิงและฟ้ามืด
7. **Bauhaus & De Stijl:** รูปทรงเรขาคณิตบริสุทธิ์ (สี่เหลี่ยม วงกลม สามเหลี่ยม) แม่สีหลัก (แดง เหลือง น้ำเงิน) ขาว ดำ
8. **Art Deco:** ลวดลายเส้นเรขาคณิตสีทองหรูหรา สมมาตร แสงสะท้อนโลหะทองเหลือง
9. **Dali / Surrealism (สัจนิยมเหนือจริง):** นาฬิกาละลาย ท้องฟ้าเวิ้งว้าง มิติบิดเบี้ยว
10. **Pop Art / Warhol & Lichtenstein:** ลายจุด Ben-Day dots, ขอบเส้นดำหนา, สีสะท้อนแสงนีออนจัดจ้าน

### หมวดที่ 2: อนิเมะและศิลปะตะวันออก (Anime & Asian Aesthetics)
11. **Studio Ghibli (จิบลิสไตล์):** ท้องฟ้าสีครามเมฆปุยขาว ทุ่งหญ้าสีเขียวสด ลมพัดระลอกคลื่น ความอบอุ่นในวัยเยาว์
12. **Makoto Shinkai (ชินไคสไตล์):** แสงแฟลร์สะท้อนเลนส์ (Lens flare), ละอองฝน, เงาสะท้อนกระจก, ท้องฟ้ายามเย็นสีม่วงทอง
13. **Dunhuang Murals (จิตรกรรมฝาผนังตุนหวง):** นางอัปสรเหินเวหา ริบบิ้นลอยพลิ้ว สีเขียวมรกตและสีส้มแสด
14. **Chinese Ink Wash (ภาพวาดพู่กันจีน):** หมึกซึมบนกระดาษข้าว การเว้นวรรคช่องว่าง (Negative space) การเคลื่อนไหวช้าเนิบ
15. **90s Retro Anime:** ลายเส้นปากกาหมึกซึม ขอบภาพเบลอเล็กน้อย (Chromatic aberration), เกรนฟิล์มอนาล็อก

### หมวดที่ 3: ศิลปะร่วมสมัยและดิจิทัล (Modern & Digital Art)
16. **Cyberpunk & Synthwave:** นีออนชมพู-ฟ้าไซอัน กริดเส้น 3D เรโทร ทิวทัศน์เมืองยามค่ำคืน
17. **Papercut 2.5D (งานกระดาษฉลุ):** เลเยอร์กระดาษซ้อนชั้นพร้อมเงาตกกระทบ (Drop shadows) มิติความลึกชัดเจน
18. **Claymation / Plasticine (แอนิเมชันดินน้ำมัน):** พื้นผิวลายนิ้วมือ ขอบโค้งมน ขยับทีละ 2-3 เฟรม ให้ความรู้สึก Hand-made
19. **Low-Poly 3D:** รูปทรงเหลี่ยมเรขาคณิต แสงเงาแบนเรียบแบบ Flat-shaded
20. **Vaporwave:** รูปปั้นกรีกโบราณ วินโดวส์ 95 ต้นปาล์ม และโทนสีพาสเทลม่วงพีช
21. **Isometric Vector:** มุมมอง 30 องศา สะอาดตา แม่นยำ เหมาะกับเทคโนโลยีและสถาปัตยกรรม
22. **Pixel Art (16-bit):** พิกเซลคมชัด คอนทราสต์สูง ให้ความรู้สึกเกมย้อนยุค
23. **Risograph Print:** สีหมึกทับซ้อน (Overprint misregistration), ลายจุดเม็ดสี, เท็กซ์เจอร์กระดาษหนังสือพิมพ์
24. **Linocut & Woodcut (ภาพพิมพ์ยาง/ไม้):** ขาวดำตัดกันรุนแรง รอยแกะเนื้อไม้ที่หยาบและดุดัน
25. **Chalkboard Art (ชอล์กกระดานดำ):** ฝุ่นชอล์กฟุ้งกระจาย เส้นร่างสีขาวบนพื้นกระดานดำ
26–35. **Glitch Art, Watercolor Bleed, Blueprint Drafting, Comic Half-tone, Minimalist Line Art, Stained Glass, Gouache Botanical, Collage Scrapbook, Dark Fantasy Gothic, และ Bioluminescent Deep Sea.**

---

## 📐 2. The 9 Visual Storytelling Grammars

เมื่อต้องผลิตวิดีโออธิบายเรื่อง (Explainer) ให้เลือก 1 ใน 9 ไวยากรณ์นี้เป็นแกนหลัก:

### 1. Kurzgesagt Style (Flat Vector Cosmic & Science)
- **จุดเด่น:** ลายเส้นเวกเตอร์แบนเรียบสดใส ขอบมน นกเป็ดน้ำ/มาสคอต สีพื้นหลังอิ่มตัวสูง (Saturated)
- **การเคลื่อนไหว:** กล้อง Zoom-in และ Zoom-out จากระดับอะตอมสู่ระดับจักรวาล, Spring bounce นุ่มนวล, วัตถุลอยเป็นอิสระ

### 2. Vox Style (Visual Journalism & Documentary)
- **จุดเด่น:** สไตล์ภาพตัดแปะ (Collage), รูปถ่ายประวัติศาสตร์ผสมกราฟิก, ปากกาไฮไลท์สีเหลืองขีดข้อความ, แผนที่พร้อมหมุดและเส้นทาง
- **การเคลื่อนไหว:** กระดาษฉีกขาด (Paper tear reveal), การหมุนและวางภาพถ่ายซ้อนกันอย่างรวดเร็ว, แว่นขยายส่องเอกสาร

### 3. 3Blue1Brown Style (Mathematical & Systematic Geometry)
- **จุดเด่น:** พื้นหลังสีเทาเข้มเกือบดำ กริดพิกัดแกน X-Y สูตรคณิตศาสตร์ (LaTeX) และเวกเตอร์เรขาคณิต
- **การเคลื่อนไหว:** การแปลงรูปพิกัด (Linear transformation), กราฟเส้นที่วาดต่อยอดอย่างนุ่มนวล, ลูกศรชี้เวกเตอร์หมุนรอบจุดกำเนิด

### 4. Whiteboard & Sketch Doodle (ภาพสเก็ตช์กระดานขาว)
- **จุดเด่น:** พื้นหลังสีขาวลายกระดาน ปากกาเมจิกสีดำ น้ำเงิน แดง
- **การเคลื่อนไหว:** การขีดเส้นตาม Path (Stroke-dashoffset animation), รอยลบแปรง และมือจำลองที่วาดองค์ประกอบขึ้นมา

### 5. Product Keynote / Apple Style (โมเดิร์นเทคโนโลยี)
- **จุดเด่น:** ตัวเครื่องอุปกรณ์โปร่งแสง กระจกฝ้า (Glassmorphism), แสงส่องกระทบขอบมุม (Specular highlights)
- **การเคลื่อนไหว:** การลอยตัวในอวกาศแบบ Smooth float, การหมุน 3D Isometric เล็กน้อย, ข้อความหัวข้อยักษ์ที่ Fade ขึ้นมา

### 6. Financial & Data Storytelling (เศรษฐกิจและข้อมูล)
- **จุดเด่น:** แท่งเทียน Candlestick, กราฟพื้นที่แบบไล่ระดับสี, ตัวเลขนับขึ้นรวดเร็ว (Ticker counter)
- **การเคลื่อนไหว:** กราฟพุ่งทะลุแนวต้าน, เส้นแนวโน้มสะบัด, การขยายกล่องข้อมูลเปรียบเทียบ

### 7. Cinematic 2.5D Parallax Narrative (เรื่องเล่าเชิงภาพยนตร์)
- **จุดเด่น:** ฉากหน้า (Foreground) เบลอเล็กน้อย, ตัวละครอยู่ระยะกลาง, ทัศนียภาพกว้างใหญ่ในฉากหลัง
- **การเคลื่อนไหว:** กล้องดอลลี่เคลื่อนที่ช้า ๆ (Slow push-in), ฝุ่นละอองหรือหิมะลอยผ่านหน้าเลนส์

### 8. Kinetic Typography (ตัวอักษรขับเคลื่อนจังหวะ)
- **จุดเด่น:** ตัวอักษรตัวหนาขนาดใหญ่ สลับขนาดคำตามการเน้นเสียงพากย์
- **การเคลื่อนไหว:** สั่นกระแทกตามจังหวะเบส (Bass pulse), ตัวอักษรไหลตามทิศทางลม, การตัดคำแบบ Frame-accurate

### 9. Storybook & Watercolor (หนังสือนิทานภาพวาด)
- **จุดเด่น:** หน้ากระดาษพับเปิด (Page turn), สีน้ำซึมตามขอบ, ตัวละครแบบหุ่นกระดาษตัด
- **การเคลื่อนไหว:** ข้อต่อขยับแบบ 2D Cutout ช้า ๆ, หมอกควันสีน้ำจางหาย, การซูมเข้าไปในกรอบรูป

---

## 🔍 3. Automated Quality Control & Physics Reality Gate (QC Checklist)

ใช้รายการนี้ประกอบการตรวจภาพและช่วงเคลื่อนไหวจริง ไม่ใช่การรับประกันความสมจริงจากคะแนนอัตโนมัติ:

1. **Biomechanical & Joint Integrity:** ตรวจความต่อเนื่องของรอยต่อ ความยาวแขนขา และข้อจำกัดของ rig ตามมุมกล้องจริง; แยก perspective/การหมุนสามมิติออกจากข้อหลุด ไม่ใช้ทิศบนหน้าจอเป็นเกณฑ์กายวิภาคตายตัว
2. **Support & Contact:** ตรวจพื้น มือ ที่นั่ง หรือ constraint ที่รับน้ำหนัก รวมถึงการไถลและการทะลุวัตถุ เงาต้องสัมพันธ์กับแสงเมื่อเห็นได้ ไม่ตัดสินการลอยจากเงาที่หายไปเพียงอย่างเดียว
3. **Kinetic Chain:** ให้การส่งแรงและ secondary motion สัมพันธ์กับข้อต่อ วัสดุและ constraint; มือกับอุปกรณ์ที่จับแน่นอาจเคลื่อนพร้อมกัน ผม/ผ้าที่หลวมอาจตามช้า ไม่บังคับทุกส่วนให้มี delay เสมอ
4. **Shape and Volume:** รักษารูปทรงและ identity ของวัตถุ ใช้ squash/stretch เฉพาะสไตล์ที่ตั้งใจ; $S_x S_y=1$ รักษาพื้นที่สองมิติ ส่วนปริมาตรสามมิติคือ $S_x S_y S_z=1$ ไม่ใช่การรับประกันมวลหรือกายวิภาค
5. **Directed Rhythm:** ช่วงเตรียม ลงมือ สัมผัส ผ่อนแรง และพักต้องช่วยอ่านเหตุการณ์ ความนิ่งที่มีเหตุผลใช้ได้ ไม่เติม ambient movement เพื่อหลบเกณฑ์เวลา และไม่ใช้ pixel difference เป็นหลักฐานว่าดูน่าสนใจ
6. **Readability & Contrast:** ข้อความบรรยายต้องมีคอนทราสต์ไม่ต่ำกว่า 4.5:1 เทียบกับพื้นหลัง
7. **Continuity:** ตรวจความเร็ว ความเร่ง การหยุดและรอยตัดตามเจตนา; การกระแทกอาจเปลี่ยนความเร็วฉับพลันได้ แต่ teleport หรือรอยต่อพิกัดผิดต้องแก้ ไม่ใช้ easing เดียวกับทุกเหตุการณ์
8. **Anti-Slop Aesthetic:** ปฏิเสธรูปทรงเด็กอนุบาล (ห้ามใช้สี่เหลี่ยมแปะวงกลมดิบ ๆ) งานออกแบบต้องมีรูปทรงสรีระและเส้นสายระดับมืออาชีพ
