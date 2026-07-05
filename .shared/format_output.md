# 📝 FORMAT ĐẦU RA — Bảng 2 Cột
> **Nguồn:** [FORMAT] — Prompt V5.1

---

## Cấu trúc bảng

| GỢI Ý HÌNH ẢNH (Visual) | LỜI NÓI (Audio) |
|---|---|
| *Mô tả hình ảnh/footage* | *Lời thoại đầy đủ* |
| Bản đồ Trung Đông, zoom xung đột | **800 tỷ đô-la.** Đó là số tiền bay hơi chỉ trong 72 giờ… |
| Cảnh chợ Việt Nam, 2 bà bán hàng | Giống y bà bán rau đầu chợ thấy bà cuối chợ hạ giá… |

## Quy tắc format
- In **đậm** cho TỪ KHÓA cần nhấn mạnh giọng.
- Đánh dấu `[PACING MARKER]` tại mỗi điểm bẻ lái nhịp (~400 từ).
- Đánh dấu `[CTA]` tại vị trí chèn lời kêu gọi Like/Sub.
- Ghi chú `[HOOK: Tên công thức]` ở đầu.
- Ghi chú kỹ thuật tại các vị trí tương ứng:
  - `[CHÂM BIẾM]`
  - `[VÍ VON MỞ RỘNG]`
  - `[NHẬP VAI]`
  - `[PHẢN BIỆN]`
  - `[NỖI ĐAU]`
  - `[LỊCH SỬ VN]`

## Cấu trúc kịch bản

```
1. HOOK — CÚ ĐẤM (50-80 từ)
2. CẦU NỐI (60-80 từ)
3. DẪN DẮT — BỐI CẢNH (200-250 từ)
4. THÂN BÀI — GIẢI MÃ SÂU (≤ 1200 từ)
   ├── Lớp 1: Bề nổi
   ├── Lớp 2: Bề chìm
   └── Lớp 3: Vĩ mô
5. CAO TRÀO & CTA
6. KẾT LUẬN — KẾT THÚC MỞ (≤ 100 từ)
```

**Tổng: 1200-1600 từ**

---

## ⚠️ QUY TẮC OUTPUT PATH — BẮT BUỘC (Không ngoại lệ)

> **Lệnh từ Sếp:** Mỗi chủ đề PHẢI tạo 3 thư mục con `YouTube/`, `Facebook/` và `YouTube_Shorts/` riêng biệt. KHÔNG ĐƯỢC để file lẫn lộn trong thư mục gốc của chủ đề.

### Cấu trúc bắt buộc:
```
outputs/YYYY-MM-DD_Ten_Chu_De/
├── YouTube/                          ← Tất cả nội dung YouTube dài
│   ├── 06_kich_ban_hoan_thien.md         Kịch bản Audio Clean
│   ├── 06_kich_ban_hoan_thien.docx       File Word cho thu âm
│   ├── 06b_goi_seo.md                    20 tiêu đề + Mô tả + 20 từ khóa
│   ├── 06b_goi_seo.docx                  File Word cho gói SEO
│   ├── thumbnail.png                     Ảnh bìa video
│   └── thumbnail_prompt.md               (Tùy chọn) Lưu prompt tạo ảnh nếu hệ thống lỗi
├── Facebook/                         ← Tất cả nội dung Fanpage
│   ├── 06d_bai_dang_fb.md                Bài đăng Facebook
│   ├── 06d_bai_dang_fb.docx              File Word bài Facebook
│   ├── 06e_mega_comments.json            Seeding comments (JSON)
│   └── thumbnail/                        Ảnh đính kèm bài post
└── YouTube_Shorts/                   ← Tất cả nội dung Video ngắn
    └── short_01/                         
        └── kich_ban_short.md             Kịch bản video ngắn dọc
```

### Mapping file → thư mục:
| File | Thư mục |
|---|---|
| `06_kich_ban_*` | `YouTube/` |
| `06b_goi_seo*` | `YouTube/` |
| `thumbnail_prompt.md` | `YouTube/` |
| `thumbnail.png/.jpg` (YouTube) | `YouTube/` (Tỷ lệ **16:9** — BẮT BUỘC TẠO) |
| `06d_bai_dang_fb*` | `Facebook/` |
| `06e_mega_comments.json` | `Facebook/` (BẮT BUỘC TẠO khi đăng FB) |
| `thumbnail/thumbnail.png` (FB) | `Facebook/` (Tỷ lệ **1.91:1** - 1200x630) |
| `short_01/kich_ban_short.md` | `YouTube_Shorts/` |

