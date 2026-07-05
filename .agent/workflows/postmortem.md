# Workflow — POSTMORTEM Sau Video

> **Mục đích:** Tự động sinh báo cáo Postmortem sau khi video lên sóng 24h, dùng skill `sred-work-summary` làm retrospective engine.
> **Trigger:** `/rut_kinh_nghiem [video_id]` HOẶC tự động chạy 24h sau publish (nếu có scheduling).
> **Output:** `outputs/[YYYY-MM-DD]_[Topic]/Postmortem/postmortem.md` + `.docx`

---

## Pipeline 5 bước

### Bước 1 — Thu thập số liệu (Agent 01 + script)
- Gọi `scripts/youtube_analytics.py --video [video_id]`
- Output: View, Like, Comment, CTR, Avg View Duration (nếu API kịp cập nhật)
- Đối chiếu Engagement Rate 10h đầu với baseline kênh

### Bước 2 — Thu thập feedback định tính (Agent 01)
- Quét comment YouTube top 50 → sentiment analysis (semantic match → `news-sentiment-engine`)
- Quét comment Facebook fanpage Giải Mã 360 (nếu post 6d đã đăng)
- Quét reaction từ Seeding Mega Comments (Bước 6e)

### Bước 3 — Đối chiếu với checklist gốc (Agent 03)
- Đọc `05_review.md` của video (Compliance Report + 33 tiêu chí ĐẠT/TRƯỢT)
- Tiêu chí nào ĐẠT mà số liệu thực vẫn yếu → ĐÁNG ĐIỀU TRA
- Tiêu chí nào TRƯỢT mà số liệu vẫn ổn → checklist có vấn đề?

### Bước 4 — Áp dụng sred-work-summary (Agent 04)
> Semantic trigger: "Generate postmortem retrospective cho video [topic] với data [số liệu] và feedback [tóm tắt]"

`sred-work-summary` sẽ:
- Group toàn bộ artifacts của video (kịch bản, dàn ý, kiểm định, số liệu, feedback) vào 1 project context
- Sinh structured postmortem doc với các section: **What worked** / **What didn't** / **Surprises** / **Action items**
- Trích xuất pattern có thể tái sử dụng vào Kho Vũ Khí

### Bước 5 — Cập nhật Kho Vũ Khí (Agent 04)
- Nếu phát hiện ví von / hook / lịch sử VN hiệu quả → thêm vào `.shared/kho_vu_khi/[loại].md`
- Nếu phát hiện pattern thất bại → thêm warning vào `ERRORS.md`
- Cập nhật `Learning.md` với 3-5 bullet bài học cụ thể

---

## Format Postmortem Output

```markdown
# POSTMORTEM — [Tên video]
> **Ngày publish:** YYYY-MM-DD | **Ngày postmortem:** YYYY-MM-DD
> **Video ID:** xxx | **Link:** https://youtu.be/xxx

## 📊 Số liệu tác chiến (10h / 24h / 7 ngày)
| Metric | 10h | 24h | 7d | Baseline kênh | Đánh giá |
|---|---|---|---|---|---|
| Views | ... | ... | ... | ... | ✅/⚠️/❌ |
| CTR | ... | ... | ... | ... | ✅/⚠️/❌ |
| Avg View Duration | ... | ... | ... | ... | ✅/⚠️/❌ |
| Like ratio | ... | ... | ... | ... | ✅/⚠️/❌ |
| Comment sentiment | ... | ... | ... | ... | ✅/⚠️/❌ |

## ✅ Điều gì THÀNH CÔNG
- ...

## ❌ Điều gì THẤT BẠI / Yếu
- ...

## 🤯 Bất ngờ (Surprises)
- ...

## 🎯 Action Items (cho video tiếp theo)
- [ ] ...

## 🗡️ Bổ sung Kho Vũ Khí
- Ví von mới: ...
- Hook mới: ...
- Liên hệ VN mới: ...

## ⚠️ Cảnh báo mới cho ERRORS.md
- ...
```

---

## Ràng buộc

1. **Không suy diễn không có data** — số nào không có thì ghi `[CHỜ DATA]`, KHÔNG bịa
2. **Tách định lượng / định tính** — số liệu YouTube Analytics ≠ comment sentiment
3. **Bài học phải CỤ THỂ** — không chấp nhận "cần cải thiện hook" (vô nghĩa); phải là "hook hiện tại dài 90 từ, lần sau ≤ 60 từ"
4. **Cập nhật Kho Vũ Khí tự động** — phát hiện mẫu hay phải lưu lại, không để mất
