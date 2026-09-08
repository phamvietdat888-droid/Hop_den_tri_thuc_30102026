---
name: tac-chien
description: "Khởi động và điều phối quy trình tác chiến sản xuất nội dung."
---

# Workflow: Tác Chiến (Sản xuất Kịch bản)
> **Trigger:** `/tac_chien [chủ đề]`
> **⚠️ v3.2:** File này là ALIAS. Pipeline chuẩn DUY NHẤT của toàn hệ thống: `san_xuat_kich_ban.md` (cùng thư mục). Mọi chi tiết bước/gate/tên file lấy ở đó — KHÔNG duy trì 2 bản song song.

## Tóm tắt luồng

1. **Bước 1-2** (Agent 01): Brief + 5 Angle → 🔴 **Gate 1: CHỜ SẾP CHỌN ANGLE**
2. **Bước 3** (Agent 02): Dàn ý Tam Giác Ngược → 🔴 **Gate 2: CHỜ SẾP DUYỆT DÀN Ý**
3. **Bước 4 → 6f** (⚡ tự động, không dừng xin phép):
   - Bước 4: Viết nháp 1200-1600 từ, 8 Module (Agent 02)
   - Bước 5: Kiểm định 33 tiêu chí `checklist.md` — nhóm A-F + H, loop tự sửa ≤ 3 vòng (Agent 03)
   - Bước 6a-6f: Xuất bản (Agent 04) — Clean MD + DOCX / Gói SEO `06b_goi_seo` / Thumbnail 16:9 / Bài FB `06d_bai_dang_fb` / Seeding `06e_mega_comments.json` / Shorts `YouTube_Shorts/`
   - Cập nhật Kho Vũ Khí `.shared/kho_vu_khi/`
4. **Bước 7:** Postmortem sau 48-72h (`workflows/postmortem.md`)

## Tham chiếu
- Pipeline YAML đầy đủ: `.agent/workflows/san_xuat_kich_ban.md`
- Quy tắc nội dung: `GEMINI.md` + `.shared/` + `skills/giai_ma_360_skill.md`
- Tên file chuẩn + cấu trúc thư mục: `docs/structure_reference.md`
