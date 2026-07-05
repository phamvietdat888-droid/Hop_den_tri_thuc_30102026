# 📘 HƯỚNG DẪN SỬ DỤNG — Hệ thống Giải Mã 360 (v2.1)

---

## Bắt đầu nhanh

### Kịch bản 1: Chưa có chủ đề → Trinh sát trước

**Bước 1:** Gõ `/tim_trend` hoặc `/tim_trend [từ khóa]`
→ Hệ thống quét 6 nguồn: Google Trends (ưu tiên) + Báo VN + Báo quốc tế + Facebook đối thủ + YouTube đối thủ + X/Reddit
→ Trả về: Top 5 chủ đề đáng làm nhất + Tình báo đối thủ + Gợi ý tiêu đề

**Bước 2:** Sếp chọn chủ đề
→ Nói: "Làm chủ đề số 1" hoặc `/tac_chien [chủ đề đã chọn]`
→ Pipeline tự động chạy từ Bước 1.

### Kịch bản 2: Đã có chủ đề → Tác chiến luôn

**Bước 1:** Gõ `/tac_chien [chủ đề]`
→ Hệ thống chạy Pipeline 7 bước (1-7).

---

## Các điểm DỪNG chờ Sếp

| Bước | Sếp cần làm gì |
|---|---|
| **Bước 0** | Chọn 1 trong Top 5 chủ đề trinh sát |
| **Bước 2** | Chọn 1 trong 5 Angle đề xuất |
| **Bước 3** | Duyệt dàn ý |
| **Bước 6** | Duyệt bản cuối |

---

## Cấu trúc file cho mỗi video

```
drafts/YYYY-MM-DD_ten_chu_de/
├── 01_brief.md          ← Đề bài
├── 02_angle.md          ← 5 góc tiếp cận
├── 03_outline.md        ← Dàn ý chi tiết
├── 04_script_draft.md   ← Kịch bản nháp
├── 05_review.md         ← Báo cáo kiểm định
├── 06_kich_ban_hoan_thien.md   ← Bản cuối (copy sang outputs/)
└── 07_postmortem.md     ← Rút kinh nghiệm (sau khi lên sóng)
```

---

## Sau khi video lên sóng (48-72h)

Gõ: `/rut_kinh_nghiem`
→ Cung cấp data YouTube (Views, Retention, CTR, Comments)
→ Hệ thống phân tích & cập nhật Kho Vũ Khí + Learning.md

---

## Tips vàng

1. **Bắt đầu bằng `/tim_trend`** — đừng đoán mò, để data dẫn đường
2. **Google Trends là vua** — nếu GT VN không tăng, khó viral tại VN
3. **Đối thủ là la bàn** — nếu TTT vừa làm cùng chủ đề, mình phải có góc nhìn KHÁC hoặc SÂU HƠN
4. **Đừng bỏ qua Postmortem** — đây là cách duy nhất kênh tiến bộ
5. **Kiểm tra Kho Vũ Khí** trước khi viết — tránh lặp ví von cũ
6. **Nỗi đau phải CỤ THỂ** — nói "giá giày" chứ đừng nói "hàng hóa tiêu dùng"
7. **Liên hệ lịch sử VN không tự nhiên → bỏ qua** — đừng ép
8. **Timing là tất cả** — video đúng thời điểm ×10 hiệu quả video muộn