### Quy trình Agent 04 khi xuất bản:
1. Tạo thư mục `outputs/YYYY-MM-DD_Ten_Chu_De/`
2. Tạo ngay 3 thư mục con `YouTube/`, `Facebook/` và `YouTube_Shorts/`
3. Lưu file vào đúng thư mục con tương ứng, và nhớ dùng `skills\md_to_docx_v2.py` để tạo đủ file Word.
4. **KHÔNG BAO GIỜ** lưu file trực tiếp vào thư mục gốc của chủ đề.

---

## ⚠️ QUY CHUẨN FILE WORD (.DOCX) — BẮT BUỘC (Rút kinh nghiệm 22/04/2026)

> **Lệnh từ Sếp:** File Word phải xuất ra **tự động** song song với file Markdown. Markdown cho AI đọc, Word cho con người (Đạo diễn, Biên tập viên) làm việc. KHÔNG ĐỢI SẾP NHẮC.

### Quy chuẩn định dạng (cho Đạo diễn/Biên tập viên):
| Thuộc tính | Giá trị |
|---|---|
| Font | **Times New Roman** |
| Cỡ chữ | **14** |
| Khổ giấy | **A4** (21 x 29.7 cm) |
| Lề | **2cm** đều 4 phía (trên, dưới, trái, phải) |
| Căn lề | **Justify** (căn đều 2 bên) |
| Giãn dòng | **1.25 lines** |

### Mã hóa giọng điệu bằng màu sắc:
Mỗi file Word kịch bản PHẢI có hệ thống màu dưới đây để Biên tập viên nhìn màu → biết cách uốn giọng:

| Màu | Mã RGB | Ý nghĩa | Giọng cần đọc |
|---|---|---|---|
| 🔴 **Đỏ** | `(204, 0, 0)` | Nhấn mạnh cực độ, bức xúc, sự thật sốc | Gắt, chắc nịch |
| 🟢 **Xanh lá** | `(0, 128, 0)` | Dữ liệu, con số, năm tháng khách quan | Rành mạch, rõ từng âm tiết |
| 🔵 **Xanh dương** | `(0, 102, 204)` | Mỉa mai, châm biếm, trào phúng | Tưng tửng, cười khẩy |
| 🟠 **Cam** | `(230, 80, 0)` | Câu hỏi, tò mò, gợi mở | Lên giọng cuối câu |
| **In đậm** | — | Punch words — từ khóa cần nhấn âm | Nhấn mạnh lực từ |
| *In nghiêng* | — | Đọc chậm, rải nhịp, tạo khoảng lặng | Hạ giọng, thì thầm |
| <u>Gạch chân</u> | — | Chốt hạ, ngắt nhịp dứt khoát | Pause ngay sau đó |

### Vị trí chú giải bảng màu:
- Đặt ngay **ĐẦU FILE Word**, sau tiêu đề, trước nội dung kịch bản.
- Chú giải phải hiển thị **đúng màu tương ứng** (chữ "Đỏ" phải tô đỏ, chữ "Xanh" phải tô xanh...).

### Tiêu đề A/B Test:
- Đưa thẳng **2 phương án tiêu đề A/B** lên **chóp file kịch bản** (trước chú giải).
- Để Đạo diễn nhìn vào là duyệt ngay, không cần mở file SEO riêng.

---

## ⚠️ QUY CHUẨN `06_kich_ban_hoan_thien.md` — FORMAT AUDIO CLEAN (BẮT BUỘC)

> **File mẫu chuẩn:** `outputs/2026-04-22_Trump_5_Thang_Lich_Su/YouTube/06_kich_ban_hoan_thien.md` + `.docx`
> **Lệnh từ Sếp (27/04/2026):** Mọi kịch bản hoàn thiện `.md` và `.docx` đều PHẢI giống file mẫu chuẩn. KHÔNG ĐƯỢC sai format. KHÔNG CẦN NHẮC LẠI.

### A. Cấu trúc file `.md` (Audio Clean):

```markdown
# Tiêu đề A: [Tiêu đề phương án A]
# Tiêu đề B: [Tiêu đề phương án B]

> **Ngày xuất bản:** YYYY-MM-DD | **Phiên bản:** Clean (Audio Only - Có hướng dẫn giọng điệu)
> **Ghi chú giọng điệu:** <red>Chữ ĐỎ</red>: nhấn mạnh/bức xúc | <green>Chữ XANH LÁ</green>: dữ liệu | <blue>Chữ XANH DƯƠNG</blue>: mỉa mai | <orange>Chữ CAM</orange>: câu hỏi/tò mò | **In đậm**: nhấn âm | *In nghiêng*: đọc chậm | <underline>Gạch chân</underline>: chốt hạ.

---

## HOOK

[Nội dung hook với thẻ màu]

---

## CẦU NỐI

[Nội dung cầu nối]

---

## BỐI CẢNH

[Nội dung bối cảnh]

---

## LỚP 1 — [TÊN LỚP]

[Nội dung]

---

## LỚP 2 — [TÊN LỚP]

[Nội dung]

---

## CAO TRÀO

[Nội dung + CTA]

---

## KẾT THÚC MỞ

[Nội dung kết bài]
```

