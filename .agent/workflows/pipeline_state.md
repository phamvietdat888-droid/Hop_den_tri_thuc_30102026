# Workflow — PIPELINE STATE (Persistent Working Memory)

> **Mục đích:** Áp dụng skill `planning-with-files` để mỗi project (1 video) có **"bộ nhớ làm việc trên đĩa"** dạng markdown — Sếp và Agent luôn biết pipeline đang ở đâu, không phải scroll lại lịch sử chat.
> **Phiên bản:** 1.0 — Phase 2 v3.0
> **Khi nào dùng:** BẮT BUỘC tạo khi `/tac_chien [chủ đề]` khởi động project mới.

---

## 1. Cấu trúc 3 file state per project

Mỗi project folder (`outputs/YYYY-MM-DD_Ten_Chu_De/`) PHẢI có 3 file:

| File | Vai trò | Ai cập nhật |
|---|---|---|
| `_task_plan.md` | Kế hoạch sản xuất video — các bước, deadline, assignee | Agent 00 (Coordinator) tạo lúc đầu; cập nhật khi Sếp đổi yêu cầu |
| `_findings.md` | Tổng hợp phát hiện trong quá trình: thông tin trinh sát, quyết định Angle, ghi chú từ Sếp, link nguồn | Agent 01 (Researcher) chính; mọi Agent có thể append |
| `_progress.md` | Trạng thái realtime: bước nào DONE, bước nào WAITING, bước nào IN-PROGRESS | Agent 00 cập nhật sau mỗi bước hoàn tất |

---

## 2. Template `_task_plan.md`

```markdown
# Task Plan — [Tên video]
> **Project ID:** YYYY-MM-DD_Ten_Chu_De
> **Khởi tạo:** YYYY-MM-DD HH:MM
> **Deadline mục tiêu:** YYYY-MM-DD
> **Persona:** Người Giải Mã V5.1

## Mục tiêu video
- Thông điệp chính: ...
- Đối tượng cụ thể: ...
- Tiêu chí thành công (KPI): View ≥ X / CTR ≥ Y% / Retention ≥ Z%

## Pipeline 8 bước
- [ ] Bước 0 — Trinh sát (Agent 01) — ETA: ...
- [ ] Bước 1 — Brief (Agent 01)
- [ ] Bước 2 — 5 Angle → 🔴 Gate 1 Sếp duyệt
- [ ] Bước 3 — Dàn ý → 🔴 Gate 2 Sếp duyệt
- [ ] Bước 4 — Viết kịch bản (Agent 02)
- [ ] Bước 5 — QC 33 tiêu chí (Agent 03)
- [ ] Bước 6a — Export DOCX (Agent 04)
- [ ] Bước 6b — 20 tiêu đề SEO
- [ ] Bước 6c — Thumbnail YouTube
- [ ] Bước 6d — Bài Facebook C.R.A.F.T
- [ ] Bước 6e — Mega Comments seeding
- [ ] Postmortem (sau publish 24h)

## Ràng buộc đặc biệt
- ...

## Đối thủ đã làm chủ đề này
- ... (tra `Đối_thủ/bao_cao_tinh_bao.md`)
```

## 3. Template `_findings.md`

```markdown
# Findings — [Tên video]

## Nguồn dữ liệu chính
- [ ] Báo VN: ...
- [ ] Báo quốc tế: ...
- [ ] YouTube đối thủ: ...
- [ ] X/Reddit/Threads: ...

## Số liệu / Sự kiện đã verify
| Số liệu | Nguồn | Ngày | Trang/Time |
|---|---|---|---|
| ... | ... | ... | ... |

## Quyết định Angle (Bước 2)
- 5 Angle đề xuất: ...
- Sếp chọn: Angle #X — lý do: ...

## Quyết định Dàn ý (Bước 3)
- Cấu trúc: Tam giác ngược
- Sếp duyệt: ✅ / ❌ — ghi chú: ...

## Ghi chú từ Sếp (trong quá trình)
- ...

## Vấn đề phát sinh
- ...
```

## 4. Template `_progress.md`

```markdown
# Progress — [Tên video]
> **Cập nhật lần cuối:** YYYY-MM-DD HH:MM by Agent XX

## Trạng thái hiện tại
🟢 **DONE:** Bước 0, 1, 2, 3
🟡 **IN PROGRESS:** Bước 4 — Đang viết tiểu mục 3.2 (đã 1100/1800 từ)
⏸️ **WAITING:** -
❌ **BLOCKED:** -

## Nhật ký bước
| Bước | Start | End | Agent | Output | Note |
|---|---|---|---|---|---|
| 0 | 09:15 | 09:42 | 01 | Top 5 chủ đề | Chọn chủ đề #2 |
| 1 | 09:42 | 09:55 | 01 | brief.md | OK |
| 2 | 09:55 | 10:08 | 01 | 5 angle | Sếp chọn Angle #4 |
| 3 | 10:08 | 10:35 | 02 | outline.md | Tam giác ngược, Sếp OK |
| 4 | 10:35 | ... | 02 | (đang viết) | - |

## Cross-validation
- Số vòng Agent 02 ↔ Agent 03 (kịch bản): 0
- Số vòng Agent 04 ↔ Agent 03 (tiêu đề): 0

## Cảnh báo
- (nếu có)
```

---

## 5. Quy tắc cập nhật

1. **`_task_plan.md`** — TĨNH (ít sửa). Chỉ sửa khi Sếp đổi yêu cầu, đổi deadline, hoặc thêm ràng buộc mới.
2. **`_findings.md`** — TĂNG DẦN (chỉ append, hiếm khi xóa). Mọi quyết định và số liệu verify được ghi vào đây làm chân lý.
3. **`_progress.md`** — ĐỘNG (cập nhật sau mỗi bước). Agent 00 BẮT BUỘC cập nhật khi:
   - Một bước chuyển sang DONE
   - Một bước bị BLOCKED (kèm lý do)
   - Có Cross-validation round mới
4. **Trước khi Agent ra quyết định lớn** — BẮT BUỘC re-read `_task_plan.md` để refresh mục tiêu, tránh "drift".
5. **Khi Sếp gọi `/tien_do`** — Agent 00 đọc `_progress.md` của TẤT CẢ project đang mở → tổng hợp báo cáo.

---

## 6. Trigger semantic cho `planning-with-files`

```
"Dùng planning-with-files: tạo 3 file state (_task_plan, _findings, _progress) 
cho project [project_id] trong outputs/[project_id]/ theo template workflow pipeline_state.md"
```

Sau đó mỗi khi update state:
```
"Cập nhật _progress.md cho [project_id]: Bước X đã DONE, output [file], 
chuyển sang Bước Y giao Agent ZZ"
```
