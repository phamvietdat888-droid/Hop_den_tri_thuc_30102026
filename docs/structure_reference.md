# 📐 STRUCTURE REFERENCE — CẤU TRÚC THƯ MỤC VÀ ĐỊNH DẠNG SẢN PHẨM HOÀN CHỈNH

> **Cập nhật:** 2026-07-30 | **Phiên bản:** v3.3 (Quy chuẩn phân nhánh Nền tảng)  
> **Quy tắc bất biến:** Mỗi dự án sản xuất video khi xuất bản ở Bước 6 bắt buộc phải tổ chức thành 3 thư mục con độc lập trong `outputs/YYYY-MM-DD_Ten_Chu_De/`: `YouTube/`, `Facebook/`, `YouTube_Shorts/`.

---

## 1. CẤU TRÚC THƯ MỤC BẮT BUỘC TRONG `outputs/YYYY-MM-DD_Ten_Chu_De/`

```text
outputs/YYYY-MM-DD_Ten_Chu_De/
├── YouTube/
│   ├── 06_kich_ban_hoan_thien.docx     ← Bản giao cho Sếp (Clean Audio / MC Teleprompter + màu đọc giọng + 10 Shorts CTA)
│   ├── 06_kich_ban_hoan_thien.md       ← Bản nháp kỹ thuật nội bộ (Clean Audio / MC Teleprompter)
│   ├── 06b_goi_seo.docx                ← Bản giao cho Sếp (20 Tiêu đề + Mô tả 250 từ + 20 Tags)
│   ├── 06b_goi_seo.md                  ← Bản nháp kỹ thuật nội bộ
│   ├── thumbnail_prompt.md             ← File Markdown prompt tạo ảnh Thumbnail 16:9 + link ảnh
│   └── thumbnail.png                   ← File ảnh Thumbnail YouTube (16:9)
│
├── Facebook/
│   ├── 06d_bai_dang_fb.docx            ← Bản giao cho Sếp (Bài đăng Fanpage Giải Mã 360 C.R.A.F.T 500-800 từ)
│   ├── 06d_bai_dang_fb.md              ← Bản nháp kỹ thuật nội bộ
│   ├── 06e_mega_comments.json          ← Gói Seeding Mega Comments (5 comment + 2 CTA)
│   └── facebook_art.png (tùy chọn)     ← Ảnh minh họa bài đăng Facebook (6:16 portrait)
│
└── YouTube_Shorts/
    ├── short_01/
    │   ├── kich_ban_short.docx         ← Bản giao cho Sếp (Short 1 ≤ 50s + Prompt ảnh 9:16 + CTA)
    │   └── kich_ban_short.md           ← Bản nháp kỹ thuật nội bộ
    ├── short_02/
    │   ├── kich_ban_short.docx         ← Short 2
    │   └── kich_ban_short.md
    └── short_03/
        ├── kich_ban_short.docx         ← Short 3
        └── kich_ban_short.md
```

---

## 2. QUY ĐỊNH ĐỊNH DẠNG FILE CHI TIẾT

### 2.1 Thư mục `YouTube/`
- **`06_kich_ban_hoan_thien.md` / `.docx`:** 
  - Định dạng: Clean Audio / MC Teleprompter format.
  - Có phần **Ghi chú giọng điệu màu sắc**:
    - `<red>Chữ ĐỎ</red>`: nhấn mạnh / bức xúc
    - `<green>Chữ XANH LÁ</green>`: dữ liệu / văn bản luật
    - `<blue>Chữ XANH DƯƠNG</blue>`: mỉa mai tinh tế
    - `<orange>Chữ CAM</orange>`: câu hỏi / tò mò
    - **In đậm**: nhấn âm
    - *In nghiêng*: đọc chậm rãi
    - `<underline>Gạch chân</underline>`: chốt hạ
  - Có đầy đủ các phần: `HOOK`, `CẦU NỐI`, `BỐI CẢNH`, `LỚP 1`, `LỚP 2`, `LỚP 3`, `CAO TRÀO`, `KẾT THÚC MỜ`.
  - Cuối kịch bản dài **BẮT BUỘC đính kèm 10 đoạn Shorts kịch bản độc lập bối cảnh + CTA** điều hướng về video dài.
- **`06b_goi_seo.md` / `.docx`:** 20 tiêu đề (chia 5 angle), mô tả video 250 từ chuẩn SEO (có Timestamps, Hashtags, Subscribe link), 20 từ khóa SEO tags.
- **`thumbnail_prompt.md`:** Prompt tiếng Anh chi tiết tạo ảnh 16:9 + nhúng ảnh demo.

### 2.2 Thư mục `Facebook/`
- **`06d_bai_dang_fb.md` / `.docx`:** Bài đăng Fanpage Facebook Giải Mã 360 chuẩn framework C.R.A.F.T (Context, Reality, Analysis, Financial truth, Takeaway), độ dài 500 – 800 từ, hành văn tự nhiên, có emoji và CTA rõ ràng.
- **`06e_mega_comments.json`:** 5 Mega Comments đa góc nhìn + 2 CTA điều hướng.

### 2.3 Thư mục `YouTube_Shorts/`
- Chứa 2 - 3 thư mục con `short_01/`, `short_02/`, `short_03/`.
- Mỗi thư mục con chứa `kich_ban_short.md` và `kich_ban_short.docx` (kịch bản nói 2 cột ≤ 50 giây + Prompt ảnh 9:16 + Hashtags + CTA cố định).

---

## 3. QUY TRÌNH XUẤT BẢN TỰ ĐỘNG (Dành cho Agent 04_Publisher & 00_Coordinator)

1. Khi Gate 2 được duyệt, tạo 3 thư mục: `YouTube/`, `Facebook/`, `YouTube_Shorts/`.
2. Tạo các bản nháp `.md` và `.json` trong từng thư mục tương ứng.
3. Chạy script `md_to_docx_v2.py` chuyển đổi tất cả file `.md` thành `.docx`.
4. Chỉ trình bày đường dẫn `.docx` (và `.md` prompt ảnh) cho Sếp trong đoạn chat báo cáo.
