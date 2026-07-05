# 🧠 CHIẾN LƯỢC TỔNG THỂ & HỆ THỐNG CỐT LÕI (Cập nhật 2026-04-29)

> **Lưu ý cho AI ở các phiên làm việc sau:** 
> Đây là bản đồ chiến lược cao nhất của hệ thống "Giải Mã 360". BẮT BUỘC phải tuân thủ các nguyên tắc và luồng công việc tại đây trước khi thực hiện bất kỳ lệnh nào của User (Sếp).

---

## 1. TÌNH TRẠNG KÊNH & MỤC TIÊU HIỆN TẠI
- **Tình trạng:** Kênh đang trong trạng thái "Ngủ đông / Hôn mê" (do ngừng đăng video 3 tháng). Kênh KHÔNG bị shadowban hay bóp đề xuất.
- **Mục tiêu ưu tiên:** Kích hoạt lại thuật toán phân phối (Browse Features & Suggested) bằng việc đăng tải nội dung đều đặn.
- **Tần suất bắt buộc:** 2 Video/tuần.

## 2. CHIẾN LƯỢC NỘI DUNG (MÔ HÌNH HUB & SPOKE)
- **Công thức:** `1 Video Dài (~10 phút) = 2 đến 3 Video Shorts (≤ 50s)`.
- **Vai trò:**
  - *Shorts:* Là "máy kích tim" kéo traffic mới, thu hút New Viewers, tạo tò mò và gắn link trỏ về video dài. Không bao giờ lấy y nguyên video dài cắt ra, mà phải viết lại Hook và kịch bản riêng cho Shorts.
  - *Video Dài:* Là nền tảng giữ chân khán giả trung thành, mang lại Watch Time và Doanh thu cốt lõi.

## 3. CẤU TRÚC HỆ SINH THÁI KỸ NĂNG (SKILLS)
Hệ thống vận hành bằng 9 Skills chính (lưu tại `skills/`):
1.  **`giai_ma_360_skill.md`**: Pipeline tổng (đã tích hợp tự động tạo Shorts tại Bước 6f).
2.  **`kham_kenh_skill.md`**: Bác sĩ chẩn đoán kênh (7 module). Thay thế hoàn toàn các skill phân tích cũ.
3.  **`youtube_short_skill.md`**: Chuyển thể tự động Kịch bản Dài -> Shorts + SEO + 10 Prompt ảnh.
4.  **`viet_tieu_de_skill.md`**: Tạo gói SEO (13 Formula Tiêu đề + Từ khóa).
5.  **`dang_fanpage_skill.md`**: Tạo và lên lịch bài Facebook.
6.  **`do_hoa_fanpage_skill.md`**: Thiết kế ảnh bằng Prompt (Geopolitical Art).
7.  **`seeding_facebook_skill.md`**: Tạo Mega Comments.
8.  **`trinh_sat_trend_skill.md`**: Quét tin tức thị trường.
9.  **`md_to_docx_v2.py`**: Chuyển đổi `.md` sang `.docx` chuẩn màu sắc cho Sếp đọc.

## 4. QUY TRÌNH TỰ ĐỘNG HÓA SẢN XUẤT 
- Chỉ có **2 Gate Check** (Báo cáo để Sếp duyệt): (1) Chốt Angle và (2) Chốt Dàn ý.
- Sau khi chốt dàn ý, toàn bộ quá trình từ Viết nháp -> Kiểm định -> Kịch bản Clean -> Gói SEO -> Bài Facebook -> YouTube Shorts -> Convert DOCX đều là **TỰ ĐỘNG HOÀN TOÀN**.

## 5. CƠ CHẾ DỰ PHÒNG TẠO ẢNH (PLAN B)
- Mặc định sử dụng lệnh `generate_image` để vẽ ảnh bìa và minh họa (Lưu vào thư mục `images/` của từng Short).
- **Fallback (Lỗi 503):** Nếu hệ thống nội bộ quá tải, AI tự động kích hoạt `browser_subagent` để truy cập `https://labs.google/fx/vi/tools/flow/project`.
- **Hành động Subagent:** Đăng nhập (tài khoản mặc định), tạo Project, duyệt vòng lặp nhập Prompt, thiết lập **2 ảnh/prompt**, tải về và lưu đúng thư mục.

---
*Bản ghi nhớ này giúp đảm bảo sự nhất quán chiến lược, tránh tình trạng AI ở phiên làm việc sau đi chệch hướng hoặc yêu cầu tạo lại các tính năng đã được thiết lập.*
