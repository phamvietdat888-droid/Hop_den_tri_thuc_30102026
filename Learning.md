# 📖 Learning.md — Nhật Ký Học Hỏi

> Ghi chép những bài học rút ra từ quá trình sản xuất kịch bản. Cập nhật sau mỗi Postmortem.

---

## 2026-04-20 — Ngày thành lập hệ thống

- Hoàn thành Prompt "Người Giải Mã" V5.1 — tích hợp 17 file phân tích kênh đối thủ TTT
- Xây dựng hệ thống GiaiMa360 với cấu trúc đầy đủ
- Bài học quan trọng:
  - Câu hỏi tu từ phải có 3 CHỨC NĂNG (tò mò + nhấn mạnh + dẫn dắt), không chỉ dùng để chuyển đoạn
  - Thán từ là "hơi thở" của kịch bản — 3-5 lần/bài, rải đều
  - Phải luôn "đánh vào nỗi đau" — kéo người xem vào câu chuyện
  - Liên hệ lịch sử VN phải TỰ NHIÊN — nếu không phù hợp thì BỎ QUA
- **Bài học từ kịch bản "Luật Đất Đai & TP Đồng Nai" (20/4):** Khi không có điểm nóng quốc tế, ta hoàn toàn có thể triển khai xuất sắc phân tích "Địa chính trị nội bộ" (quy hoạch, luật pháp). Bóc tách luật khô cứng thành câu chuyện túi tiền bằng ngôn ngữ đời thường (nồi lẩu, thuốc đắng, "vặt lông gà") sẽ gây đồng cảm mạnh mẽ cho người xem bình dân.

## 2026-07-05 — 4 nguyên tắc "cuốn hút" (Sếp góp ý từ kịch bản Sân Trống Đồng) ⭐ BẮT BUỘC

Sếp chỉ ra 4 điểm yếu cốt lõi. Đã ghi thẳng vào DNA hệ thống để mọi phiên sau tự áp dụng, KHÔNG cần nhắc lại:

1. **Mạch phải LIỀN, không rời rạc** → `tone_guide.md` mục "KẾT NỐI MẠCH VĂN". Dùng liên từ–thán từ làm "chất keo", móc xích giữa các đoạn (câu cuối đoạn gieo tò mò, câu đầu đoạn sau trả lời). Kiểm bằng checklist #19b.
2. **Diệt chữ hàn lâm, ví von phải SÁT** → `tone_guide.md` mục "VĂN NÓI BÌNH DÂN". Bảng thay chữ (chủ thể→người bỏ tiền, cơ chế→cách nó chạy…). Test "mẹ mình có hiểu không". Kiểm bằng checklist #19c.
3. **Khai thác tối đa chi tiết thú vị — QUY ĐỔI mọi con số khủng** → `storytelling_arsenal.md` KỸ THUẬT 7 (Number Anchoring, 5 cách quy đổi). Con số phải làm khán giả bật "so sánh hay quá!". Kiểm bằng checklist #12b.
4. **Nêu vấn đề bất ngờ TRƯỚC, giải thích cặn kẽ SAU** → `tone_guide.md` mục "NÊU VẤN ĐỀ TRƯỚC". Ưu tiên số 1: gài nghịch lý khiến "ơ sao lại thế?" rồi mới bung giải thích tường tận, không nhảy cóc. Kiểm bằng checklist #12c.

## 2026-07-05 (bổ sung) — 5 nâng cấp + Agent 05 Hook Master (v3.3) ⭐ BẮT BUỘC

Sếp góp ý vòng 2 từ kịch bản Sân Trống Đồng. Đã cài vào hệ thống:

5. **Câu chuyển cảnh mặc định sau Hook** = *"Ngay sau đây, chúng ta cùng tìm hiểu các bạn nhé."* → `tone_guide.md`. Bỏ *"Mình cùng bóc từng lớp một nhé."*
6. **Agent 05 Hook Master** — agent chuyên trị Hook, quy trình 5 bước (mổ tư tưởng → định vị điểm chạm nỗi đau/xu hướng/mâu thuẫn → bóc lớp 1-2-3 → viết 3-5 phương án chấm điểm 5 thước đo → mài câu đầu ≤15 từ + open loop). File: `.agent/agents/05_Hook_Master.md`. Chèn vào pipeline Bước 3.5.
7. **Dồn chi tiết đắt lên NỬA ĐẦU** (chống rơi rụng 1/3 đầu) → `storytelling_arsenal.md` KT8. Checklist #12d.
8. **CTA sau CAO TRÀO** — kêu gọi like/share/đăng ký chèn khéo ngay sau chi tiết ấn tượng, gắn vào cảm xúc vừa tạo, không van nài → `tone_guide.md`. Checklist #12f.
9. **Đào tới BẢN CHẤT + liên hệ sự kiện thế giới** (hỏi "vì sao" tới gốc, mỗi tầng kèm ví von; dẫn case nước ngoài đã kiểm chứng khi làm bài sâu hơn) → `storytelling_arsenal.md` KT9. Checklist #12e.
10. **CHỈ GIAO `.docx`** ở mọi công đoạn; `.md` chỉ là nháp nội bộ trong `scratch/` → GEMINI.md §8.1b + CLAUDE.md.

## 2026-04-21 — Tối ưu hóa quy trình sản xuất (Protocol 2.5)

Rút kinh nghiệm từ chiến dịch "Binh pháp đêm 21/04", hệ thống chính thức áp dụng 5 trụ cột tối ưu:
1. **Chiến thuật 5 Angle Độc Bản (Tiền Tác Chiến):** Bắt buộc phải trình Sếp 5 góc nhìn (Kinh tế, Binh pháp, Lịch sử, Âm mưu, Phản biện) trước khi làm dàn ý. Không làm tắt.
2. **Tổ chức Quân Doanh (Workspace):** Mỗi tập video bắt buộc lưu trong một thư mục riêng biệt định dạng `outputs/YYYY-MM-DD_Ten_Chu_De/` và phải chia làm 2 thư mục con: `YouTube` và `Facebook`.
3. **Định dạng thư mục YouTube:** Gồm các file bắt buộc: (1) `06_script_final.md`; (2) `06_script_final.docx` (Tích hợp cả kịch bản và 20 tiêu đề ở cuối); (3) `06b_tieu_de.md`; (4) `thumbnail.jpg` (ảnh minh họa).
4. **Định dạng thư mục Facebook:** Gồm các file bắt buộc: (1) `06d_fb_post.md`; (2) `06d_fb_post.docx` (Tích hợp nội dung bài viết và 20 tiêu đề gợi ý ở cuối như file kịch bản Youtube); (3) `06b_tieu_de.md` (20 tiêu đề cho bài Face); (4) `06e_fb_seeding.md` (file seeding/bình luận); (5) `thumbnail.jpg`.
5. **Cơ chế Dự phòng Đồ họa:** Nếu AI tạo ảnh thất bại/sập server (lỗi 503) hoặc tải ảnh lỗi, KHÔNG tự ý tải ảnh linh tinh. Bắt buộc phải tạo một file text chứa Promt tạo ảnh cực kỳ chi tiết (ví dụ: `06c_image_prompt.md`) đặt vào thư mục và báo cáo lại ngay cho Sếp để Sếp tự tạo.

## 2026-04-22 — Bài học từ kịch bản "Trump & 5 Tháng Lịch Sử"

Sếp đã rút kinh nghiệm trực tiếp trong quá trình sản xuất. Toàn bộ bài học dưới đây **BẮT BUỘC** áp dụng cho mọi phiên sau:

### A. Hành văn — Mượt mà, Hài hước mà Sâu sắc
> **Triết lý của Sếp:** Kịch bản phải mượt mà, hài hước mà sâu sắc, thú vị, lôi cuốn. AI phải không ngừng học hỏi để hoàn thiện văn phong theo hướng này.

1. **Trị bệnh lạm dụng tiểu từ "nhá":**
   - KHÔNG gắn "nhá" vào mọi câu. Tối đa **2-3 lần/kịch bản**, phải đặt đúng ngữ cảnh (nhấn mạnh, dặn dò).
   - Ở câu CTA (kêu gọi hành động) → dùng **"nhé"** thay "nhá" (nhẹ nhàng, lịch sự hơn).
   - Ở câu hỏi tu từ, câu chuyển ý → **BỎ HẲN** tiểu từ nếu không cần thiết.
   - ❌ *"Công bằng mà nói nhá,"* → ✅ *"Công bằng mà nói,"*
   - ❌ *"Thử nghĩ xem nhá:"* → ✅ *"Thử nghĩ xem:"*
   - ❌ *"Rồi bây giờ nhá,"* → ✅ *"Rồi bây giờ,"*

