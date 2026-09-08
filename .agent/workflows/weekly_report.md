---
name: weekly-report
description: "Tổng hợp báo cáo hoạt động theo tuần, tháng hoặc khoảng ngày."
---

# Workflow — BÁO CÁO TUẦN / THÁNG (Auto-Generated)

> **Mục đích:** Tự động sinh báo cáo tuần/tháng dùng skill `sred-project-organizer` — Sếp không cần gõ tay.
> **Phiên bản:** 1.0 — Phase 3 v3.0
> **Output:** `outputs/_reports/YYYY-MM-DD_weekly.md` + `.docx`

---

## 1. Khi nào chạy

| Tần suất | Trigger | Output |
|---|---|---|
| **Tuần** | Mỗi Chủ nhật 21:00 (hoặc Sếp gõ `/bao_cao_tuan`) | `_reports/YYYY-WW_weekly.md` |
| **Tháng** | Ngày 1 tháng sau, 09:00 (hoặc `/bao_cao_thang`) | `_reports/YYYY-MM_monthly.md` |
| **Ad-hoc** | Sếp gõ `/bao_cao [từ ngày X đến ngày Y]` | `_reports/[range].md` |

---

## 2. Pipeline 4 bước

### Bước 1 — Thu thập artifacts (Agent 04)
- Quét `outputs/` tìm tất cả project folder có `_progress.md` được cập nhật trong khoảng thời gian
- Quét `Postmortem/postmortem.md` của các video đã publish
- Quét `Learning.md` (entries mới)
- Quét `Đối_thủ/bao_cao_tinh_bao.md` (cập nhật mới)

### Bước 2 — Format với sred-project-organizer
> Semantic trigger: "Generate weekly report theo sred-project-organizer cho khoảng [date range], dùng artifacts từ outputs/, postmortems, Learning.md"

`sred-project-organizer` sẽ:
- Group artifacts theo project (1 project = 1 video)
- Format structured report với section: Projects completed / In progress / Blocked
- Tính metrics tổng: số video publish, avg checklist score, avg retention, top theme

### Bước 3 — Bổ sung phân tích chiến lược (Agent 00)
- Đối thủ tuần này nói gì → có cơ hội đánh đối chiếu không?
- Chủ đề nào lên top mà mình chưa làm → ghi vào backlog
- Pattern thắng/thua từ Postmortem → đề xuất 3 action items cho tuần tới

### Bước 4 — Xuất sản phẩm
- Markdown → DOCX qua `scripts/md_to_docx_v2.py`
- Lưu vào `outputs/_reports/`
- (Tùy chọn) Gửi link cho Sếp qua kênh thông báo

---

## 3. Format Báo cáo Tuần

```markdown
# BÁO CÁO TUẦN — Tuần WW/YYYY (DD-MM → DD-MM)

## 📊 Tóm tắt số
- Video publish: X (target tuần: Y)
- Avg checklist score: XX.X / 100 (baseline: 85)
- Tổng view 24h đầu: ... 
- Tổng view 7 ngày: ...
- Top video: [tên] — X view
- Đáy video: [tên] — X view

## 🟢 Project HOÀN THÀNH tuần này
- [video_1]: publish DD-MM, checklist YY/100, retention ZZ%
- [video_2]: ...

## 🟡 Project ĐANG SẢN XUẤT
- [video_3]: đang ở Bước 4, ETA DD-MM
- [video_4]: chờ Gate 2 (Sếp duyệt dàn ý)

## ❌ Project BLOCKED
- (nếu có)

## 🎯 Postmortem highlights
- Bài học nổi bật từ video tuần này: ...
- Pattern thắng phát hiện: ...
- Pattern thất bại cần tránh: ...

## 🕵️ Đối thủ tuần này
- Kênh A: làm chủ đề ... (X view) — ta có nên đánh đối chiếu?
- Kênh B: ...

## 🔥 Backlog đề xuất (từ trinh sát)
- Chủ đề chưa làm mà đang nóng: ...

## 🎬 Action items cho tuần tới
- [ ] ...
- [ ] ...

## 📚 Kho Vũ Khí cập nhật
- Ví von mới thêm: ...
- Hook mới: ...
```

---

## 4. Ràng buộc

1. **Không bịa số** — số nào không có data → ghi `[CHỜ DATA]`, không gán "0" hay ước lượng.
2. **Action items phải CỤ THỂ** — không chấp nhận "cần cải thiện X". Phải có owner + deadline + tiêu chí đo lường.
3. **Backlog đề xuất phải kèm justification** — vì sao chủ đề này nên làm tuần sau (nóng / đối thủ chưa làm / phù hợp persona).
4. **Báo cáo phải ĐỌC ĐƯỢC trong 3 phút** — Sếp bận, không có thời gian đọc 10 trang. Section nào trống thì ghi "(không có)" thay vì padding.

---

## 5. Trigger semantic

```
# Tuần
"sred-project-organizer: tạo báo cáo tuần [Tuần WW/YYYY] 
cho GM360 dùng artifacts từ outputs/ và Postmortem/"

# Tháng (rollup từ 4 báo cáo tuần)
"sred-project-organizer: tổng hợp báo cáo tháng [MM/YYYY] 
từ 4 báo cáo tuần trong _reports/, thêm trend analysis"
```
