# Project execution notes

## Automatic DOCX conversion

- This repository is stored on the user-mounted Google Drive `T:`. The project
  config in `.codex/config.toml` intentionally uses the Windows `unelevated`
  sandbox so the restricted process can still resolve that mapped drive.
- Convert Markdown by running the checked wrapper from the repository root:

  `powershell -NoProfile -ExecutionPolicy Bypass -File scripts\convert_markdown_to_docx.ps1 -ProjectRoot . -InputMd "<input.md>" -OutputDocx "<output.docx>"`

- DOCX conversion is a local, workspace-scoped- Khi trình bày, báo cáo và dẫn link kết quả cho Sếp trong đoạn chat, hãy chỉ dẫn link trực tiếp tới các file `.docx` tương ứng.

## ⚠️ Quy chuẩn Ngôn từ Bình Dân, Dễ Hiểu, Mạch Lạc & Siêu Thu Hút (BẮT BUỘC VĨNH VIỄN)
- **TẤT CẢ kịch bản (YouTube dài, Shorts, Facebook), lời bình, tiêu đề và cấu trúc** BẮT BUỘC sử dụng ngôn từ bình dân, trực diện, gần gũi như trò chuyện đời thường (ngồi quán nước/trò chuyện với bạn bè, người thân).
- **Mở đầu kịch bản / Bài viết**: BẮT BUỘC đi trực tiếp vào bối cảnh/nội dung gốc, tạo cú móc (Hook) siêu thu hút, giật mình và tạo sự bức bách ngay từ câu đầu tiên. TỰ ĐỘNG biên soạn **2 phương án Hook đỉnh nhất** (Phương án 1: Hook nghịch lý gây sốc & Phương án 2: Hook xoáy trực diện cảm xúc) để Sếp chọn hoặc sử dụng.
- **TUYỆT ĐỐI KHÔNG TRÙNG LẶP Ý GIỮA HOOK VÀ THÂN BÀI (BẮT BUỘC VĨNH VIỄN)**:
  + Hook là "cú đấm tò mò / gây sốc / nghịch lý" độc lập. Thân bài BẮT BUỘC lập tức đi vào bóc tách cơ chế, dữ kiện và giá trị mới mà **TUYỆT ĐỐI KHÔNG lặp lại câu chữ, ngữ cảnh hay ý tứ của Hook**.
  + Đặc biệt trong các bài viết ngắn (~200 - 800 từ) và kịch bản, mỗi câu viết ra phải mang thông tin mới, cấm nhại lại lời mở đầu làm loãng dung lượng bài viết.
- **BẮT BUỘC CÓ "CÂU CẦU NỐI NÊU VẤN ĐỀ" SAU HOOK (BẮT BUỘC VĨNH VIỄN)**: Ngay sau Hook, BẮT BUỘC có 1-2 câu nêu rõ vấn đề cốt lõi mà bài viết sắp giải đáp + tạo đà dẫn dắt tự nhiên sang thân bài. CẤM dùng câu dẫn rỗng kiểu *"Ngay sau đây, chúng ta cùng tìm hiểu các bạn nhé"*. Cấu trúc: `[Hook] → [Câu cầu nối nêu vấn đề] → [Thân bài]`. Chi tiết: `.shared/hook_formulas.md`.
- **TỰ ĐỘNG KÈM GÓI SEO ĐẦY ĐỦ (BẮT BUỘC VĨNH VIỄN)**: Mọi nội dung/bài viết/kịch bản được tạo ra BẮT BUỘC TỰ ĐỘNG đi kèm Gói SEO đầy đủ (gồm **10 tiêu đề ngắn gọn siêu thu hút**, **đoạn mô tả chuẩn SEO ~150-250 từ**, **bộ thẻ Hashtag tối ưu tìm kiếm**, và **20 từ khóa chuẩn SEO**) cùng file `.docx` tương ứng (`06b_goi_seo.docx`) mà KHÔNG để Sếp phải nhắc hay đòi lại ở bất kỳ phiên làm việc nào.
- **TỰ ĐỘNG KÈM LỜI KÊU GỌI HÀNH ĐỘNG (CTA) GẮN CÂU CỐ ĐỊNH (BẮT BUỘC VĨNH VIỄN)**: Phần cuối của mọi bài viết (Facebook, bài phân tích, kịch bản...) BẮT BUỘC phải có câu CTA khơi gợi thảo luận gắn liền với câu cố định: *"Đừng quên bấm Like và đăng ký kênh để thảo luận những vấn đề nóng bỏng khác nữa."* (Ví dụ: "Ý kiến của bạn về vấn đề này thế nào? Hãy để dưới bình luận nhé! Đừng quên bấm Like và đăng ký kênh để thảo luận những vấn đề nóng bỏng khác nữa."). Câu hỏi tương tác phía trước có thể linh hoạt tùy chỉnh cho ăn khớp với nội dung bài viết, nhưng câu *"Đừng quên bấm Like và đăng ký kênh để thảo luận những vấn đề nóng bỏng khác nữa."* là BẮT BUỘC TỰ ĐỘNG ĐƯỢC ĐƯA VÀO TRONG MỌI BÀI VIẾT mà không cần Sếp phải nhắc lại.
- **NGHIÊM CẤM** từ ngữ hàn lâm, từ Hán-Việt khô khan, từ chuyên môn màu mè hay diễn đạt sách vở (như *"hạ tầng bất động sản", "chiều sâu văn hóa", "công cụ quảng bá", "vị trí tôn nghiêm", "cơ chế vĩ mô"*... phải thay bằng *"khối bê tông nhà đất", "rần rần niềm tự hào", "chỗ quảng cáo riêng", "nơi trân trọng nhất", "cách làm"*...).
- **CẤM TIÊU ĐỀ KHẨU HIỆU / CỜ QUẠT**: Tuyệt đối KHÔNG sử dụng các tiêu đề, tên bước hoặc tiểu mục mang tính chất khẩu hiệu, cờ quạt hay giật gân khiên cưỡng (như *"Bước 3: Đấu giá công khai, thu tiền tươi về túi"*...). Tiêu đề các bước bắt buộc đặt tên đơn giản, bình dân, mô tả trực diện như trò chuyện đời thường (như *"Bước 1: Gom đất từ khi còn rẻ"*, *"Bước 2: Chờ làm xong ga, đất tự vọt giá"*, *"Bước 3: Bán đất thu tiền về"*...).
- **Tiêu chí kiểm duyệt tự động**: *"Mẹ/bà nội nghe qua là hiểu liền và thích nghe"*. Áp dụng vĩnh viễn cho tất cả Agent và mọi kịch bản tạo ra mà không cần Sếp nhắc lại.
- DOCX conversion is a local, workspace-scoped operation. Run it automatically
  and report the resulting `.docx`; do not create a batch file and ask the user
  to click it.
- Do not call the Microsoft Store Python alias under
  `Microsoft\WindowsApps`. The wrapper selects and verifies a real Python 3
  interpreter before starting the converter.
- The merged `skills/claude-youtube/` package is a growth/analytics layer. When it
  is used, follow `docs/claude_youtube_integration.md`; the root persona, evidence,
  Compliance Shield, two-Gate pipeline, and DOCX output rules remain authoritative.
- Project config is loaded when a task starts. If an already-open task still
  has the old elevated sandbox and cannot resolve `T:`, request a scoped
  escalation for the conversion command and continue; do not report that
  conversion is impossible.
