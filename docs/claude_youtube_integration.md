# Lớp tăng trưởng YouTube trong Hộp Đen Tri Thức

> Tài liệu hợp nhất hai dự án: pipeline sản xuất nội dung **Giải Mã 360 / Hộp Đen Tri Thức** và gói **Claude YouTube**.
>
> Quy tắc quan trọng nhất: Hộp Đen Tri Thức là hệ điều hành nội dung và là nguồn ưu tiên cao nhất. Claude YouTube là lớp tăng trưởng, dữ liệu và tối ưu phân phối; không được tự tạo một pipeline cạnh tranh.

## 1. Kiến trúc sau hợp nhất

Sau khi hợp nhất, thư mục `T:\CLAUDE\Hop_Den_Tri_Thuc` là dự án duy nhất:

| Lớp | Thành phần | Trách nhiệm |
|---|---|---|
| Hệ điều hành nội dung | `GEMINI.md`, `AGENTS.md`, `CLAUDE.md` | Persona, tiếng Việt, tính xác thực, 2 Gate, quy tắc file và quyền tự động hóa |
| Pipeline biên tập | `.agent/agents/`, `.agent/workflows/` | Trinh sát → brief → angle → dàn ý → hook → viết → kiểm định → xuất bản |
| DNA thương hiệu | `.shared/`, `prompts/`, `checklist.md` | Giọng Hộp Đen, 8 Module, Compliance Shield, 33 tiêu chí |
| Lớp tăng trưởng YouTube | `skills/claude-youtube/` | SEO, retention, thumbnail, Shorts, analytics, chiến lược, lịch nội dung, đối thủ và doanh thu |
| Skill nội bộ kênh | `skills/*.md` | Các tác vụ đã chuyên biệt hóa cho Giải Mã 360, Facebook và pipeline hiện tại |
| Sản phẩm | `outputs/` | Chỉ có sản phẩm hoàn thiện; bài video vẫn theo 3 nhánh `YouTube/`, `Facebook/`, `YouTube_Shorts/` |

Không copy đè các thư mục `outputs/`, `drafts/`, `scratch/` hoặc các file hiến pháp hiện có. Gói Claude YouTube được đặt riêng trong `skills/claude-youtube/` để giữ nguyên toàn bộ 14 phân hệ, tài liệu tham chiếu, template và script API.

## 2. Thứ tự ưu tiên khi có mâu thuẫn

Khi hai dự án diễn đạt khác nhau, áp dụng thứ tự sau:

1. `GEMINI.md` và `AGENTS.md` của dự án đích.
2. `CLAUDE.md`, `checklist.md`, `.shared/compliance_shield.md` và các file DNA trong `.shared/`.
3. Tài liệu này — chỉ dùng để định tuyến lệnh và nối output.
4. `skills/claude-youtube/SKILL.md` và các sub-skill đã nhập.
5. Các reference/template của Claude YouTube.

Các quy tắc cứng của dự án đích luôn thắng:

- Viết cho khán giả Việt bằng giọng `Hộp Đen Tri Thức`; không mặc định trả lời bằng tiếng Anh.
- Không bịa số liệu, trích dẫn, sự kiện hoặc benchmark. Thiếu nguồn thì ghi `[CẦN XÁC MINH]`.
- Kịch bản mới đi qua đúng hai Gate: chọn Angle và duyệt Dàn ý. Không bỏ Gate để chạy thẳng bản hoàn thiện.
- Mọi nội dung công khai phải qua Compliance Shield và checklist 33 tiêu chí.
- File giao Sếp là `.docx`; Markdown chỉ là bản nháp kỹ thuật trong `drafts/` hoặc `scratch/`. Prompt ảnh là ngoại lệ được giao dạng `.md`.
- Bài sản video hoàn chỉnh giữ cấu trúc 3 nhánh trong `docs/structure_reference.md`.

## 3. Bản đồ 14 lệnh `/youtube`