2. **Chống lạm dụng dấu gạch ngang (—) để nối ý:**
   - Dấu gạch ngang chỉ dùng khi tạo **ngắt nhịp kịch tính** hoặc **chèn thông tin phụ**.
   - KHÔNG dùng thay từ nối. Hãy dùng **từ nối tự nhiên** (chỉ, mà, rồi, thì).
   - ❌ *"giao cho tôi — 5 tháng là xong"* → ✅ *"giao cho tôi chỉ 5 tháng là xong"*

3. **Xóa cụm từ lệch tone, không ăn khớp:**
   - Khi viết châm biếm, câu cảm thán phải **khớp giọng** với ngữ cảnh. Nếu đoạn trước đang phân tích nghiêm túc → câu châm biếm phải tinh tế, KHÔNG suồng sã.
   - ❌ *"Nghe oai lắm. Đến chịu luôn."* → ✅ *"Nghe oai lắm."* (bỏ câu thừa, để giọng sắc hơn)

4. **Linh hoạt dùng liệt kê khi cần MẠCH LẠC:**
   - Quy tắc "CẤM liệt kê" trong `tu_cam.md` KHÔNG phải tuyệt đối. Khi đoạn văn cần trình bày **nhiều ý rõ ràng** (3 vấn đề, 3 lý do...) → PHẢI dùng cấu trúc liệt kê tự nhiên.
   - ❌ *"Ông Trump đang gặp 3 vấn đề. Tỷ lệ ủng hộ giảm. Phe bảo thủ chia rẽ. Và ông ấy cần chiến tích."*
   - ✅ *"Ông Trump đang gặp 3 vấn đề cùng lúc. Vấn đề đầu tiên đó là tỷ lệ ủng hộ giảm. Vấn đề thứ 2, phe bảo thủ chia rẽ. Và vấn đề thứ 3 là ông ấy cần chiến tích."*

5. **Câu chuyển ý phải có LỰC và SANG:**
   - Câu mời gọi người xem phải đẳng cấp, thể hiện vị thế "người am hiểu mời khách", không phải ra lệnh.
   - ❌ *"Pha ấm trà đi, rồi mình nói chuyện kỹ."*
   - ✅ *"Nào, pha ấm trà thôi, rồi mời các bác cùng bàn luận."*

### B. Quy trình Xuất Bản — Format chuyên nghiệp
6. **File Word (.docx) BẮT BUỘC sinh tự động:** Markdown cho AI, Word cho con người. Không cần Sếp nhắc.
7. **Quy chuẩn format Word (dành cho Đạo diễn/Biên tập viên):**
   - Font: **Times New Roman**, cỡ **14**
   - Khổ giấy: **A4**, lề đều **2cm** (trên, dưới, trái, phải)
   - Căn đều 2 bên (**Justify**), giãn dòng **1.25**
8. **Mã hóa giọng điệu bằng màu sắc trong file Word:**
   - 🔴 **Đỏ (CC0000):** Nhấn mạnh cực độ, bức xúc, sự thật sốc
   - 🟢 **Xanh lá (008000):** Dữ liệu, con số, năm tháng khách quan
   - 🔵 **Xanh dương (0066CC):** Mỉa mai, châm biếm, trào phúng
   - 🟠 **Cam (E65000):** Câu hỏi, tò mò, gợi mở
   - **In đậm:** Punch words — nhấn âm
   - *In nghiêng:* Đọc chậm, rải nhịp, tạo khoảng lặng
   - <u>Gạch chân:</u> Chốt hạ, ngắt nhịp dứt khoát

---

## 2026-05-23 — Tối ưu token v3.1

Sau audit toàn diện dự án v3.0 (38 skills), thực hiện 7 quick win KHÔNG đụng 8 Module/Anti-AI/33 tiêu chí:

**Hành động thực thi:**
1. **Move `agent-evaluation`** (943 lines, ~10.5k token) → `.agent/skills/community/_lazy/` + thêm pattern vào `.antigravityignore` để không index ngầm. Invoke explicit qua `/kiem_dinh` deep mode.
2. **Slim `.shared/to_mo_loi_ich_module.md` §5 Mental Models** (72→40 lines, -44%) — gom chi tiết 5 model về skill `marketing-psychology` duy nhất, file `.shared/` chỉ giữ tên + quy tắc dùng.
3. **Compact GEMINI.md §6 CẤU TRÚC** (138→30 lines) — convert text list thành tree compact, tách full paths sang `docs/structure_reference.md` (lazy companion).
4. **Compact GEMINI.md §10 Community Skills** (~135→60 lines) — gom Phase 3 Tier B thành 1 dòng, tách ví dụ prompt + flow chi tiết sang `docs/gemini_companion.md` (lazy companion).
5. **Tạo `.agent/metrics/skill_usage.md`** — template log skill trigger frequency mỗi video, quy trình 3-video review để move skill noise sang `_lazy/`.
6. **Bump GEMINI.md v3.0 → v3.1** + cập nhật Agent 03 reference path `_lazy/` cho `agent-evaluation`.

**Kết quả đo được:**
- GEMINI.md: 515 → 279 lines (-46% size, -13.4KB) → mỗi session tiết kiệm ~5-8k token always-loaded
- to_mo_loi_ich_module.md: 72 → 40 lines (-44%)
- Tổng token tiết kiệm/session: ~25k (15-20% context window)
- 0 thay đổi pipeline production. 8 Module + Anti-AI 3 tầng + 33 tiêu chí + Persona "Người Giải Mã" GIỮ NGUYÊN.

**Bài học:**
- **Lazy companion pattern**: file chi tiết tách ra `docs/*.md`, GEMINI.md chỉ giữ ref. Antigravity semantic match vẫn tìm thấy khi cần, nhưng không tốn token always-load.
- **`.antigravityignore` + `_lazy/`**: skill nặng (>500 lines) NÊN move sang `_lazy/` + ignore pattern thay vì xóa — giữ nguyên capability, chỉ giảm cost index.
- **3-video review rule**: skill không trigger sau 3 video → downgrade tier hoặc move lazy. `.agent/metrics/skill_usage.md` track tự động.
- **Centralize duplication**: mental models (Loss Aversion, ...) đã trùng 200 lines giữa `to_mo_loi_ich_module.md` ↔ `marketing-psychology` → gom về 1 source, file kia chỉ giữ tên + ref.
9. **Chú giải bảng màu:** Đặt ngay ĐẦU FILE Word, ngay sau tiêu đề, trước nội dung kịch bản.
10. **Chèn tiêu đề A/B Test lên đầu kịch bản:** Đưa thẳng 2 phương án tiêu đề chính lên chóp file kịch bản để Đạo diễn duyệt ngay, không cần mở file SEO riêng.

### C. Kỷ luật Xuất bản (Fanpage & Đồ họa)
11. **TUYỆT ĐỐI KHÔNG QUÊN MEGA COMMENTS:** Khi phát sóng bài Facebook (Bước 6d), bắt buộc phải sinh luôn file `06e_mega_comments.json` chứa các bình luận mồi (seeding) và 2 CTA. Đừng đợi Sếp nhắc "thế file comment đâu em?".
12. **Ảnh Thumbnail YouTube PHẢI LÀ 16:9:** Kích thước cho ảnh thumbnail kênh YouTube mặc định là tỷ lệ 16:9 (1280x720). Đừng nhầm lẫn với tỷ lệ 1.91:1 (1200x630) của ảnh bài đăng Facebook. Phải tự động tạo và lưu vào đúng thư mục `YouTube/thumbnail.png`.

---

*(Bổ sung sau mỗi video)*

## 2026-04-30 — Chẩn đoán Kênh & Vòng Xoáy Thuật Toán

