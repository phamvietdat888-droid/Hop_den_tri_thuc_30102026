# 📖 GEMINI Companion — Chi tiết §10 Community Skills

> **Lazy-load companion** của GEMINI.md §10. File này chứa: (1) Ví dụ prompt kích hoạt skill, (2) Sơ đồ flow Image Generation, (3) Sơ đồ flow Trinh Sát Đa Nguồn, (4) Chi tiết Phase 3 Tier B skills.
> **Cập nhật cùng phiên bản:** GEMINI.md v3.1

---

## §1 — TIER B (Phase 3) — CHI TIẾT TRIGGER

5 skill Tier B active + 1 skill lazy (agent-evaluation). Trigger explicit khi cần — KHÔNG load mặc định.

| Skill | Vị trí | Trigger Keywords | Tình huống áp dụng |
|---|---|---|---|
| `verification-before-completion` | `community/` | `Gate 3 verify`, `auto-check thumbnail dimensions`, `docx format check` | Sau Bước 6a-c — auto-verify trước khi giao Sếp |
| `hybrid-search-implementation` | `community/` | `vector search`, `keyword search`, `semantic search transcript`, `heat map đối thủ` | Tình báo đối thủ — search transcript 5 kênh (xem `kham_kenh_skill.md` §v1.1) |
| `daily-gift` | `community/` | `template 5-stage`, `editorial synthesis concept visual render`, `template task plan` | Khởi tạo `_task_plan.md` 5-stage chuẩn |
| `sred-project-organizer` | `community/` | `báo cáo tuần`, `báo cáo tháng`, `tổng hợp project`, `weekly monthly report` | Báo cáo tuần/tháng (xem `workflows/weekly_report.md`) |
| `explain-like-socrates` | `community/` | `đối thoại socrates`, `chuỗi câu hỏi dẫn dắt`, `giải thích khái niệm trừu tượng` | KỸ THUẬT 6 storytelling (xem `.shared/storytelling_arsenal.md` KT 6) |
| `agent-evaluation` ⚠️ | `community/_lazy/` | `benchmark 33 tiêu chí`, `evaluate có cơ sở`, `reliability metrics QC` | Bước 5 — invoke explicit qua `/kiem_dinh` deep mode. Skill 943 lines (~10.5k token) — `.antigravityignore` skip để không index ngầm. |

**Cách invoke `agent-evaluation` (đã move `_lazy/`):**
```
"Dùng skill agent-evaluation tại .agent/skills/community/_lazy/agent-evaluation/SKILL.md
 để benchmark kịch bản theo 33 tiêu chí có framework — không cảm tính."
```

---

## §2 — LAYER IMAGE GENERATION (Bước 6c + 6d)

```
INPUT: Brief ảnh từ Agent 04 (mô tả nội dung + tinh thần)
   ↓
image-studio → Phân loại: PHOTO-STYLE (thumbnail có mặt người) vs ARTISTIC (Geopolitical Art)
   ↓
stability-ai → Generate với style phù hợp + inpaint chi tiết
   ↓
OUTPUT: thumbnail.png (16:9 YT) + geopolitical_art.png (FB)
```

**Trigger prompt mẫu (Agent 04 — Bước 6c):**
```
"Stability AI SD3.5 Ultra — generate thumbnail 16:9:
- Subject: [mô tả nhân vật/đối tượng]
- Style: documentary-photographic
- Mood: tension / urgency
- Text overlay: KHÔNG (thumbnail clean, text add sau bằng Canva)"
```

---

## §3 — LAYER TRINH SÁT ĐA NGUỒN (Bước 0)

```
INPUT: Từ khóa / Chủ đề từ Sếp
   ↓
deep-research → Autonomous research planning + multi-source search
   ↓
news-sentiment-engine → Multi-source RSS + sentiment scoring
   ↓
trinh_sat_trend_skill (cũ) → Tổng hợp + chấm 7 tiêu chí
   ↓
OUTPUT: Top 5 chủ đề + sentiment heat map
```

**Trigger prompt mẫu (Agent 01 — Bước 0):**
```
"Deep research chủ đề [tên]: quét đồng thời 7 nguồn,
trả về Top 5 góc tiếp cận với evidence từ ít nhất 3 nguồn/góc"
```

---

## §4 — VÍ DỤ PROMPT KÍCH HOẠT SKILL CỐT LÕI

```markdown
# avoid-ai-writing (BẮT BUỘC sau mỗi đoạn — Agent 02):
"Kiểm tra đoạn văn theo avoid-ai-writing: loại bỏ
- Câu mở đầu kiểu 'Điều này cho thấy...', 'Có thể thấy rằng...'
- Cấu trúc liệt kê máy móc, bullet points thừa
- Từ đệm AI: 'quan trọng', 'đáng chú ý', 'trong bối cảnh đó'
Đối chiếu rewrite table 43-entry."

# parallel-agents (Agent 00 — Bước 4-5):
"Parallel pipeline: Agent 02 viết tiểu mục [3.2.3]
ĐỒNG THỜI Agent 03 chạy 33 tiêu chí trên tiểu mục [3.2.2]"

# sred-work-summary (Agent 04 — Sau publish 24h):
"Generate postmortem retrospective cho video [Tên]:
- Số liệu YT Analytics: [paste]
- Comment sentiment: [paste]
- Compliance Report gốc: [paste]
- Output: postmortem.md theo template trong workflows/postmortem.md"

# marketing-psychology (Agent 02 — Module 7 Nỗi đau):
"Trigger marketing-psychology để chọn 1-2 mental model phù hợp chủ đề [X]:
5 model có sẵn — Loss Aversion / Status Quo Bias / Social Proof / Temporal Framing / Identity Threat.
Output qua persona Người Giải Mã, KHÔNG lộ thuật ngữ tâm lý học."

# keyword-extractor (Agent 04 — Bước 6b Pre-step):
"Extract 50 keywords từ kịch bản [path]: 25 short-tail SEO + 25 long-tail.
Output: kho_keyword.md để viet_tieu_de_skill ăn vào."
```

---

## §5 — CÁCH ANTIGRAVITY MATCH SKILL

Antigravity (Gemini) match skill qua:
1. **Frontmatter `description` field** trong SKILL.md
2. **Tên thư mục** skill
3. **Keywords trong tên file**
4. **Inline content** khi semantic search

**Cách viết prompt để match đúng:**
- ❌ "Hãy viết kịch bản" → mơ hồ, không trigger skill nào
- ✅ "Viết kịch bản theo avoid-ai-writing + beautiful-prose, đảm bảo no AI pattern, hard-edged prose, ngôn từ cụ thể" → trigger đúng 2 skill

**Tip token-saving:**
- Khi đang viết kịch bản dài → KHÔNG gọi explicit cả 28 skill, chỉ gọi 3-5 skill liên quan trực tiếp.
- Mỗi semantic match thừa = thêm ~500-2000 token vào context.

---

**Cập nhật cuối:** 2026-05-23 (v3.1 — token optimization)