| Lệnh | Cách chạy trong dự án hợp nhất | Đầu ra chuẩn |
|---|---|---|
| `/youtube audit` | Đọc `sub-skills/audit.md`, dùng thêm `skills/kham_kenh_skill.md`, dữ liệu kênh và template đúng loại kênh. | Báo cáo `.docx` trong `outputs/kham_kenh/`; nếu phát hiện video cần sản xuất thì chuyển sang `/tac_chien`. |
| `/youtube analyze` | Kết hợp `sub-skills/analyze.md`, `skills/kham_kenh_skill.md`, `scripts/youtube_analytics.py` và `references/analytics-guide.md`. | Báo cáo khám nghiệm `.docx` trong `outputs/kham_kenh/`. |
| `/youtube competitor` | Kết hợp `sub-skills/competitor.md`, `Đối_thủ/`, `skills/kham_kenh_skill.md` và hồ sơ 5 đối thủ của kênh. | Báo cáo `.docx`; cập nhật hồ sơ trong `Đối_thủ/` chỉ khi có nguồn xác minh. |
| `/youtube ideate` | Dùng `sub-skills/ideate.md` để xếp hạng ý tưởng; với chủ đề thời sự, nối thêm `/tim_trend` và 7 nguồn của Agent 01. | Bản đề xuất `.docx` trong `outputs/Content_Mang_Xa_Hoi/YouTube_Growth/`; ý tưởng được chọn chuyển sang `/tac_chien`. |
| `/youtube strategy` | Dùng `sub-skills/strategy.md`, `Chien_Luoc_Phat_Trien.md`, `Muc_tieu_2026.md` và template Education/Commentary phù hợp. | Kế hoạch `.docx` trong `outputs/Content_Mang_Xa_Hoi/YouTube_Growth/`. |
| `/youtube calendar` | Dùng `sub-skills/calendar.md` và strategy đã duyệt; kiểm tra mùa vụ, sức sản xuất và kho chủ đề. | Lịch `.docx` trong `outputs/Content_Mang_Xa_Hoi/YouTube_Growth/`. |
| `/youtube monetize` | Dùng `sub-skills/monetize.md` và `references/monetization-guide.md`; mọi con số phải ghi nguồn/ngày. | Kế hoạch `.docx` trong `outputs/Content_Mang_Xa_Hoi/YouTube_Growth/`. |
| `/youtube script` | Nếu là chủ đề mới: chuyển thành `/tac_chien` để giữ 2 Gate. Nếu đã có Angle và Dàn ý được duyệt: Agent 02 dùng `sub-skills/script.md` và `references/retention-scripting-guide.md` làm lớp tối ưu. | Kịch bản hoàn chỉnh theo `outputs/YYYY-MM-DD_Ten_Chu_De/YouTube/`. |
| `/youtube hook` | Agent 05 chạy quy trình 5 bước trong `.agent/agents/05_Hook_Master.md`, tham chiếu `sub-skills/hook.md` và `hook_formulas.md`. | Hook nằm trong draft/kịch bản; không giao riêng ngoài format `.docx` nếu Sếp không yêu cầu. |
| `/youtube seo` | Agent 04 dùng `sub-skills/seo.md`, `references/seo-playbook.md` và `skills/viet_tieu_de_skill.md`; quy mô gói SEO theo chuẩn kênh là 20 tiêu đề. | `YouTube/06b_goi_seo.docx`. |
| `/youtube metadata` | Dùng `sub-skills/metadata.md` để hoàn thiện title, description, tags, chapters, hashtags; áp dụng compliance và giọng kênh trước khi xuất. | Gộp vào `YouTube/06b_goi_seo.docx` hoặc file `.docx` metadata riêng khi Sếp yêu cầu. |
| `/youtube thumbnail` | Đọc `sub-skills/thumbnail.md`, `references/thumbnail-ctr-guide.md`, `references/script-thumbnail-alignment.md`; Agent 04 kiểm tra lời hứa thumbnail có khớp kịch bản. | `YouTube/thumbnail_prompt.md` và `YouTube/thumbnail.png` nếu có công cụ tạo ảnh. |
| `/youtube shorts` | Dùng `skills/youtube_short_skill.md` làm chuẩn sản xuất, `sub-skills/shorts.md` và `references/shorts-playbook.md` làm lớp retention/SEO. | 2–3 thư mục `YouTube_Shorts/short_XX/`, mỗi thư mục có `.docx` theo structure reference. |
| `/youtube repurpose` | Dùng `sub-skills/repurpose.md` để lập bản đồ phái sinh; ưu tiên `/dang_fb` và `/tao_short`, thêm nền tảng khác chỉ khi Sếp yêu cầu. | Facebook/Shorts theo output chuẩn; sản phẩm nền tảng khác vào `outputs/Content_Mang_Xa_Hoi/`. |

