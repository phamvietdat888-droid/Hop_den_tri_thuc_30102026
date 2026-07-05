# 🐛 ERRORS.md — Sổ Ghi Lỗi Phổ Biến & Cách Khắc Phục

---

## E01: Giọng AI — Liệt kê "Thứ nhất, Thứ hai"
**Triệu chứng:** Kịch bản dùng "Thứ nhất... Thứ hai... Thứ ba..."
**Nguyên nhân:** AI mặc định liệt kê theo thứ tự.
**Cách sửa:** Kể chuyện tuần tự, mỗi ý là một lớp bóc tách. Dùng câu hỏi tu từ để chuyển ý.

## E02: Hook yếu — Chào hỏi
**Triệu chứng:** Mở đầu bằng "Xin chào các bạn" hoặc giới thiệu kênh.
**Nguyên nhân:** Pattern mặc định của AI.
**Cách sửa:** Xóa toàn bộ. Đập thẳng bằng 1 trong 6 công thức Hook.

## E03: Câu quá dài
**Triệu chứng:** Câu > 20 từ, đọc thành tiếng bị hụt hơi.
**Nguyên nhân:** AI viết văn viết thay vì văn nói.
**Cách sửa:** Tách thành 2-3 câu ngắn. Thêm tiểu từ tình thái.

## E04: Thiếu tiểu từ tình thái
**Triệu chứng:** Văn bản đọc "sạch" quá, không có hơi thở.
**Nguyên nhân:** AI không tự thêm "nhá", "cơ", "đấy"...
**Cách sửa:** Rà soát mỗi 3-4 câu, thêm 1 tiểu từ. Xem bảng Module 3.

## E05: Ví von sáo rỗng
**Triệu chứng:** Ví von kiểu "giống như cạnh tranh thương mại tạo áp lực".
**Nguyên nhân:** AI dùng ví von trừu tượng.
**Cách sửa:** Phải có nhân vật + hành động + kết quả CỤ THỂ. Xem Module 6.

## E06: Quên nỗi đau người xem
**Triệu chứng:** Kịch bản phân tích hay nhưng người xem không thấy liên quan đến mình.
**Nguyên nhân:** Chỉ nói vĩ mô, quên kết nối vi mô.
**Cách sửa:** Sau mỗi ý vĩ mô → thêm 1-2 câu kéo về giá xăng, giá gạo, túi tiền.

## E07: Liên hệ lịch sử gượng ép
**Triệu chứng:** Liên hệ lịch sử VN nhưng không liên quan đến chủ đề.
**Nguyên nhân:** Ép liên hệ vì checklist yêu cầu.
**Cách sửa:** Nếu không tự nhiên → BỎ QUA. Ghi chú "không phù hợp" trong checklist.

## E08: Lặp cấu trúc câu
**Triệu chứng:** 3 câu liên tiếp bắt đầu cùng kiểu "Chủ ngữ + Vị ngữ".
**Nguyên nhân:** Pattern AI.
**Cách sửa:** Đảo ngữ, dùng câu hỏi, câu cụt, thán từ mở đầu.

## E09: Dùng từ cấm
**Triệu chứng:** Xuất hiện "Ngoài ra", "Tuy nhiên", "Điều đáng chú ý là"...
**Nguyên nhân:** AI dùng từ nối học thuật.
**Cách sửa:** Xem `.shared/tu_cam.md` — thay bằng cách nói dân dã.

## E10: Kết bài đóng
**Triệu chứng:** Kết bài chốt ý rõ ràng, không để người xem suy ngẫm.
**Nguyên nhân:** AI có xu hướng kết luận tròn trịa.
**Cách sửa:** Thay bằng câu hỏi mở gây tranh cãi. Xem Module 1 — Bước 4, mục 6.

## E11: Clickbait Rỗng — Tiêu đề/Hook cường điệu vô căn cứ ⚠️ VETO
**Triệu chứng:** Dùng các từ "Cú lừa thế kỷ", "SỐC", "Kinh hoàng", "Sụp đổ", "Cả thế giới chấn động" mà nội dung video/bài viết không tương xứng.
**Nguyên nhân:** AI bắt chước pattern giật tít của báo mạng. Hoặc người viết muốn tăng CTR bằng mọi giá.
**Hậu quả:**
- YouTube: Bị flag "Misleading Metadata", shadowban (bóp đề xuất ngầm), demonetize, giảm độ uy tín kênh dài hạn.
- Facebook: Bị giảm reach do thuật toán Meta phát hiện engagement bait.
- Thương hiệu: Khán giả trí thức (target chính của Giải Mã 360) mất niềm tin, thấy kênh giống "báo lá cải".
**Cách sửa:** Xem danh sách Blacklist F1 trong `.shared/tu_cam.md` mục F. Thay bằng từ ngữ tạo tò mò CHÂN THỰC: "Sự thật đằng sau...", "Ít ai để ý...", "Nước cờ bất ngờ...", "Bí mật ít người biết".
**Quy tắc vàng:** Tiêu đề hứa gì → nội dung PHẢI trả được lời hứa đó. Cường điệu ≤ 20%.
**Phạm vi:** Áp dụng cho YouTube (tiêu đề + hook) VÀ Facebook (caption + tiêu đề bài).

