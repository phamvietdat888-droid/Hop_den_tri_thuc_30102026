# 🧠 GIẢI MÃ 360° — Nhà máy Sản xuất Kịch bản YouTube "Kiến thức Giải trí"
> **Persona:** "Người Giải Mã" (giải thích cặn kẽ, dễ hiểu, thu hút) · **Fanpage:** Giải Mã 360
> **Phiên bản:** v1.0 (2026-07-05) · Nhân bản cấu trúc từ dự án NKTC, thay TOÀN BỘ giọng văn.

---

## 1. Đây là gì?

Một hệ **đa tác nhân (5 Agent)** sản xuất kịch bản video YouTube theo dây chuyền — GIỐNG HỆT cấu trúc dự án "Nhật Ký Tác Chiến" (NKTC), nhưng **giọng văn đổi hoàn toàn**:

| | NKTC (dự án gốc) | GIẢI MÃ 360 (dự án này) |
|---|---|---|
| Persona | "Bình Luận Viên Trà Đá" (bố đời, gai góc) | **"Người Giải Mã"** (giải thích cặn kẽ, dễ hiểu, thu hút) |
| Xưng hô | chúng ta / các bác / anh em | **mình / bạn / các bạn** |
| Chủ đề | Địa chính trị | **Đa chủ đề** (địa chính trị + true-crime + tài chính + khoa học đời sống + giải mã khái niệm + lịch sử) |
| Vũ khí chính | Mỉa mai, châm biếm, kéo về "nỗi đau túi tiền" | **Ví von đời thường · Bẻ nhỏ đánh số · Đón đầu phản biện · Chi tiết đinh** |
| Độ dài | 1500–1800 từ | **1200–1600 từ** |
| Kết bài | Câu hỏi gây tranh cãi | **Chốt cân bằng, an toàn + mở câu hỏi** |

Nguồn cảm hứng giọng: phân tích 4 transcript edutainment Sếp gửi (Năm Cam · Bóng đè · Rửa tiền · Bảo hiểm) → chưng cất thành "Hiến pháp Giọng nói" + persona-prompt bậc thầy.

---

## 2. "Bộ não" của dự án (đọc trước khi làm)

| File | Vai trò |
|---|---|
| `prompts/nguoi_giai_ma_v1.md` | ⭐ **Persona-prompt bậc thầy** (C.R.A.F.T.) — Agent 02 đọc trước khi viết |
| `GEMINI.md` | Hiến pháp trung tâm (pipeline, lệnh, nguyên tắc) — LUÔN đọc đầu tiên |
| `CLAUDE.md` | Điểm vào Cowork (bản đồ nhanh) |
| `checklist.md` | 33 tiêu chí kiểm định (đã hiệu chỉnh cho giọng mới) |

## 3. DNA giọng nói (thư mục `.shared/`)

| File | Nội dung |
|---|---|
| `tone_guide.md` | Giọng "Người Giải Mã": xưng hô, nhịp câu, tiểu từ, hài duyên |
| `hook_formulas.md` | 6 công thức Hook (con số, câu hỏi, "bạn là nhân vật"…) + open loop |
| `storytelling_arsenal.md` | 6 kỹ thuật: Ví von · Bẻ nhỏ đánh số · **Đón đầu phản biện** · Nhập vai · Chi tiết đinh · Socrates |
| `to_mo_loi_ich_module.md` | Liên hệ người xem qua Tò mò · Lợi ích · Gương soi (thay module "nỗi đau") |
| `tu_cam.md` | Từ cấm — giữ phần chống-AI/clickbait, thêm mục **G** cấm đặc thù persona |
| `few_shot_examples.md` | 8 ví dụ mẫu đa chủ đề |
| `kho_vu_khi/` | Kho tái sử dụng: ví von, hook đã kiểm chứng, điểm liên hệ, kiến thức nền |

## 4. Cách dùng (giống NKTC)

Mở thư mục này trong Cowork rồi gõ lệnh (bảng lệnh đầy đủ ở `GEMINI.md §7`):
- `/tac_chien [chủ đề]` — chạy dây chuyền sản xuất 1 kịch bản (2 Gate: chọn Angle → duyệt Dàn ý).
- `/tim_trend [từ khóa]` — trinh sát chủ đề.
- `/dang_fb`, `/tao_short` — phái sinh Facebook / Shorts.

Xem bản mẫu nghiệm thu: `outputs/2026-07-05_Bong_De_DEMO/` (kịch bản + kiểm định 90/100).

## 5. Việc cần Sếp lưu ý (bàn giao)

1. **Đổi tên thương hiệu:** "Giải Mã 360" / "Người Giải Mã" / thư mục `GiaiMa360` là tên tạm em đặt — muốn đổi, tìm-thay đồng loạt là xong.
2. **Cài lại node_modules cho skill tải transcript:** `cd skills/video-transcript-downloader && npm install`. (Còn vài file `.d.ts` cũ bị khóa quyền, vô hại.)
3. **File kế thừa cần tỉa dần:** `ERRORS.md`, `Learning.md`, `viet_bai_viral.md`, `format_facebook.md` chứa bài học/format chung nhưng còn vài ví dụ mang giọng cũ — dùng tham khảo, sẽ chuẩn hóa dần theo giọng mới.
4. **Scripts PowerShell** (`.ps1`) chạy trên máy Windows, không chạy trong sandbox Cowork.
5. **Tuyệt đối không bịa số liệu** — mọi con số phải xác minh, chưa chắc thì ghi `[CẦN XÁC MINH]`.

---

*Dựng bởi Cowork · nhân bản cấu trúc NKTC + thay giọng theo phân tích transcript edutainment.*