Nếu một yêu cầu chứa nhiều lệnh, chạy theo thứ tự: `ideate/strategy` → `tac_chien` → `seo/metadata` → `thumbnail` → `repurpose/shorts` → `analyze/postmortem`. Không tự động đăng Facebook hoặc gọi API công khai khi chưa có Gate/duyệt tương ứng.

## 4. Mặc định ngữ cảnh của kênh

Khi Sếp không nói khác, lớp tăng trưởng dùng các giả định đã có trong `GEMINI.md`:

- Thương hiệu: **Hộp Đen Tri Thức**; fanpage: **Giải Mã 360**.
- Thị trường: khán giả Việt; ngôn ngữ nội dung: tiếng Việt.
- Định vị: kiến thức giải trí đa chủ đề, ưu tiên giải thích dễ hiểu, có bằng chứng và có liên hệ đời thường.
- Mục tiêu sản xuất: giữ chân và hiểu đúng trước; tăng trưởng/SEO là lớp hỗ trợ.
- Loại kênh: Education kết hợp Commentary/Niche Authority tùy chủ đề; không tự bịa số người đăng ký để tính benchmark.
- Nếu cần benchmark theo quy mô kênh mà chưa biết tier, hỏi Sếp một câu hoặc ghi rõ `[CẦN SẾP XÁC NHẬN]`.

Source Claude YouTube có các ví dụ quốc tế và mặc định tiếng Anh/Mỹ. Khi dùng trong dự án này, phải đổi sang thị trường Việt, kiểm tra lại từ khóa bằng dữ liệu hiện có, và giữ lại các phần có nguồn. Không đưa benchmark cũ vào kịch bản như một sự thật hiện tại nếu chưa kiểm tra ngày.

## 5. Quy trình dữ liệu và xác minh

### 5.1. Nghiên cứu chủ đề

- Chủ đề thời sự/trend: Agent 01 vẫn là đầu mối; ưu tiên 7 nguồn và template `template_bao_cao_trinh_sat_trend.md`.
- Từ khóa/SEO: dùng reference Claude YouTube để lập giả thuyết; nếu không có dữ liệu live thì ghi rõ là giả thuyết, không bịa volume/CPC/competition.
- Đối thủ: ghi URL, tiêu đề, ngày, số liệu và thời điểm chụp; không suy đoán động cơ hoặc gán phát ngôn.
- Tin nhạy cảm, chính trị-xã hội, tiền bạc và sức khỏe phải có nguồn trực tiếp và qua Compliance Shield.

### 5.2. Script API và credentials

Các script nhập từ `skills/claude-youtube/execution/` là tùy chọn:

- Kiểm tra `YOUTUBE_API_KEY` hoặc OAuth trước khi chạy.
- Không ghi key/token/client secret vào Git, `outputs/`, `drafts/` hoặc chat.
- Thiếu credential thì yêu cầu dữ liệu thủ công hoặc dùng nguồn công khai; không báo cáo “0 dữ liệu” như thể API đã chạy.
- Dùng Python thật đã được kiểm tra; không gọi alias Microsoft Store `WindowsApps`.
- Script chỉ lấy dữ liệu/hỗ trợ phân tích; quyết định biên tập vẫn thuộc Agent 00–04.

## 6. Chuẩn output sau hợp nhất

### 6.1. Video mới

Giữ nguyên cấu trúc bắt buộc:

```text
outputs/YYYY-MM-DD_Ten_Chu_De/
├── YouTube/
│   ├── 06_kich_ban_hoan_thien.docx
│   ├── 06b_goi_seo.docx
│   ├── thumbnail_prompt.md
│   └── thumbnail.png (nếu có)
├── Facebook/
│   ├── 06d_bai_dang_fb.docx
│   └── 06e_mega_comments.json
└── YouTube_Shorts/
    ├── short_01/kich_ban_short.docx
    ├── short_02/kich_ban_short.docx
    └── short_03/kich_ban_short.docx
```

Markdown tương ứng chỉ là bản nháp kỹ thuật. Prompt ảnh được phép ở dạng `.md` theo quy định dự án đích.

### 6.2. Báo cáo tăng trưởng độc lập

Các báo cáo audit, analytics, strategy, calendar, monetization và ideation không phải video hoàn chỉnh, nên lưu theo mẫu:

```text
outputs/Content_Mang_Xa_Hoi/YouTube_Growth/YYYY-MM-DD_Ten_Bao_Cao/
└── bao_cao.docx
```

Nếu báo cáo là khám kênh/khám video/đối thủ, dùng `outputs/kham_kenh/` theo quy ước hiện có. Không để bản Markdown giao Sếp trong các thư mục này.

## 7. Hai Gate và vòng đời nội dung

1. **Gate 1 — Chọn Angle:** mọi kịch bản mới phải có brief, rủi ro, nguồn và 5 Angle; dừng tại `[CHỜ SẾP CHỌN ANGLE]`.
2. **Gate 2 — Duyệt Dàn ý:** sau khi Agent 02 lập dàn ý, dừng tại `[CHỜ SẾP DUYỆT DÀN Ý]`.
3. Sau Gate 2, Agent 05 → Agent 02 → Agent 03 → Agent 04 chạy liên tục theo workflow chuẩn.
4. Claude YouTube chỉ bổ sung retention, SEO, thumbnail, phân tích và phái sinh; không được tạo một bản kịch bản thứ hai ngoài pipeline.
5. Sau khi publish, `/youtube analyze` hoặc `/studio` lấy số liệu; `/rut_kinh_nghiem` cập nhật `Learning.md`, Kho Vũ Khí và lỗi cần tránh.

## 8. Quy tắc nội dung riêng cho lớp tăng trưởng

- Title và thumbnail phải chia sẻ thông tin, không lặp nguyên câu và không hứa quá nội dung.
- Retention tactic không được biến thành câu giật gân rỗng; hook vẫn phải có cầu nối nêu vấn đề và được thân bài trả lời.
- SEO dùng từ khóa để giúp người đúng tìm thấy video, không nhồi từ khóa vào lời bình.
- Thumbnail prompt phải bằng tiếng Anh theo chuẩn source khi cần gọi image model, nhưng chữ trên ảnh và toàn bộ copy kênh vẫn giữ tiếng Việt có dấu.
- Mọi lời khuyên monetization phải phân biệt rõ dữ liệu, giả định, rủi ro và việc cần xác minh chính sách hiện hành.
- Không tự động đăng, seeding, thay thumbnail thật hoặc gọi API có tác động bên ngoài nếu chưa có sự duyệt của Sếp.

## 9. Kiểm tra nghiệm thu sau hợp nhất

Một lần hợp nhất được xem là hoàn tất khi:

- `skills/claude-youtube/SKILL.md` và đủ 14 sub-skill mở được từ dự án đích.
- 9 template, các reference, script API và file `script-thumbnail-alignment.md` còn nguyên.
- Lệnh `/youtube ...` được định tuyến theo bảng ở Mục 3.
- `GEMINI.md`, `CLAUDE.md`, `AGENTS.md` và `README.md` đều trỏ tới tài liệu tích hợp này.
- Manifest `.claude-plugin/plugin.json` nhận diện dự án hợp nhất, không còn manifest “youtube” đứng riêng.
- JSON hợp lệ, Python compile được, không có credential trong file nhập.
- Git diff chỉ gồm phần tích hợp; các file output/draft cũ không bị sửa.

Khi các điều kiện trên đạt, Sếp chỉ cần mở một thư mục `T:\CLAUDE\Hop_Den_Tri_Thuc` để dùng cả pipeline sản xuất lẫn bộ công cụ tăng trưởng YouTube.
