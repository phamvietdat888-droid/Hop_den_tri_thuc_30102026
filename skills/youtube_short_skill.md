# ⚡ SKILL YOUTUBE SHORTS — Chuyển Thể Kịch Bản Dài Thành Video Ngắn
> **Phiên bản:** 1.0 | **Ngày tạo:** 2026-04-29
> **Vai trò:** Shorts Content Factory — "Nhà máy sản xuất video ngắn"
> **Vị trí:** Chạy SAU Pipeline chính (sau khi có kịch bản dài hoàn chỉnh)
> **Triết lý:** 1 kịch bản dài = 2-3 Shorts. Shorts là "phễu" kéo khán giả về video dài.

---

## 🎯 SỨ MỆNH

Biến mỗi kịch bản YouTube dài (~10 phút) thành **2-3 video Shorts (≤50 giây)** hoàn chỉnh, bao gồm:
- 🎬 **Kịch bản Short** (≤150 từ, Hook 2 giây, CTA trỏ về video dài)
- 🖼️ **10 ảnh minh họa 9:16** (portrait, chi tiết, sát kịch bản)
- 📝 **Toàn bộ prompt tạo ảnh** (tiếng Anh, chi tiết, tái sử dụng được)
- 🎨 **Ảnh thu nhỏ (Thumbnail)** riêng cho Short
- 📋 **Tiêu đề + Mô tả + SEO** riêng cho Short

**Đối tượng:** Nam giới Việt Nam 25-50 tuổi, lướt Shorts trên điện thoại.
**Tone:** Sốc — Nhanh — Gọn — Gây tò mò xem bản Full.

---

## 🔗 KẾT NỐI HỆ SINH THÁI

| Skill nguồn | Vai trò |
|---|---|
| `giai_ma_360_skill.md` | Cung cấp kịch bản dài hoàn chỉnh (input) |
| `viet_tieu_de_skill.md` | 13 Formula tiêu đề → áp dụng cho tiêu đề Short |
| `do_hoa_fanpage_skill.md` | Template prompt ảnh Geopolitical Art → kế thừa style |
| `kham_kenh_skill.md` | Data CTR/AVD → feedback cải thiện Short |

---

## 📂 CẤU TRÚC THƯ MỤC OUTPUT

```
outputs/[YYYY-MM-DD]_[Tên_Chủ_Đề]/
├── YouTube/                          ← Video dài (đã có)
│   ├── 06_kich_ban_hoan_thien.md
│   ├── 06b_goi_seo.md
│   └── thumbnail.png
│
├── YouTube_Shorts/                   ← THƯ MỤC MỚI
│   ├── short_01/
│   │   ├── kich_ban_short.md         ← Kịch bản Short (≤150 từ)
│   │   ├── kich_ban_short.docx       ← Bản DOCX để đọc/in (MỚI)
│   │   ├── tieu_de_seo.md            ← Tiêu đề + Mô tả + Tags
│   │   ├── tieu_de_seo.docx          ← Bản DOCX SEO (MỚI)
│   │   ├── prompt_anh.md             ← 10 prompt tạo ảnh chi tiết
│   │   └── images/                   ← Thư mục chứa ảnh (MỚI)
│   │       ├── anh_01.png → anh_10.png
│   │       └── thumbnail_short.png
│   │
│   ├── short_02/
│   │   ├── (cấu trúc tương tự)
│   │   └── ...
│   │
│   └── short_03/ (nếu có)
│       └── ...
│
└── Facebook/                         ← Bài Fanpage (đã có)
```

---

## ⚙️ PIPELINE SẢN XUẤT — 7 BƯỚC