### B. Quy tắc thẻ màu trong `.md`:

| Thẻ mở | Thẻ đóng | Ý nghĩa | Ví dụ |
|---|---|---|---|
| `<red>` | `</red>` | Nhấn mạnh, bức xúc | `<red>**5 lần trốn lính.**</red>` |
| `<green>` | `</green>` | Dữ liệu, con số | `<green>21 tháng 4</green>` |
| `<blue>` | `</blue>` | Mỉa mai, châm biếm | `<blue>Nghe oai lắm.</blue>` |
| `<orange>` | `</orange>` | Câu hỏi, tò mò | `<orange>Tại sao Trump nói vậy?</orange>` |
| `<underline>` | `</underline>` | Chốt hạ | `<underline>Việt Nam đang bị nhắc tên</underline>` |

**TUYỆT ĐỐI CẤM:**
- ❌ KHÔNG dùng emoji 🔴🟢🔵🟠 để thay thế thẻ màu
- ❌ KHÔNG dùng bảng 2 cột (Visual / Audio) trong bản hoàn thiện (chỉ dùng trong bản nháp)
- ❌ KHÔNG dùng heading có emoji (## ⚡ LỚP 1) — chỉ dùng text thuần
- ❌ KHÔNG có metadata/blockquote trong thân bài (chỉ ở header)

### C. Quy tắc chuyển đổi `.md` → `.docx`:

Script Python (`md_to_docx_v2.py`) PHẢI thực hiện:

1. **Parse thẻ HTML** `<red>`, `<green>`, `<blue>`, `<orange>` → tạo Word runs với `font.color.rgb` tương ứng
2. **Parse `**bold**`** → `run.bold = True`
3. **Parse `*italic*`** → `run.italic = True`
4. **Parse `<underline>`** → `run.underline = True`
5. **Heading `## TÊN`** → đoạn text thường (Normal style), KHÔNG dùng Word Heading style
6. **Divider `---`** → Đoạn `────────────────────────────────────────` với `alignment=CENTER`, `color=C8C8C8`
7. **Text thường không có thẻ** → `color=000000` (đen)
8. **Tiêu đề `# Tiêu đề A/B`** → Đoạn đầu tiên trong Word, font bình thường
9. **Blockquote `> ...`** → Render như text thường (ghi chú giọng điệu)

### D. Specification file `.docx` (tham chiếu từ file mẫu):

| Thuộc tính | Giá trị |
|---|---|
| Normal Style Font | Times New Roman |
| Normal Style Size | 14pt (177800 EMU) |
| Margins | 2cm đều 4 phía (720090 EMU) |
| Page Size | A4 (7560310 x 10692130 EMU) |
| Run-level color | Áp dụng qua `run.font.color.rgb` |
| Run-level bold | Áp dụng qua `run.bold = True` |
| Divider alignment | CENTER |
| Divider color | `#C8C8C8` |
| Section heading | Text thường (KHÔNG dùng Word Heading style) |
| Paragraph alignment | None (left) cho nội dung, CENTER cho divider |

---

## 📌 QUY TẮC HÀNH VĂN NÂNG CAO (Rút kinh nghiệm 22/04/2026)

> **Triết lý Sếp:** Kịch bản phải mượt mà, hài hước mà sâu sắc, thú vị, lôi cuốn. AI phải không ngừng học hỏi.

### Chống lạm dụng dấu gạch ngang (—):
- Dấu gạch ngang chỉ dùng khi tạo **ngắt nhịp kịch tính** hoặc **chèn thông tin phụ**.
- KHÔNG dùng thay từ nối. Dùng **từ nối tự nhiên** (chỉ, mà, rồi, thì).
- ❌ *"giao cho tôi — 5 tháng là xong"* → ✅ *"giao cho tôi chỉ 5 tháng là xong"*

### Câu cảm thán phải KHỚP GIỌNG:
- Nếu đoạn trước đang phân tích nghiêm túc → câu châm biếm sau đó phải tinh tế, không suồng sã.
- ❌ *"Nghe oai lắm. Đến chịu luôn."* → ✅ *"Nghe oai lắm."*

### Câu chuyển ý phải có LỰC và SANG:
- Thể hiện vị thế "người am hiểu mời khách", không ra lệnh.
- ❌ *"Pha ấm trà đi, rồi mình nói chuyện kỹ."*
- ✅ *"Nào, pha ấm trà thôi, rồi mời các bác cùng bàn luận."*
