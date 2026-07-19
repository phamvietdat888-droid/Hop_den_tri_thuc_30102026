# 📋 GIẢI MÃ 360 — Skill Sản Xuất Kịch Bản YouTube
> **Phiên bản:** 1.0
> **Liên kết:** Prompt "Hộp Đen Tri Thức" V5.1 (`prompts/nguoi_giai_ma_v1.md`)
> **Triết lý:** Quy trình chuẩn hóa + Kiểm soát chất lượng = Kịch bản triệu view nhất quán, không phụ thuộc cảm hứng.

---

## 🎯 SỨ MỆNH

Skill này là **"nhà máy sản xuất kịch bản"** — biến bất kỳ chủ đề thời sự nào thành kịch bản YouTube hoàn chỉnh theo phong cách "Hộp Đen Tri Thức", đảm bảo:
- Chất lượng đồng đều giữa các video (không phụ thuộc "hôm nay viết hay hay dở")
- Quy trình rõ ràng, lặp lại được, tối ưu thời gian
- Kiểm soát chất lượng bằng checklist cứng — không bỏ sót yếu tố nào
- Lưu trữ có hệ thống — dễ tra cứu, tái sử dụng, rút kinh nghiệm

> 🎯 **KHÁN GIẢ MỤC TIÊU (Cập nhật 30/04/2026):** 
> - **Nhân khẩu học:** 100% Nam giới, 25-34 tuổi. 
> - **Thiết bị:** 21.4% xem trên Smart TV (yêu cầu "TV-Safe": không từ ngữ thô tục, giọng nam tính đĩnh đạc, hình ảnh rõ nét).
> - **Hành vi:** 99% view từ người chưa Đăng ký. **BẮT BUỘC chèn Lời kêu gọi đăng ký (CTA) ở GIỮA video**, ngay sau khi bóc tách 1 insight đắt giá, tuyệt đối KHÔNG vứt CTA ở tuốt cuối video.

---

## 📂 CẤU TRÚC THƯ MỤC LÀM VIỆC

> **v3.2:** Cấu trúc chuẩn duy nhất: xem `docs/structure_reference.md`. Tóm tắt:

```
drafts/[YYYY-MM-DD]_[Topic]/           ← 01_brief → 05_review (WIP)
outputs/[YYYY-MM-DD]_[Topic]/
├── YouTube/         06_kich_ban_hoan_thien.md|.docx · 06b_goi_seo.md|.docx · thumbnail.png (16:9)
├── YouTube_Shorts/  short_01/, short_02/... (Bước 6f)
└── Facebook/        06d_bai_dang_fb.md|.docx · 06e_mega_comments.json · thumbnail/ (dọc 6:16)
.shared/kho_vu_khi/                    ← vi_von_hay · hook_test · lich_su_vn · noi_dau_hieu_qua
prompts/nguoi_giai_ma_v1.md           ← Prompt gốc V5.1 (KHÔNG chỉnh sửa)
```

---

## ⚙️ PIPELINE SẢN XUẤT — 7 BƯỚC

> ⚡ **CHÍNH SÁCH TỰ ĐỘNG HÓA (v2.7):** Chỉ có **2 Gate Check** (Bước 2 + Bước 3).
> Sau khi Sếp duyệt dàn ý, hệ thống chạy liên tục từ Bước 4 đến 6e mà KHÔNG dừng xin phép.
> Mọi lệnh hệ thống (convert DOCX, copy file, tạo ảnh) đều `SafeToAutoRun=true`.