```
[Kịch bản dài hoàn chỉnh: 06_kich_ban_hoan_thien.md]
       │
       ▼
[BƯỚC 1] Phân tích & Chiết xuất Ý chính
       │  → Xác định 2-3 "mảnh vàng" từ kịch bản dài
       ▼
[BƯỚC 2] Viết Kịch bản Short (≤150 từ, ≤50 giây)
       │  → Hook 2s + Thân 40s + CTA 8s
       ▼
[BƯỚC 3] Tạo Tiêu đề + SEO cho Short
       │  → 5 tiêu đề viral + Mô tả + Tags
       ▼
[BƯỚC 4] Thiết kế 10 Prompt ảnh chi tiết
       │  → Mỗi prompt = 1 cảnh trong kịch bản, tỷ lệ 9:16
       ▼
[BƯỚC 5] Tạo 10 ảnh minh họa 9:16
       │  → generate_image × 10 (tự động, SafeToAutoRun=true)
       ▼
[BƯỚC 6] Tạo Thumbnail Short
       │  → 1 ảnh 9:16 nổi bật, khác biệt với 10 ảnh trên
       ▼
[BƯỚC 7] Đóng gói & Lưu trữ
       │  → Ghi tất cả vào thư mục YouTube_Shorts/short_XX/
       ▼
[BƯỚC 8] Chuyển đổi sang DOCX
       │  → Chạy python md_to_docx_v2.py cho kịch bản & SEO
       ▼
[HOÀN TẤT] Báo cáo Sếp
```

> [!IMPORTANT]
> **Chính sách tự động:** Toàn bộ 7 bước chạy TỰ ĐỘNG sau khi Sếp ra lệnh. Không Gate Check. Sếp chỉ cần gõ `/tao_short [tên chủ đề]` và chờ kết quả.

---

## 📝 CHI TIẾT TỪNG BƯỚC

---

### BƯỚC 1: PHÂN TÍCH & CHIẾT XUẤT Ý CHÍNH

**Input:** Kịch bản dài `06_kich_ban_hoan_thien.md`

**Quy trình:**
1. Đọc toàn bộ kịch bản dài
2. Xác định các **"mảnh vàng"** — những đoạn có tiềm năng viral cao nhất khi đứng độc lập:

| Tiêu chí chọn "mảnh vàng" | Giải thích |
|---|---|
| Có con số gây sốc | VD: "1,7 triệu tỷ đồng", "giá xăng tăng 30%" |
| Có mâu thuẫn/xung đột | VD: "UAE vừa 'đâm sau lưng' OPEC" |
| Có ảnh hưởng trực tiếp đến túi tiền | VD: "Giá xăng Việt Nam sẽ ra sao?" |
| Có yếu tố bất ngờ | VD: "Điều không ai ngờ tới là..." |
| Có thể đứng độc lập (không cần context) | Người xem hiểu được mà không cần xem video dài |

3. Chọn **2-3 mảnh vàng** → Mỗi mảnh = 1 Short

**Output:** Danh sách 2-3 ý chính, mỗi ý kèm:
- Tên ngắn (VD: "Giá xăng VN sau khi UAE rời OPEC")
- Tóm tắt nội dung (2-3 câu)
- Lý do chọn (tiêu chí nào ở trên)

---

### BƯỚC 2: VIẾT KỊCH BẢN SHORT

**Quy tắc vàng:**
- **Tối đa 150 từ** (đọc tự nhiên trong ~45-50 giây)
- **KHÔNG mở đầu bằng giới thiệu** — vào thẳng vấn đề
- **Cấu trúc 3 phần cứng:** Hook (2s) → Thân (40s) → CTA (8s)

#### Cấu trúc kịch bản Short:

```markdown
## ⚡ KỊCH BẢN SHORT: [Tên Short]
> Thời lượng: ~[XX] giây | Số từ: [XXX]/150

### 🔴 HOOK (0s-2s) — Câu đầu tiên người xem nghe
> Quy tắc: SỐC + CỤ THỂ. Phải khiến ngón tay dừng lướt.

"[Câu hook — VD: 'Giá xăng Việt Nam sắp tăng 30% — và đây là lý do.']"

### 📖 THÂN (2s-42s) — Nội dung chính
> Quy tắc: Mỗi câu ≤ 15 từ. Nhịp nhanh. Không giải thích dài dòng.

[Nội dung — chia thành 5-7 câu ngắn, mỗi câu 1 dòng]

### 🎯 CTA (42s-50s) — Kêu gọi hành động
> Quy tắc: Trỏ về video dài. Tạo FOMO.

"[CTA — VD: 'Muốn biết 3 kịch bản giá xăng sắp tới? Link video đầy đủ ở trên.']"
```

