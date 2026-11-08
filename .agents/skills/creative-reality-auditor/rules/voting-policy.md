# Multi-Agent Voting & Debate Policy (นโยบายการโหวต การโต้แย้ง และอำนาจตัดสิน)

## 1. หลักการ "ความจริงเหนือเสียงส่วนใหญ่" (Truth Over Consensus)
- การโหวต (Voting) มีไว้เพื่อรวบรวมมุมมองทางสุนทรียะและคะแนนประเมินคุณภาพ
- **ข้อเท็จจริง กฎฟิสิกส์ และตรรกะเชิงเหตุผล ไม่สามารถตัดสินด้วยเสียงส่วนใหญ่**
- หากกรรมการ 7 คนโหวตว่า "ผ่าน" เพราะประทับใจบท แต่กรรมการ Reality Judge หรือ Physics Judge มีหลักฐานเชิงประจักษ์ว่ามีข้อผิดพลาดระดับ `CRITICAL` หรือข้อมูลผิดที่ยืนยันได้ งานนั้นต้องถูกส่งกลับไปแก้ไข (`REVISE`)

## 2. ขั้นตอนการโต้แย้ง (The 6-Stage Audit Protocol)

```
[INPUT] 
   ↓
[STAGE 1: CLASSIFY & PROFILE] 
   - กำหนด work_type, world_mode และโหลดค่าน้ำหนัก
   ↓
[STAGE 2: INDEPENDENT REVIEW] 
   - กรรมการแต่ละท่านตรวจงานโดยอิสระ ห้ามเห็นคะแนนของท่านอื่นก่อน
   ↓
[STAGE 3: DEVIL'S ADVOCATE CROSS-EXAMINATION] 
   - Devil's Advocate ตรวจสอบช่องโหว่ ข้อสมมติฐานที่เลื่อนลอย หรือการเออออตามกัน
   - ท้าทายข้อสรุป (Challenge Rounds: จำกัดไม่เกิน 2 รอบ)
   ↓
[STAGE 4: EVIDENCE VERIFICATION] 
   - ตรวจสอบว่าข้อโต้แย้งมีหลักฐานรองรับจริงหรือไม่ คัดกรอง UNVERIFIED
   ↓
[STAGE 5: WEIGHTED SCORING] 
   - คำนวณคะแนนตาม Profile ถ่วงน้ำหนัก
   ↓
[STAGE 6: CHIEF JUDGE SYNTHESIS & FINAL VERDICT] 
   - ออกคำตัดสิน (PASS, PASS_WITH_NOTES, REVISE, REJECT, INSUFFICIENT_EVIDENCE)
   - จัดลำดับ Revision Plan (Minimal Fix First)
```

## 3. เกณฑ์การออกคำตัดสิน (Verdict Criteria)
- **`PASS` (ผ่าน):** คะแนนรวม $\ge 80$, ไม่มีข้อผิดพลาดระดับ HIGH หรือ CRITICAL
- **`PASS_WITH_NOTES` (ผ่านแบบมีข้อสังเกต):** คะแนนรวม $70 - 79$, ไม่มีข้อผิดพลาดระดับ CRITICAL, มีเฉพาะประเด็น MEDIUM หรือ LOW ที่ควรปรับปรุงในอนาคต
- **`REVISE` (ส่งกลับไปแก้ไข):** คะแนนรวม $< 70$ หรือ **มีข้อผิดพลาดระดับ CRITICAL แม้เพียง 1 จุด**
- **`REJECT` (ปฏิเสธ):** มีข้อผิดพลาดระดับ CRITICAL หลายจุดที่มีผลกระทบทางกฎหมาย ความปลอดภัย หรือโครงสร้างหลักเสียหายจนแก้ไขเฉพาะจุดไม่ได้
- **`INSUFFICIENT_EVIDENCE` (ข้อมูลไม่เพียงพอ):** ข้อมูลที่ส่งมาขาดองค์ประกอบสำคัญ เช่น ส่ง prompt มาแต่ไม่มีภาพ หรือส่งชื่อเรื่องมาโดยไม่มีเนื้อหา

## 4. Human Override (สิทธิ์การตัดสินใจสูงสุดของมนุษย์)
- มนุษย์ (Creator / Creative Director / System Owner) คือผู้มีอำนาจสูงสุด
- หากมนุษย์ตัดสินใจ Override คำตัดสินของ AI (เช่น เปลี่ยนจาก `REVISE` เป็น `PASS` ด้วยเหตุผลทางศิลปะเฉพาะตัว):
  - ระบบจะบันทึกสถานะ `human_override: true`
  - บันทึก `original_verdict`, `new_verdict` และ `rationale` ของมนุษย์ไว้ในรายงาน เพื่อความโปร่งใสของประวัติการทำงาน