- **Không bao giờ xóa (Delete) video:** Chỉ sử dụng tính năng **Riêng tư (Private)** cho những video kém chất lượng (< 50 view) hoặc vi phạm chính sách. Xóa video sẽ làm gãy link nội bộ và khiến YouTube đánh giá kênh bị "mất dữ liệu", tụt Trust Score nghiêm trọng.
- **Tẩy trắng Metadata:** YouTube AI dùng OCR quét chữ trên cả Thumbnail và quét Tiêu đề. Việc dùng từ Blacklist (Kinh hoàng, Sốc, Chấn động, Cú lừa) sẽ khiến video bị gắn cờ "Misleading Metadata" (Gây nhầm lẫn/Giật gân). Hậu quả là khóa van đề xuất. Nếu video cũ vi phạm mà view vẫn cao → phải sửa Tiêu đề (và thay Thumbnail nếu trên ảnh có chứa từ cấm).
- **Vòng xoáy tử thần thuật toán (Algorithmic Death Spiral):** Khi kênh dính gậy bản quyền → hạ Trust Score. Nếu sau đó chủ kênh hoảng sợ và **nghỉ đăng liên tục 90 ngày**, thuật toán sẽ coi như "kênh bỏ cuộc", đóng băng phễu phân phối. Subscribers sẽ trở thành "sub ma". Khi đăng lại, CTR từ trang chủ sẽ tụt thảm hại (chỉ còn 1-2%).
- **Cách cứu kênh (Bơm máu):** Kênh chưa chết hẳn nếu **CTR từ Đề xuất vẫn tốt (ví dụ >10%)** khi được hiển thị. Cần một chiến dịch "Bơm máu": Đăng liên tục 7 video (1 video/2 ngày) với Tiêu đề SẠCH HOÀN TOÀN để ép AI đánh giá lại.

## 2026-05-24 — Khắc phục lỗi DOCX Sandbox, Chuẩn Hóa Tỷ Lệ Ảnh & Đăng Bài Seeding Facebook Tự Động

Rút kinh nghiệm sâu sắc từ đợt tác chiến chủ đề "Nhà Cho Thuê", hệ thống chính thức cập nhật và đồng bộ 3 quy tắc cốt lõi sau để chạy tự động hoàn hảo trong các phiên làm việc tiếp theo:

### A. Quy trình Xuất Bản DOCX tự thân (v3.2)
- **Bài học:** Không phụ thuộc vào ứng dụng Word COM bên ngoài (tránh lỗi bảo mật DCOM Access Denied của Sandbox Windows) và tránh việc cài đặt PyPI bị chặn mạng.
- **Giải pháp:** Sử dụng công cụ tự thân `scripts/convert_markdown_to_docx_v3.py`. Công cụ này copy cấu hình lề và style từ template mẫu chuẩn của Sếp (`outputs/2026-04-22_Trump_5_Thang_Lich_Su/YouTube/06_kich_ban_hoan_thien.docx`), sau đó giải nén, dịch mã kịch bản Markdown sang OpenXML chuẩn, ghi đè vào `word/document.xml` rồi nén ZIP lại.
- **Đầu ra:** 100% chuẩn chỉ .docx, căn lề Justify, font Times New Roman 14pt, giãn dòng 1.15, tô màu highlight đệ quy chuẩn chỉnh. Sếp tuyệt đối không còn nhận file lỗi hay trống chữ.

### B. Quy chuẩn Tỷ lệ Ảnh Đa Nền tảng (YouTube 16:9 & Facebook 6:16)
- **Ảnh Thumbnail YouTube (Ngang 16:9):** Bắt buộc phải hiển thị dạng ngang 16:9. Do trình tạo ảnh AI mặc định ra khung vuông (1:1), ta thiết lập Prompt đóng khung đen trên-dưới (Letterbox) để ép phần nội dung hoạt họa chính hiển thị hoàn hảo ở dải ngang 16:9 ở giữa. Sếp có thể dùng ngay hoặc crop nhẹ viền đen.
- **Ảnh Thumbnail Facebook (Dọc 6:16):** Bắt buộc phải là ảnh dọc 6:16 tối ưu cho hiển thị mobile feed. Ta thiết lập Prompt đóng khung đen hai bên (Pillarbox) để nội dung chính nằm gọn trong dải dọc 6:16 ở giữa.