#### 7 Công thức Hook cho Shorts:

| # | Formula | Ví dụ | Khi nào dùng |
|---|---|---|---|
| H1 | **Con số + Hệ quả** | "1,7 triệu tỷ đồng vừa bốc hơi — và nó ảnh hưởng đến VÍ TIỀN bạn." | Bài kinh tế, tài chính |
| H2 | **Câu hỏi gây tò mò** | "Tại sao UAE vừa 'phản bội' OPEC?" | Bài phân tích nguyên nhân |
| H3 | **Tuyên bố sốc** | "Giá xăng Việt Nam sắp tăng 30%." | Bài dự báo, cảnh báo |
| H4 | **Mâu thuẫn** | "Một quốc gia vừa giàu thêm — còn bạn vừa nghèo đi." | Bài so sánh, bất công |
| H5 | **Thời sự nóng** | "Chuyện vừa xảy ra sáng nay sẽ thay đổi giá xăng VN." | Breaking news |
| H6 | **Bí mật/Ít ai biết** | "Có 1 điều về UAE mà 99% người Việt không biết." | Bài insight, góc khuất |
| H7 | **Đếm ngược** | "3 điều bạn CẦN BIẾT trước khi giá xăng tăng." | Bài listicle ngắn |

#### Quy tắc viết thân Short:

| Quy tắc | Đúng ✅ | Sai ❌ |
|---|---|---|
| Câu ngắn | "UAE vừa rời OPEC." | "UAE, một quốc gia giàu có ở Trung Đông, vừa quyết định rời khỏi tổ chức OPEC." |
| Cụ thể | "Giá xăng có thể tăng 2.000đ/lít." | "Giá xăng sẽ bị ảnh hưởng." |
| Nhịp nhanh | Mỗi câu 1 ý. Chấm. Xuống dòng. | Một đoạn dài liên tục không ngắt |
| Không giải thích | "OPEC kiểm soát 40% dầu thế giới." | "OPEC, viết tắt của Tổ chức các nước xuất khẩu dầu mỏ, là một liên minh..." |

---

### BƯỚC 3: TẠO TIÊU ĐỀ + SEO CHO SHORT

#### Tiêu đề Short (khác tiêu đề video dài):

| Tiêu chí | Video dài | Short |
|---|---|---|
| Độ dài | ≤ 55 ký tự | ≤ 40 ký tự (hiển thị đầy đủ trên feed Shorts) |
| Tone | Phân tích, sâu sắc | Sốc, nhanh, gây tò mò |
| Emoji | Không dùng | Dùng 1-2 emoji ở đầu/cuối |
| Hashtag | Không | Thêm #Shorts #[chủ đề] |

**Tạo 5 tiêu đề**, chọn Top 1 làm tiêu đề chính:

```markdown
## 📋 5 TIÊU ĐỀ SHORT

1. 🔥 [Tiêu đề 1 — Formula H1]
2. 😱 [Tiêu đề 2 — Formula H3]
3. ⚡ [Tiêu đề 3 — Formula H5]
4. 🇻🇳 [Tiêu đề 4 — Formula H2]
5. 💰 [Tiêu đề 5 — Formula H4]

🏆 **TOP 1 (Đề xuất):** [Tiêu đề X]
📌 **Lý do:** [Giải thích ngắn tại sao tiêu đề này sẽ cho CTR cao nhất]
```

#### Mô tả Short (≤100 từ):