## E12: Lỗi Font / Mất dấu tiếng Việt (Mojibake) khi đăng fanpage
**Triệu chứng:** Đoạn chữ tiếng Việt đăng lên Facebook biến thành ký tự lạ (như "Ã", "Ð", "á", "").
**Nguyên nhân:** Quá trình giao tiếp giữa PowerShell (`Get-Content`, `Invoke-RestMethod`) và `curl.exe` với Graph API bị lệch chuẩn Encoding. Hoặc lưu file text bằng lệnh `WriteAllText` của .NET sinh ra BOM (Byte Order Mark) khiến `curl` đọc sai.
**Cách sửa:** 
1. Khi dùng PowerShell đọc file: Luôn dùng `Get-Content -Path <file> -Raw -Encoding UTF8`.
2. Hạn chế dùng `WriteAllText` với `UTF8`. Nên dùng: `$bytes = [System.Text.Encoding]::UTF8.GetBytes($text); [System.IO.File]::WriteAllBytes($file, $bytes)` để đảm bảo UTF-8 without BOM.
3. Khi dùng `curl` đọc file đính kèm `message=<file`, PHẢI luôn khai báo mime type: `-F "message=<$messageFile;type=text/plain;charset=utf-8"`.
4. Nếu push text trực tiếp, hãy tận dụng `[System.Net.WebUtility]::UrlEncode($text)` truyền vào body. 

## E13: Lộ Metadata / Văn bản thừa trên bài Facebook
**Triệu chứng:** Bài đăng lên Facebook xuất hiện các thẻ "# 06d. BÀI VIẾT FACEBOOK", "> **Tình trạng:**", hoặc các blockquote hệ thống ở ngay đầu bài.
**Nguyên nhân:** Khi tạo file `06d_fb_post.md`, Agent gài thêm tiêu đề hệ thống và metadata. Nhưng lệnh Post FB API lại đọc TOÀN BỘ file nhét lên Facebook. Graph API không biết gọt metadata.
**Cách sửa:** Khi tạo bài viết nháp ở `.md` để dùng cho Lệnh đăng tự động, bảng kết quả **PHẢI trần trụi**. Tuyệt đối KHÔNG ĐƯỢC thêm `# Tiêu đề file` hay blockquote hệ thống. File bắt đầu bằng chữ gì thì lên Fanpage hiển thị chữ đó.

## E14: Vi phạm Tiêu chuẩn Cộng đồng (Từ ngữ nhạy cảm/Tục) ⚠️ VETO
**Triệu chứng:** Sử dụng các từ ngữ nhạy cảm (như "thối mồm", "chết đói", "chó đẻ"...) hoặc vi phạm tiêu chuẩn cộng đồng của nền tảng (bạo lực, nhục mạ, thù ghét).
**Nguyên nhân:** AI hoặc Agent nhập vai quá trớn (đặc biệt khi Seeding bằng các persona "Người đặt câu hỏi móc", "Doanh nhân thực tế") nhằm đẩy cao trào tranh luận.
**Hậu quả:** Bài viết hoặc Comment bị Facebook/YouTube cắm cờ (flag), ẩn, xóa, bóp tương tác. Kênh bị cảnh cáo hoặc "bay màu" nếu vi phạm nhiều lần.
**Cách sửa:** 
- Tuyệt đối tuân thủ Mục A của `tu_cam.md` (TỪ TỤC — TUYỆT ĐỐI CẤM).
- Khi tạo nội dung seeding hoặc bài đăng, phải quét nội dung xem có chứa ngôn từ dễ gây hiểu lầm là nhục mạ, đả kích cá nhân, hoặc thô tục không.
- Thay bằng các từ ngữ thể hiện sự khó khăn nhưng vẫn văn minh (VD: "lao đao", "chật vật", "điêu đứng" thay vì "đói thối mồm").

## E15: Vòng Xoáy Tử Thần Thuật Toán (Thuật toán bỏ rơi)
**Triệu chứng:** Kênh có hàng chục ngàn sub nhưng video mới đăng lẹt đẹt vài chục view. Nguồn view từ "Đề xuất" và "Trang chủ" gần như bằng 0 (dưới 5%). Kênh chỉ sống ngoi ngóp nhờ Tìm kiếm thụ động.
**Nguyên nhân:** Thường là hậu quả của chuỗi domino: Dính gậy bản quyền (tụt Trust) → Nghỉ đăng video quá lâu (thuật toán đóng băng) → Tiêu đề vi phạm Blacklist (bị đánh dấu Misleading Metadata).
**Hậu quả:** YouTube ngừng chủ động phân phối video. Video không hiện lên bảng feed của chính những người đã đăng ký.
**Cách sửa:** 
1. **Dọn rác:** KHÔNG xóa video (tránh báo lỗi gãy link nội bộ). Chỉ chuyển các video kém (<50 view) hoặc vi phạm sang trạng thái Riêng tư (Private).
2. **Tẩy trắng Metadata:** Đổi toàn bộ tiêu đề (và thumbnail nếu chứa chữ) loại bỏ các từ Blacklist F1 (Kinh hoàng, Chấn động, Cú lừa, Tận khốc...).
3. **Bơm máu:** Đăng đều đặn 1 video/2 ngày liên tục trong 14 ngày (chuỗi 7 video), tuân thủ tuyệt đối Metadata sạch để ép thuật toán "đo lại huyết áp" cho kênh.