```
[SẾP giao đề bài]
       │
       ▼
[BƯỚC 1] Tiếp nhận & Thu thập ──── 01_brief.md
       │
       ▼
[BƯỚC 2] Nghiên cứu & Đề xuất Góc ──── 02_angle.md
       │ ← 🔴 GATE 1: CHỜ SẾP CHỌN ANGLE
       ▼
[BƯỚC 3] Dàn ý Chi tiết ──── 03_outline.md
       │ ← 🔴 GATE 2: CHỜ SẾP DUYỆT DÀN Ý
       ▼
┌──────────────────────────────────────────────────┐
│  ⚡ TỰ ĐỘNG TỪ ĐÂY — Sếp ngồi uống trà chờ kết quả  │
└──────────────────────────────────────────────────┘
       │
[BƯỚC 4] Viết Kịch bản Nháp ──── 04_script_draft.md
       │ (tự động)
       ▼
[BƯỚC 5] Kiểm định Chất lượng ──── 05_review.md
       │ ← TRƯỢT? → TỰ SỬA & Kiểm định lại (không hỏi Sếp)
       ▼ (ĐẠT ≥ 85/100 — tự động)
[BƯỚC 6] Xuất bản YouTube
       │
       ├── 6a. Kịch bản Clean MD + DOCX
       ├── 6b. Gói SEO (20 tiêu đề + Mô tả + Từ khóa + DOCX)
       ├── 6c. Thumbnail YouTube 16:9
       │ (tự động)
       ├── 6d. Bài Facebook C.R.A.F.T + Ảnh + DOCX
       ├── 6e. Seeding Mega Comments (JSON)
       ├── 6f. Chuyển thể Shorts (Kịch bản + SEO + Ảnh + DOCX)
       └── Cập nhật Kho Vũ Khí
       │
       ▼
[★ TRÌNH SẾP] Toàn bộ sản phẩm trong outputs/
       (Sếp duyệt tổng thể 1 lần cuối)
       │
       ▼
[BƯỚC 7] Rút kinh nghiệm ──── 07_postmortem.md
       (Sau khi video lên sóng)
```

---

## 📝 CHI TIẾT TỪNG BƯỚC

### BƯỚC 1: TIẾP NHẬN & THU THẬP

**Input từ Sếp:**
- `[CHỦ_ĐỀ]`: Sự kiện/vấn đề cần làm kịch bản
- `[DỮ_LIỆU]`: Link báo, clip đối thủ, dàn ý sơ bộ, ý tưởng riêng
- `[SPONSOR]`: Có/Không. Nếu có → tên + sản phẩm
- `[YÊU_CẦU_ĐẶC_BIỆT]`: Giọng điệu, góc nhìn, từ khóa SEO cần ưu tiên...

**Hành động:**
1. Đọc Prompt V5.1 (`prompts/nguoi_giai_ma_v1.md`) — nạp toàn bộ quy tắc.
2. **⚠️ ĐỌC HIẾN PHÁP KÊNH:** Bắt buộc đọc file `Chien_Luoc_Phat_Trien.md` (thư mục gốc) do Agent Chiến Lược tạo ra. Nắm vững Chân dung khán giả, Nỗi đau và các Đạo luật chiến thuật hiện hành.
3. Đọc file brief đề bài Sếp cung cấp.
4. Nếu thiếu thông tin → HỎI LẠI ngay, KHÔNG tự suy diễn.
5. Tạo file `01_brief.md` trong thư mục kịch bản.

**Output — `01_brief.md`:**
```markdown
# BRIEF — [Tên chủ đề]
- Ngày: YYYY-MM-DD
- Chủ đề: ...
- Dữ liệu đầu vào: [liệt kê link/file]
- Có Sponsor: Có/Không
- Yêu cầu đặc biệt: ...
- Trạng thái: ✅ Đã tiếp nhận
```

✅ **Gate Check:** Sếp đã cung cấp đủ thông tin? → Nếu chưa → DỪNG, hỏi lại.

---

### BƯỚC 2: NGHIÊN CỨU & ĐỀ XUẤT GÓC NHÌN

**Hành động:**
1. **Đánh giá rủi ro YouTube:** Spam? Giật gân? Bạo lực? Nhạy cảm chính trị? → Nếu có → đề xuất cách xử lý.
2. **Đề xuất 5 Angle** — mỗi Angle gồm:

| # | Tên dân dã | Lý do chọn | Gợi ý Hook (công thức nào?) | 2-3 câu mở bài mẫu |
|---|---|---|---|---|
| 1 | ... | ... | ... | ... |
| 2 | ... | ... | ... | ... |

