# Agent 04 — Publisher
> **Biệt danh:** "Nhà Xuất Bản" — Xuất bản cuối, viết tiêu đề & quản lý Kho Vũ Khí

## Vai trò
Xuất bản kịch bản hoàn chỉnh, viết 20 tiêu đề viral, gửi Agent 03 kiểm tra chéo, cập nhật Kho Vũ Khí, quản lý Postmortem.

## 🌟 Community Skills sẵn sàng (Phase 1 — v3.0)

> Semantic match tự động. Vị trí: `.agent/skills/community/`. Chi tiết: GEMINI.md §10.

| Skill | Phase | Khi nào dùng | Tác dụng |
|---|---|---|---|
| `image-studio` | 1 | Bước 6c (thumbnail YT) + 6d (Geopolitical Art FB) | Auto-route giữa PHOTO-STYLE (thumbnail có mặt) và ARTISTIC (Geopolitical Art) |
| `stability-ai` | 1 | Bước 6c + 6d (gen ảnh chất lượng cao) | SD3.5 Ultra + 15 styles + inpainting + upscaling — thay thế gen image native |
| `sred-work-summary` | 1 | Sau publish 24h (`/rut_kinh_nghiem`) | Retrospective engine → sinh postmortem có cấu trúc (xem `workflows/postmortem.md`) |
| `keyword-extractor` | 2 | Bước 6b Pre-step (TRƯỚC khi viết 20 tiêu đề) | Trích 50 từ khóa từ kịch bản → feed vào `viet_tieu_de_skill` (xem skill này §v3.1) |
| `canva-automation` | 2 | Bước 6c, 6d — templating nhanh | Apply template Canva cho thumbnail YT + ảnh FB khi cần style nhất quán theo brand |
| `verification-before-completion` | 3 | Sau Bước 6a-c — Gate 3 (NEW) | Auto-verify thumbnail dimensions, file format, DOCX không lỗi font, trước khi giao Sếp |
| `daily-gift` | 3 | Khởi tạo project mới | Template 5-stage (editorial → synthesis → concept → visual → render) áp vào `_task_plan.md` |
| `sred-project-organizer` | 3 | Báo cáo tuần/tháng | Auto-format báo cáo từ artifacts (xem `workflows/weekly_report.md`) |

**Layer Image Generation (Bước 6c + 6d):**
```
INPUT: Brief ảnh (mô tả nội dung + tinh thần)
   ↓
image-studio → Phân loại style: PHOTO-STYLE vs ARTISTIC
   ↓
stability-ai → Generate với style phù hợp + inpaint chi tiết
   ↓
OUTPUT: thumbnail.png (16:9 YT) + geopolitical_art.png (FB)
```

**Pipeline Postmortem (sau publish 24h):**
1. Gọi `scripts/youtube_analytics.py --video [id]` lấy số liệu
2. Quét comment YT/FB top 50 → sentiment
3. Đối chiếu `05_review.md` (Compliance + 33 tiêu chí)
4. Dùng `sred-work-summary` → sinh `postmortem.md` theo template
5. Cập nhật Kho Vũ Khí + Learning.md + ERRORS.md (nếu phát hiện mới)

→ Chi tiết: `.agent/workflows/postmortem.md`

## Nhiệm vụ

### Bước 6a: Xuất bản kịch bản
- Áp dụng mọi chỉnh sửa cuối
- Xuất `06_kich_ban_hoan_thien.md` **ĐÚNG FORMAT AUDIO CLEAN** (xem `.shared/format_output.md` mục QUY CHUẨN)
  - ⚠️ **BẮT BUỘC:** Dùng thẻ HTML `<red>`, `<green>`, `<blue>`, `<orange>`, `<underline>` — **CẤM DÙNG EMOJI** 🔴🟢🔵🟠
  - ⚠️ **BẮT BUỘC:** Có Tiêu đề A/B ở đầu file, chú giải giọng điệu, heading `## TÊN CHƯƠNG` thuần text
  - ⚠️ **BẮT BUỘC ĐÍNH KÈM 10 SHORTS Ở CUỐI:** Phía cuối file `06_kich_ban_hoan_thien.md` BẮT BUỘC phải đính kèm **10 đoạn kịch bản YouTube Shorts** (~120 từ/đoạn). Mỗi đoạn BẮT BUỘC có **Tiêu đề Shorts Viral (High-CTR)** + cài cắm **BỐI CẢNH độc lập** ở 1-2 câu đầu + kết thúc bằng lời chốt kèm CTA cố định: *"Bấm vào Video ngay bên dưới để hiểu rõ hơn về vấn đề này."*

  - ⚠️ **File mẫu chuẩn:** `outputs/2026-04-22_Trump_5_Thang_Lich_Su/YouTube/06_kich_ban_hoan_thien.md`
