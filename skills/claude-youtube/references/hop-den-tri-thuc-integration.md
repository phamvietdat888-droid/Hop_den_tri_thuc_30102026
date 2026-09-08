# Hộp Đen Tri Thức — Integration Contract

This reference is loaded whenever the Claude YouTube skill runs inside the merged
`Hop_Den_Tri_Thuc` project. It adapts the imported English-first creator skill to
the Vietnamese editorial system without duplicating the source sub-skills.

## Authority

The project root is authoritative. Follow `GEMINI.md`, `AGENTS.md`, `CLAUDE.md`,
`checklist.md`, and `.shared/compliance_shield.md` before applying any source
reference. If a source instruction conflicts with a root rule, keep the root rule.

## Editorial defaults

- Brand: Hộp Đen Tri Thức / Giải Mã 360.
- Audience and language: Vietnamese viewers; write in Vietnamese with the local persona.
- Evidence: do not invent facts, benchmarks, quotes, dates, or keyword metrics.
- Production: new scripts enter the two-Gate pipeline; do not bypass Angle and Outline approval.
- Delivery: user-facing production files are `.docx`; Markdown is an internal draft except image prompts.
- Compliance: scan public-facing copy with the local Compliance Shield and 33-point checklist.

## Command routing

Use `docs/claude_youtube_integration.md` for the complete `/youtube` command map.
In short, the imported sub-skills provide growth analysis and references; the local
Agents 00–05 own research, writing, quality control, publishing, and final output.

## Market and data overrides

- Treat the local Vietnamese market as the default, not the source's US/English example.
- Set language, search location, and examples explicitly when a live data tool is available.
- Treat source benchmarks as dated reference material. Verify dynamic platform rules and prices before presenting them as current.
- If a credential or live-data tool is unavailable, state the limitation and use user-supplied or public data.

## Output mapping

- Production: `outputs/YYYY-MM-DD_Ten_Chu_De/YouTube/`, `Facebook/`, and `YouTube_Shorts/`.
- Standalone growth reports: `outputs/Content_Mang_Xa_Hoi/YouTube_Growth/`.
- Channel/video/competitor investigations: `outputs/kham_kenh/`.

Do not create a second output tree just because a source sub-skill has a generic
Markdown template. Adapt the template to the local output contract.