### C. Quy trình Tự Động Đăng Bài & Seeding Fanpage Giải Mã 360
- **Đăng bài kèm ảnh dọc (`scripts/post_to_fb.ps1`):** Tự động đọc file Markdown bài viết, bỏ qua 5 dòng metadata đầu, dọn dẹp ký tự `**` Markdown, xuất mã UTF-8 không BOM để bảo toàn tiếng Việt và đăng kèm ảnh dọc `thumbnail_fb.png` (nếu Sếp đã tải ảnh về) hoặc tự động chuyển sang đăng Text-only nếu chưa có ảnh.
- **Seeding 5 Mega Comments (`scripts/post_seeding.ps1`):** Cập nhật sửa lỗi cũ (trước đây gửi cả Object JSON gây lỗi API, nay đã sửa để lấy đúng trường văn bản `.content`). Tập lệnh chạy seeding tự động 5 bình luận đại diện cho 5 nhóm khán giả cách nhau mỗi 3 giây dựa trên Post ID Sếp nhập vào để đảm bảo độ mượt và tránh bộ lọc Spam của Facebook.

## 2026-07-02 — Đại tu Đồng bộ v3.2 + Đóng gói Claude Projects

Audit toàn hệ phát hiện 7 nhóm bất nhất tích tụ qua các đời phiên bản. Đã vá triệt để, KHÔNG đụng 8 Module / Anti-AI / persona:

1. **Hợp nhất kiểm định về 1 nguồn:** `checklist.md` (33 tiêu chí, 8 nhóm A-H, 5 VETO: #16/#23/#27/#29/#30) là nguồn chấm điểm DUY NHẤT. Xóa bảng 22 tiêu chí cũ trong `giai_ma_360_skill.md`; sửa mọi chỗ ghi "22/23 tiêu chí" (README, workflows, Agent 03).
2. **Chuẩn hóa tên file output (khớp outputs/ thực tế):** `06_kich_ban_hoan_thien.md|.docx` · `06b_goi_seo.md|.docx` · `thumbnail.png` (YT 16:9) · `06d_bai_dang_fb.md|.docx` · `06e_mega_comments.json` · `thumbnail_fb.png` (FB dọc 6:16). Các tên cũ (`06_script_final`, `06b_tieu_de`, `06d_facebook_post`, `06d_fb_post`, `06e_fb_seeding`) hết hiệu lực.
3. **Chính thức hóa Bước 6f (Shorts):** Đưa `/tao_short` + `youtube_short_skill` vào GEMINI.md §4/§7/§8, Agent 04, `san_xuat_kich_ban.md`. Đánh số Bước 6 thống nhất: 6a Clean+DOCX · 6b SEO · 6c Thumbnail · 6d Facebook · 6e Seeding · 6f Shorts · cuối cùng Kho Vũ Khí.
4. **Vá tham chiếu ma:** `phan_tich_studio_skill` → `kham_kenh_skill` (chế độ /kham_video); `outputs/nguoi_giai_ma_v1.md` → `prompts/`; `Obsidian/Chien_Luoc_Phat_Trien.md` → root; `skills/md_to_docx_v2.py` → `scripts/`; xóa ref `ke_hoach_nang_cap_skill_v3.0.md`.
5. **Đồng bộ bảng lệnh GEMINI §7:** bổ sung `/tao_short`, `/mo_ta`, `/tu_khoa`, `/seeding`, `/kham_kenh|/kham_video|/kham_nhanh`, `/studio`, `/rip_transcript`, `/bao_cao_tuan|thang`.
6. **Chốt spec ảnh 2 nền tảng:** YT ngang 16:9 Letterbox · FB dọc 6:16 Pillarbox (`format_facebook.md` đã sửa, hết xung đột với spec 1200×630 cũ — spec đó chỉ còn cho link preview).
7. **Khử trùng lặp workflow:** `tac_chien.md` chuyển thành ALIAS trỏ về `san_xuat_kich_ban.md` — hết cảnh 2 pipeline song song lệch nhau.

**Đóng gói Claude Projects:** Toàn bộ hệ được chưng cất thành bộ `NKTC_Claude_Project/` (CLAUDE.md + 10 file kiến thức hợp nhất, tiếng Việt 100%, đã rút tinh chất 27 community skills vào quy tắc) — dùng cho mục Project của Claude chat, nơi không có file system/script/semantic-match skill.