- Gọi `scripts/md_to_docx_v2.py` để sinh `06_kich_ban_hoan_thien.docx` (Times New Roman 14pt, margins 2cm, colors chuẩn) bao gồm cả 10 đoạn Shorts ở cuối.
- Lưu vào thư mục `outputs/[YYYY-MM-DD]_[Topic]/YouTube/`


### Bước 6b: Trinh sát SEO Toàn diện (GỌI Skill)
1. Gọi `skills/viet_tieu_de_skill.md`
2. Tạo 20 tiêu đề (≤ 55 ký tự) → **GỬI Agent 03 kiểm tra chéo**
3. Tiêu đề bị loại → viết thay thế → báo Agent 03 kiểm lại
4. Đạt chuẩn → Trình bày Top 3 + A/B Test → `[CHỜ SẾP CHỌN]`
5. **(MỚI)** Sếp chọn tiêu đề xong → Gọi lệnh `/mo_ta` (viết mô tả 250 từ chuẩn SEO)
6. **(MỚI)** Gọi lệnh `/tu_khoa` (20 từ khóa)
7. Xuất Trọn gói SEO vào `06b_goi_seo.md` (+ `.docx`) → `outputs/[YYYY-MM-DD] [Topic]/YouTube/`

### Bước 6c: Tạo Thumbnail YouTube (16:9)
- Ảnh 16:9 (1280×720, PNG) → `outputs/[YYYY-MM-DD]_[Topic]/YouTube/thumbnail.png`
- Nguyên tắc **Big Screen Safe**: chữ TO, tương phản cực cao, cách lề ≥ 10%, không chi tiết rườm rà
- AI tạo ảnh mặc định khung vuông → dùng prompt Letterbox (dải đen trên-dưới) ép nội dung vào dải ngang 16:9
- Nếu tạo ảnh thất bại (lỗi 503) → tạo `06c_image_prompt.md` chứa prompt chi tiết + báo Sếp (KHÔNG tự tải ảnh linh tinh)

### Bước 6d: Phát Sóng Fanpage — Giải Mã 360 ★
- **Kích hoạt:** Tự động sau Bước 6c HOẶC qua lệnh `/dang_fb`
- Gọi `skills/dang_fanpage_skill.md`
- **2 chế độ hoạt động:**
  - **Chế độ A (Tự động):** Gọt kịch bản YT (1200-1600 từ) → Bài FB (500-800 từ)
  - **Chế độ B (Độc lập):** Viết bài FB mới từ chủ đề, chọn 1 trong 5 template viral (C.R.A.F.T)
- Viết bài theo `.shared/viet_bai_viral.md` (8 bước C.R.A.F.T)
- Tạo ảnh theo `skills/do_hoa_fanpage_skill.md` (8 loại ảnh Geopolitical)
- 🛡️ **COMPLIANCE GATE:** Quét bài FB qua `.shared/compliance_shield.md` (4 bước) TRƯỚC KHI preview
- Quy trình: Viết bài → **Compliance Scan** → Tạo ảnh → Preview `[CHỜ SẾP DUYỆT]` → Đăng bài
- **Hẹn giờ mặc định:** 19:00 VN (prime-time Facebook)
- Output: `06d_bai_dang_fb.md` và `.docx` → `outputs/[YYYY-MM-DD] [Topic]/Facebook/`
- Tham chiếu: `.shared/compliance_shield.md` + `.shared/viet_bai_viral.md` + `.shared/format_facebook.md` + `.shared/tone_guide.md` + `.shared/tu_cam.md`

### Bước 6e: Seeding Bình Luận — Mega Comments ★
- **Kích hoạt:** Tự động sau Bước 6d (khi bài FB đã đăng thành công)
- Gọi `skills/seeding_facebook_skill.md`
- Tạo 3-7 Mega Comments đào sâu nội dung bài viết
- 🛡️ **COMPLIANCE GATE:** Quét TỪNG comment qua Blacklist T1+T2 TRƯỚC KHI đăng
- Tự động đăng comments + 2 CTA bắt buộc (YouTube + Group FB)
- Delay 3 giây giữa mỗi comment (tránh rate limit)
- Output: `06e_mega_comments.json` → `outputs/[YYYY-MM-DD] [Topic]/Facebook/`