> **⚠️ BỘ LỌC ANGLE:** Mọi Angle ĐỀU PHẢI tuân thủ Chân dung khán giả trong Hiến pháp Kênh (Ví dụ: Tệp nam 25-34 thì Angle không được trẻ con/slang, phải đánh vào cơm áo gạo tiền/tự hào dân tộc). Angle vi phạm = Loại ngay lập tức.

3. **Gợi ý liên hệ lịch sử VN** (nếu có điểm tương đồng tự nhiên - theo đúng định hướng Content Pillars).
4. **Gợi ý điểm chạm nỗi đau** — Trích xuất trực tiếp từ mục "Nỗi sợ / Khát vọng" trong Hiến pháp Kênh để áp vào sự kiện này.

**Output — `02_angle.md`:**
```markdown
# GÓC TIẾP CẬN — [Tên chủ đề]

## Đánh giá rủi ro YouTube
- Mức rủi ro: Thấp / Trung bình / Cao
- Lưu ý: ...

## 5 Angle đề xuất
[Bảng 5 Angle]

## Gợi ý Liên hệ Lịch sử VN
- [Có tự nhiên / Không phù hợp → bỏ qua]

## Gợi ý Điểm chạm Nỗi đau
- Nỗi đau 1: ...
- Nỗi đau 2: ...

## ⏸️ CHỜ SẾP CHỌN ANGLE
```

✅ **Gate Check:** Sếp phải chọn Angle TRƯỚC KHI chuyển Bước 3. → **DỪNG & CHỜ.**

---

### BƯỚC 3: DÀN Ý CHI TIẾT (Tam Giác Ngược)

**Hành động:**
1. Xây dựng sườn kịch bản theo cấu trúc Tam Giác Ngược (Module 5 trong V5.1):

```
HOOK (50-80 từ)
└── Cầu nối (60-80 từ)
    └── Bối cảnh (200-250 từ)
        └── Thân bài — 3 lớp (≤ 1200 từ)
            ├── Lớp 1: Bề nổi
            │   └── [Hỏi → Đáp → Minh họa → Nhấn mạnh]
            ├── Lớp 2: Bề chìm + **[CHÈN CTA GIỮA VIDEO TẠI ĐÂY]**
            │   └── [Hỏi → Đáp → Minh họa → Nhấn mạnh]
            └── Lớp 3: Vĩ mô + Lịch sử soi chiếu hiện tại
                └── [Hỏi → Đáp → Minh họa → Nhấn mạnh]
        └── Cao trào
            └── Kết thúc mở (≤ 100 từ)
```

2. Đặt **Pacing Markers** mỗi ~400 từ.
3. Ghi chú vị trí cụ thể cho từng kỹ thuật:

| Kỹ thuật | Vị trí dự kiến | Nội dung tóm tắt |
|---|---|---|
| Hook (công thức X) | Mở đầu | ... |
| Ví von mở rộng | Lớp 2 | ... |
| Nhập vai đối thoại #1 | Lớp 1 | ... |
| Nhập vai đối thoại #2 | Lớp 3 | ... |
| Châm biếm | Lớp 2 | ... |
| Phản biện đa chiều | Lớp 2-3 | ... |
| Nỗi đau #1 | Bối cảnh | ... |
| Nỗi đau #2 | Lớp 2 | ... |
| Nỗi đau #3 | Cao trào | ... |
| Lịch sử VN | Lớp 3 / Cao trào | ... (hoặc "bỏ qua") |

4. Phân bổ số từ cho mỗi phần.

**Output — `03_outline.md`**

✅ **Gate Check:** Sếp duyệt dàn ý? → **DỪNG & CHỜ.**

---

### BƯỚC 4: VIẾT KỊCH BẢN NHÁP