```markdown
[Câu tóm tắt hấp dẫn — 1 dòng]

👉 Xem PHÂN TÍCH ĐẦY ĐỦ: [link video dài]
📢 Đăng ký kênh Giải Mã 360 để không bỏ lỡ!

#Shorts #[Chủđề1] #[Chủđề2] #[Chủđề3] #NhậtKýTácChiến
```

#### Tags SEO (10 tags):

```
[tag1], [tag2], ..., [tag10]
```

> Quy tắc: 5 tags chủ đề cụ thể + 3 tags trending + 2 tags kênh

---

### BƯỚC 4: THIẾT KẾ 10 PROMPT ẢNH CHI TIẾT

**Mục tiêu:** Mỗi ảnh minh họa 1 cảnh/ý trong kịch bản Short. Khi Sếp ghép 10 ảnh theo thứ tự → thành 1 "slideshow" kể chuyện hoàn chỉnh.

#### Quy tắc prompt ảnh:

| Quy tắc | Chi tiết |
|---|---|
| **Tỷ lệ** | 9:16 (portrait, tối ưu cho Shorts/TikTok/Reels) |
| **Phong cách** | Geopolitical Art, Dark Cinematic (kế thừa từ `do_hoa_fanpage_skill.md`) |
| **Không text** | TUYỆT ĐỐI không yêu cầu AI viết chữ trên ảnh |
| **Không mặt người thật** | Dùng silhouette, bóng đổ, góc xa, biểu tượng |
| **Tone màu** | Đỏ (#CC0000), Vàng gold (#C5973E), Navy (#1a3a6b), Đen (#1A1A1A) |
| **Ánh sáng** | Cinematic, dramatic, low-key lighting |
| **Chi tiết cao** | Mỗi prompt ≥ 50 từ tiếng Anh, mô tả cụ thể bố cục + ánh sáng + biểu tượng |
| **Trình bày** | **BẮT BUỘC** đặt prompt trong ô mã (code block) để người dùng dễ copy |

#### Template prompt cho mỗi ảnh:

```
[Scene description] in dramatic geopolitical illustration style,
portrait format 9:16, vertical composition optimized for mobile viewing,
[specific symbolic elements],
[specific lighting: dramatic rim lighting / cinematic golden hour / dark moody],
[specific color palette: dark background with red and gold accents],
highly detailed, 4K quality,
no text, no watermarks, no recognizable human faces
```

#### Bảng phân bổ 10 ảnh theo kịch bản:

| Ảnh # | Phân đoạn | Nội dung minh họa | Phong cách |
|---|---|---|---|
| 01 | **HOOK** (0-2s) | Ảnh sốc, gây chú ý, tương phản mạnh | Bold, dramatic |
| 02 | Thân — Ý 1 (3-8s) | Bối cảnh/nguyên nhân | Establishing shot |
| 03 | Thân — Ý 1 (8-13s) | Chi tiết bổ sung | Close-up symbolic |
| 04 | Thân — Ý 2 (13-18s) | Diễn biến/xung đột | Dynamic, tension |
| 05 | Thân — Ý 2 (18-23s) | Cao trào xung đột | Peak drama |
| 06 | Thân — Ý 3 (23-28s) | Hệ quả/tác động | Impact visualization |
| 07 | Thân — Ý 3 (28-33s) | Tác động đến VN/người dân | Localized, personal |
| 08 | Thân — Kết luận (33-38s) | Tổng kết, toàn cảnh | Wide angle, overview |
| 09 | **CTA** (38-45s) | Gợi mở, tạo tò mò xem thêm | Mystery, cliffhanger |
| 10 | **CTA** (45-50s) | Branding/kênh — ảnh kết thúc | Clean, branded feel |

#### Output Bước 4 — File `prompt_anh.md`:

```markdown
# 🖼️ 10 PROMPT ẢNH — SHORT: [Tên Short]

## Ảnh 01: [Tên cảnh — VD: "Cú sốc giá dầu"]
> Phân đoạn: HOOK (0-2s)
> Mô tả VN: [Mô tả ngắn bằng tiếng Việt để Sếp hiểu ảnh sẽ trông như nào]

**Prompt:**
```
[Prompt tiếng Anh đầy đủ ≥50 từ]
```

## Ảnh 02: [Tên cảnh]
...
(lặp lại cho 10 ảnh)
```

---

### BƯỚC 5: TẠO 10 ẢNH MINH HỌA 9:16

**Tool:** `generate_image` × 10

**Quy trình:**
1. Đọc 10 prompt từ `prompt_anh.md`
2. Gọi `generate_image` lần lượt cho từng prompt. Lưu ảnh: `anh_01.png` → `anh_10.png` vào thư mục `short_XX/images/`
3. Nếu `generate_image` lỗi (ví dụ: lỗi 503) → Kích hoạt **Plan B (Tự động hóa trình duyệt)**:
   - Gọi `browser_subagent` tự động truy cập: `https://labs.google/fx/vi/tools/flow/project`.
   - Sử dụng phiên đăng nhập mặc định của trình duyệt.
   - Tạo dự án mới tên theo chủ đề Short.
   - Paste lần lượt 11 prompt (10 ảnh minh họa + 1 thumbnail) vào công cụ.
   - Thiết lập để tạo **2 ảnh cho mỗi prompt**.
   - Tải tất cả kết quả về thư mục `short_XX/images/`.

> [!IMPORTANT]
> **SafeToAutoRun=true** cho tất cả 10 lần generate. Không hỏi Sếp.

---

### BƯỚC 6: TẠO THUMBNAIL SHORT

**Thumbnail Short khác ảnh minh họa:**
- Phải **nổi bật** hơn 10 ảnh kia (vì đây là ảnh đầu tiên khán giả thấy)
- Phải **khác biệt** (không lặp lại ảnh 01)
- Tỷ lệ **9:16**, tối ưu mobile

**Quy tắc Thumbnail Short:**

| Yếu tố | Quy tắc |
|---|---|
| Bố cục | Đơn giản, 1 focal point duy nhất |
| Màu sắc | Tương phản cao (đỏ/vàng trên nền tối) |
| Biểu tượng | 1 biểu tượng lớn, dễ nhận biết ở kích thước nhỏ |
| Cảm xúc | Gây tò mò hoặc sốc |
| Text | KHÔNG (YouTube tự hiện tiêu đề bên dưới) |

**Template prompt Thumbnail:**
```
[Main symbolic element] as a dramatic focal point,
portrait 9:16, centered composition,
dark background with [red/gold] dramatic lighting,
single powerful symbolic image, eye-catching contrast,
cinematic quality, highly detailed,
designed to grab attention on mobile phone screen,
no text, no watermarks, no recognizable human faces
```

---

### BƯỚC 7: ĐÓNG GÓI & LƯU TRỮ

Ghi tất cả file vào đúng cấu trúc thư mục:

```
YouTube_Shorts/short_01/
├── kich_ban_short.md      ← Bước 2
├── kich_ban_short.docx    ← Bước 8
├── tieu_de_seo.md         ← Bước 3
├── tieu_de_seo.docx       ← Bước 8
├── prompt_anh.md          ← Bước 4
└── images/                ← Bước 5 & 6
    ├── anh_01.png → anh_10.png
    └── thumbnail_short.png
```

### BƯỚC 8: CHUYỂN ĐỔI SANG DOCX

Sử dụng script `md_to_docx_v2.py` trong thư mục `scripts/` để chuyển đổi các file `.md` sau sang định dạng Word:
1. `kich_ban_short.md` → `kich_ban_short.docx`
2. `tieu_de_seo.md` → `tieu_de_seo.docx`

**LƯU Ý:** Riêng file `prompt_anh.md` BẮT BUỘC giữ nguyên định dạng `.md`, tuyệt đối KHÔNG chuyển sang `.docx`.

**Quy chuẩn DOCX:** Times New Roman 14pt, chuẩn màu HTML tags (<red>, <green>, <blue>, <orange>).

---

**Báo cáo hoàn tất cho Sếp:**
```markdown
══════════════════════════════════════════════════
⚡ SHORTS ĐÃ SẴN SÀNG — [Tên chủ đề]
══════════════════════════════════════════════════

📦 Đã tạo: [2/3] Shorts

### Short 01: [Tên]
- 🎬 Kịch bản: [XX] từ / ~[XX]s
- 🏆 Tiêu đề: "[Tiêu đề đã chọn]"
- 📄 Bản Word: kich_ban_short.docx ✅
- 🖼️ Ảnh: 10/10 ✅
- 🎨 Thumbnail: ✅
- 📂 Thư mục: outputs/[...]/YouTube_Shorts/short_01/

### Short 02: [Tên]
- (tương tự)

🎯 BƯỚC TIẾP THEO:
→ Sếp quay video dài + 2 Shorts cùng lúc (tiết kiệm setup)
→ Đăng video dài trước, Shorts đăng sau 24h
══════════════════════════════════════════════════
```

---

## 📏 QUY TẮC VẬN HÀNH

### 1. Shorts KHÔNG phải bản cắt ngắn
- **KHÔNG** cắt 50 giây đầu tiên của video dài → làm Short
- **PHẢI** viết lại hoàn toàn: hook mới, nhịp mới, CTA mới

### 2. Mỗi Short phải đứng độc lập
- Người xem CHƯA BAO GIỜ xem video dài vẫn phải hiểu được Short
- Không viết: "Như mình đã nói ở video trước..."

### 3. Lịch đăng Short
- Đăng video dài **TRƯỚC** → Shorts đăng **SAU 24-48h**
- Lý do: Để video dài có thời gian "chạy" trước, tránh Shorts "ăn" view của video dài

### 4. Ảnh phải kể chuyện
- 10 ảnh khi xem liên tiếp phải tạo thành 1 câu chuyện hình ảnh hoàn chỉnh
- Mỗi ảnh phải khác biệt rõ ràng (không 2 ảnh giống nhau)

### 5. Tự động hóa triệt để
- Toàn bộ 7 bước chạy tự động, KHÔNG dừng hỏi Sếp
- Nếu generate_image lỗi → ghi prompt vào file + thông báo, KHÔNG dừng pipeline

---

## ⚡ SLASH COMMANDS

| Lệnh | Chức năng |
|---|---|
| `/tao_short [tên chủ đề]` | Tạo 2-3 Shorts từ kịch bản dài có sẵn (Full pipeline 7 bước) |
| `/tao_short [tên chủ đề] 1` | Chỉ tạo 1 Short (ý chính nhất) |

**Ví dụ:**
```
/tao_short UAE Rời OPEC
→ Tìm kịch bản trong outputs/2026-04-29_UAE_Roi_OPEC/YouTube/
→ Chiết xuất 2-3 ý chính
→ Viết 2-3 kịch bản Short
→ Tạo 10 ảnh × 2-3 Shorts
→ Tự động convert sang DOCX (MỚI)
→ Lưu vào outputs/2026-04-29_UAE_Roi_OPEC/YouTube_Shorts/
```

---

## 📎 THAM CHIẾU

| Tài liệu | Đường dẫn |
|---|---|
| Pipeline sản xuất dài | `skills/giai_ma_360_skill.md` |
| 13 Formula tiêu đề | `skills/viet_tieu_de_skill.md` |
| Template ảnh Geopolitical | `skills/do_hoa_fanpage_skill.md` |
| Khám kênh (feedback data) | `skills/kham_kenh_skill.md` |
| Kho Vũ Khí | `.shared/kho_vu_khi/` |

---

> **Ghi nhớ:** Shorts là "mồi câu" — ngắn gọn, sốc, tạo tò mò. Video dài là "bữa chính" — sâu, chi tiết, giữ chân. Hai thứ này phải hoạt động như một cặp đôi, không phải đối thủ của nhau.