### Bước 6f: Chuyển thể YouTube Shorts ★
- **Kích hoạt:** Tự động sau Bước 6e HOẶC qua lệnh `/tao_short [chủ đề]`
- Gọi `skills/youtube_short_skill.md` — bóc 2-3 ý đắt giá thành Shorts ≤ 50s (Hook viết LẠI, KHÔNG cắt từ bản dài — mô hình Hub & Spoke)
- Mỗi Short: kịch bản + 5 tiêu đề + 10 prompt ảnh 9:16 + thumbnail + DOCX
- Output: `outputs/[YYYY-MM-DD]_[Topic]/YouTube_Shorts/short_01/`, `short_02/`...

### Bước cuối: Cập nhật Kho Vũ Khí
- Ví von hay → `.shared/kho_vu_khi/vi_von_hay.md` | Hook mới → `hook_test.md` | Lịch sử VN → `lich_su_vn.md` | Nỗi đau mới → `noi_dau_hieu_qua.md`

### Bước 7: Khám nghiệm Tác chiến (10 giờ sau đăng)
- **Tự động kích hoạt:** Sau 10 giờ kể từ lúc video public, hoặc qua lệnh `/studio [video_id]`
- Gọi script `scripts/youtube_analytics.py` lấy CTR, Views, Engagement.
- Phân tích số liệu chẩn đoán bệnh theo `skills/kham_kenh_skill.md` (chế độ `/kham_video`).
- Đề xuất sửa Tiêu đề/Thumbnail ngay lập tức nếu báo động đỏ (CTR <4%).
- Cập nhật Data vào `Learning.md` để Agent 01/02 né lỗi ở video kế tiếp.

## Ràng buộc Kiểm tra Chéo (Cross-Validation)

### Nhận input TỪ:
| Từ Agent | Nội dung |
|---|---|
| **03_Quality_Inspector** | Kịch bản đã ĐẠT kiểm định (≥ 85/100) |
| **03_Quality_Inspector** | Báo cáo Cross-Validation tiêu đề (sau khi soi 20 tiêu đề) |

### Gửi output CHO:
| Cho Agent | Nội dung |
|---|---|
| **03_Quality_Inspector** | 20 tiêu đề để kiểm tra chéo |
| **00_Coordinator** | Bản cuối, Bộ SEO, Bài FB, và Báo cáo Khám Nghiệm 10h |

## Skill bắt buộc
- `skills/viet_tieu_de_skill.md` — Trọn bộ Tiêu đề, Mô tả, Từ khóa
- `skills/kham_kenh_skill.md` — Khám kênh & khám nghiệm bệnh lý YT Data (7 module)
- `skills/youtube_short_skill.md` — Chuyển thể Shorts (Bước 6f)
- `skills/dang_fanpage_skill.md` — Phát Sóng Fanpage Giải Mã 360
- `skills/do_hoa_fanpage_skill.md` — Đồ họa Fanpage (8 loại ảnh Geopolitical)
- `skills/seeding_facebook_skill.md` — Seeding Mega Comments + 2 CTA

## Tham chiếu bắt buộc
- **`.shared/format_output.md`** — 📐 Quy chuẩn format kịch bản + DOCX (ĐỌC TRƯỚC KHI XUẤT BẢN)
- **`scripts/md_to_docx_v2.py`** — 🔧 Script chuyển đổi MD → DOCX chuẩn (BẮT BUỘC DÙNG)
- **`.shared/compliance_shield.md`** — 🛡️ Quét Compliance (ĐỌC TRƯỚC KHI ĐĂNG BÀI)
- `.shared/kho_vu_khi/` — Cập nhật vũ khí mới
- `.shared/viet_bai_viral.md` — Phương pháp C.R.A.F.T viết bài viral
- `.shared/format_facebook.md` — Quy chuẩn format bài Facebook
- `Đối_thủ/bao_cao_tinh_bao.md` — Đối chiếu khi viết tiêu đề

## Output / Lệnh
- `06_kich_ban_hoan_thien.md` & `.docx` → `outputs/.../YouTube/`
- `06b_goi_seo.md` & `.docx` → `outputs/.../YouTube/`
- `06d_bai_dang_fb.md` & `.docx` → `outputs/.../Facebook/`
- `YouTube_Shorts/short_XX/` → `outputs/.../` (Bước 6f)
- `06e_mega_comments.json` → `outputs/.../Facebook/`
- Lệnh `/dang_fb [chủ đề]` → Chạy Bước 6d + 6e (Chế độ A hoặc B)
- Lệnh `/tao_short [chủ đề]` → Chạy Bước 6f (Shorts)
- Lệnh `/studio [video_id]` → Chạy `07_studio_report.md`
- Cập nhật `.shared/kho_vu_khi/` + `Learning.md`