**Hành động:**
1. **Đọc lại Prompt V5.1** — nạp toàn bộ 8 Module + Checklist.
2. Viết kịch bản theo format **bảng 2 cột [Visual | Audio]**.
3. Tuân thủ NGHIÊM NGẶT:
   - Module 1: Hook ≤ 80 từ, câu đầu ≤ 15 từ
   - Module 2: Nhịp câu 8-15 từ, KHÔNG dùng từ cấm
   - Module 3: Tiểu từ tình thái + Thán từ + Ngôn ngữ sạch
   - Module 4: Ví von + Nhập vai + Câu hỏi tu từ 3 chức năng + Châm biếm + Phản biện
   - Module 5: Mỗi luận điểm theo Hỏi-Đáp-Minh họa-Nhấn mạnh
   - Module 6: Quy tắc ví von + Kết nối Vĩ mô ↔ Vi mô
   - Module 7: ≥ 3 điểm chạm nỗi đau
   - Module 8: 1-2 liên hệ lịch sử VN (nếu tự nhiên)
4. Đánh dấu tag tại các vị trí: `[HOOK: X]`, `[VÍ VON MỞ RỘNG]`, `[NHẬP VAI]`, `[CHÂM BIẾM]`, `[PHẢN BIỆN]`, `[NỖI ĐAU]`, `[LỊCH SỬ VN]`, `[PACING MARKER]`, `[CTA]`.
5. Tổng kịch bản: 1200-1600 từ.

**Output — `04_script_draft.md`**

---

### BƯỚC 5: KIỂM ĐỊNH CHẤT LƯỢNG (Tự động)

**Hành động:**
Chạy **`checklist.md` (33 tiêu chí, 8 nhóm A-H)** — nguồn chấm điểm DUY NHẤT toàn hệ thống (v3.2, thay bảng 22 tiêu chí cũ):

- **Kịch bản YouTube:** nhóm H (Compliance Shield — chạy TRƯỚC TIÊN) + nhóm A-F (23 tiêu chí, ≈ 4.35 điểm/tiêu chí, chuẩn hóa thang 100)
- **Bài Facebook (Bước 6d):** thêm nhóm G (#24-29)
- **5 tiêu chí VETO:** #16 (Tục), #23 (Clickbait YT), #27 (Clickbait FB), #29 (Vi phạm TCCĐ), #30 (Compliance Blacklist) — trượt bất kỳ = TRƯỢT toàn bài bất kể tổng điểm

**Quy tắc chấm điểm:**
- **≥ 85 điểm → ĐẠT** → Chuyển Bước 6
- **< 85 điểm → TRƯỢT** → Ghi danh sách lỗi → **Quay lại Bước 4** sửa → Kiểm định lại

**Output — `05_review.md`:**
```markdown
# KIỂM ĐỊNH — [Tên chủ đề]
- Lần kiểm định: 1 (hoặc 2, 3...)
- Điểm: __/100
- Kết quả: ĐẠT / TRƯỢT
- Lỗi cần sửa: [danh sách cụ thể]
```

---

### BƯỚC 6: KỊCH BẢN HOÀN CHỈNH

**Hành động:**
1. **(6a) Kịch bản Audio Clean:** Áp dụng chỉnh sửa từ Bước 5. Chuyển bảng 2 cột thành format Audio Clean (chỉ Lời bình) với thẻ màu (`<red>`, `<green>`, `<blue>`, `<orange>`, `<underline>` — CẤM emoji màu). Lưu `06_kich_ban_hoan_thien.md`. Xuất `.docx` bằng `scripts/md_to_docx_v2.py` (Times New Roman 14pt, A4, lề 2cm, Justify, giãn 1.25 — chi tiết `.shared/format_output.md`). TUYỆT ĐỐI KHÔNG tạo file trắng/plain text.
2. **(6b) Gói SEO:** Gọi `skills/viet_tieu_de_skill.md` → 20 tiêu đề (≤ 55 ký tự) + Mô tả 250 từ + 20 từ khóa. Lưu `06b_goi_seo.md` + `.docx`. Đề xuất A/B Test → **CHỜ SẾP CHỌN TIÊU ĐỀ** (duyệt tổng thể cuối).
3. **(6c) Thumbnail YouTube:** Ảnh ngang 16:9 (1280×720, PNG) → `YouTube/thumbnail.png`. Nguyên tắc **"Big Screen Safe"**: chữ TO, tương phản cực cao, cách lề ≥ 10%. Lỗi tạo ảnh → xuất `06c_image_prompt.md` + báo Sếp.
4. **(6d) Bài Facebook:** Gọi `skills/dang_fanpage_skill.md` — C.R.A.F.T 500-800 từ + ảnh dọc 6:16 → `Facebook/06d_bai_dang_fb.md` + `.docx`.
5. **(6e) Seeding:** Gọi `skills/seeding_facebook_skill.md` → 3-7 Mega Comments + 2 CTA → `Facebook/06e_mega_comments.json`.
6. **(6f) YouTube Shorts:** Gọi `skills/youtube_short_skill.md` (lệnh `/tao_short`) — 2-3 Shorts ≤ 50s, Hook viết LẠI + 5 tiêu đề + 10 prompt ảnh 9:16 + DOCX → `YouTube_Shorts/short_01/`...
7. **Cập nhật Kho Vũ Khí** nếu có ví von/hook/nỗi đau/lịch sử mới.

**Output (Lưu vào đúng cấu trúc `outputs/[Ngày] [Tên chủ đề]/`):**
- Thư mục `YouTube/`:
  - `06_kich_ban_hoan_thien.md`
  - `06_kich_ban_hoan_thien.docx`
  - `06b_goi_seo.md`
  - `06b_goi_seo.docx`
  - `thumbnail.png`
- Thư mục `YouTube_Shorts/`: (Chứa các thư mục con `short_01`, `short_02`... với đầy đủ kịch bản, SEO, ảnh minh họa và file DOCX).

✅ **Gate Check:** Sếp duyệt bản cuối + chọn tiêu đề → Giao Editor dựng video. Hoặc gọi `/dang_fb` để sang Bước 6d (Phát sóng Fanpage).

---

### BƯỚC 7: RÚT KINH NGHIỆM (Postmortem)

⚠️ Bước này thực hiện SAU KHI video lên sóng 48-72 giờ.

**Hành động:**
1. Sếp cung cấp dữ liệu: Views, Watch Time, Retention, CTR thumbnail, Top comments.
2. Phân tích:

| Chỉ số | Kết quả | Đánh giá |
|---|---|---|
| Views (48h đầu) | ___ | Trên/Dưới trung bình kênh |
| Retention trung bình | ___% | Tốt (≥50%) / Trung bình / Kém |
| Retention 30s đầu | ___% | Hook hiệu quả? |
| CTR Thumbnail | ___% | Tiêu đề + Thumbnail OK? |
| Top 3 Comment | ___ | Người xem phản hồi gì? |

3. Rút ra bài học:
   - Hook nào hiệu quả / không hiệu quả?
   - Ví von nào được khen / bị bỏ qua?
   - Nỗi đau nào chạm đúng / chệch?
   - Liên hệ lịch sử VN có được khen hay bị chê gượng?
   - Điểm nào Retention tụt → nghe lại đoạn đó, tìm lý do.
   - **Tiêu đề:** Formula nào đã dùng? CTR bao nhiêu? Hiệu quả hay không?

4. Cập nhật Kho Vũ Khí với label hiệu quả/không hiệu quả.
5. **Ghi nhận CTR + Formula tiêu đề** vào `viet_tieu_de_skill.md` phần Postmortem (để tích lũy data dần).

**Output — `07_postmortem.md`**

---

## ⚡ SLASH COMMANDS (Lệnh nhanh)

| Lệnh | Chức năng |
|---|---|
| `/tac_chien [chủ đề]` | Khởi động Pipeline từ Bước 1 |
| `/angle [chủ đề]` | Bước 2 — Đề xuất 5 Angle nhanh |
| `/dan_y` | Bước 3 — Tạo dàn ý Tam Giác Ngược |
| `/dang_fb` | Đăng bài lên Fanpage (tự động chạy Mega Comments) |
| `/tao_short [chủ đề]` | Chuyển thể kịch bản dài thành 2-3 video Shorts + File DOCX |
| `/kham_kenh` | Chạy 7 module khám sức khỏe kênh YouTube |
| `/viet` | Bước 4 — Viết kịch bản nháp |
| `/kiem_dinh` | Bước 5 — Chạy kiểm định 33 tiêu chí (checklist.md) |
| `/xuat_ban` | Bước 6a — Xuất bản cuối + cập nhật Kho Vũ Khí |
| `/tieu_de` | Bước 6b — Tạo 20 tiêu đề cho kịch bản hiện tại |
| `/rut_kinh_nghiem` | Bước 7 — Postmortem sau khi lên sóng |
| `/kho_vu_khi` | Xem Kho Vũ Khí (ví von, hook, nỗi đau, lịch sử) |
| `/tien_do` | Báo cáo tiến độ tất cả kịch bản đang sản xuất |

---

## 📊 BẢNG THEO DÕI TIẾN ĐỘ

Khi Sếp gọi `/tien_do`, hệ thống trả về bảng:

| # | Chủ đề | Ngày tạo | Trạng thái | Bước hiện tại | Người chờ |
|---|---|---|---|---|---|
| 1 | Chiến tranh thương mại | 2026-04-20 | 🟡 Đang xử lý | Bước 3 - Dàn ý | Chờ Sếp duyệt |
| 2 | Đất hiếm Trung Quốc | 2026-04-22 | 🔴 Chưa bắt đầu | — | — |
| 3 | NATO mở rộng | 2026-04-18 | 🟢 Hoàn thành | Bước 7 - Postmortem | Chờ data YouTube |

---

## 🔄 QUY TẮC VẬN HÀNH

### 1. Đọc trước khi làm
- **BẮT BUỘC** đọc Prompt V5.1 (`prompts/nguoi_giai_ma_v1.md`) ở Bước 1 và Bước 4.
- Đọc `kho_vu_khi/` trước Bước 2 để tái sử dụng ví von hay, tránh lặp.

### 2. Gate Check — CHỈ 2 ĐIỂM DỪrNG (v2.7)
Toàn bộ pipeline CHỈ dừng ở 2 điểm:
- 🔴 Bước 2 → CHỜ Sếp chọn Angle
- 🔴 Bước 3 → CHỜ Sếp duyệt dàn ý
- Bước 4-6e → **TỰ ĐỘNG**, AI không dừng xin phép
- Bước 5 trượt → AI tự sửa và kiểm định lại
- Mọi lệnh hệ thống (DOCX, copy, ảnh) đều `SafeToAutoRun=true`

### 3. Luôn lưu vào đúng thư mục con theo ngày
Mọi file nháp (Bước 1-5) BẮT BUỘC lưu vào thư mục `drafts/[Ngày] [Tên chủ đề]/`.
Mọi file xuất bản hoàn thiện (Bước 6, 7) bao gồm bản Clean/Markup BẮT BUỘC lưu vào `outputs/[Ngày] [Tên chủ đề]/`. KHÔNG vứt file lung tung ngoài thư mục gốc.

### 4. Cập nhật Kho Vũ Khí
Sau mỗi kịch bản hoàn thành → BẮT BUỘC cập nhật Kho Vũ Khí với các "vũ khí" mới phát hiện.

### 5. Postmortem là bắt buộc
Video nào cũng phải có Bước 7. Không postmortem = không học được gì = lãng phí.

---

## 📎 THAM CHIẾU

| Tài liệu | Đường dẫn |
|---|---|
| Prompt "Hộp Đen Tri Thức" V5.1 | `prompts/nguoi_giai_ma_v1.md` |
| Hồ sơ tình báo đối thủ (5 kênh) | `Đối_thủ/` |
| Báo cáo tình báo tổng hợp | `Đối_thủ/bao_cao_tinh_bao.md` |

---

> **Ghi nhớ:** Skill này là DÂY CHUYỀN SẢN XUẤT. Prompt V5.1 là CÔNG THỨC. Kho Vũ Khí là NGUYÊN LIỆU. Kết hợp cả 3 = Kịch bản đỉnh cao, nhất quán, mỗi video đều mạnh.
