# 📘 Hướng Dẫn Sử Dụng Nhanh NotebookLM Cùng Antigravity

Tài liệu này tổng hợp các "siêu phím tắt" giúp bạn giao tiếp và tự động hóa quy trình làm việc với Google NotebookLM ngay tại cửa sổ chat của Antigravity mà không cần mở trình duyệt.

---

## 1. Hệ Thống Tài Khoản (Profiles)

Công cụ hiện đã được liên kết với 2 tài khoản Google của bạn:
- **Tài khoản 1 (Mặc định):** `degiocuondi494@gmail.com`
- **Tài khoản 2 (Account2):** `phamhoangminhkhang2023@gmail.com`

> **Lưu ý:** Mặc định, mọi lệnh sẽ chạy trên Tài khoản 1. Nếu muốn dùng Tài khoản 2, bạn chỉ cần thêm số `2` vào sau lệnh.

---

## 2. Danh Sách Lệnh Siêu Tốc (Shorthands)

Chỉ cần gõ các từ khóa sau vào khung chat, Antigravity sẽ tự động thực hiện mọi thao tác ngầm.

### 🚀 Tải file và Tạo Notebook
*Dùng khi bạn muốn đẩy tài liệu đang làm việc lên NotebookLM để AI phân tích.*

- `!nlm up` : Lấy **file bạn đang mở** trên màn hình, tự động tạo Notebook mới và tải lên (Tài khoản 1).
- `!nlm up 2` : Thực hiện thao tác tương tự nhưng đẩy lên **Tài khoản 2**.
- `!nlm up [tên_thư_mục]` : Đẩy toàn bộ các file trong một thư mục cụ thể lên làm nguồn.

### 🎧 Tạo Podcast (Audio Overview)
*Biến tài liệu khô khan thành một buổi thảo luận Podcast âm thanh sinh động.*

- `!nlm audio` : Tự động ra lệnh tạo Podcast cho notebook bạn vừa tạo/vừa làm việc.
- `!nlm audio [Tên Notebook]` : Cụ thể tên dự án bạn muốn tạo Podcast.

### 💬 Hỏi Đáp & Phân Tích Dữ Liệu
*Truy vấn thông tin với độ chính xác cao (kèm trích dẫn) từ tài liệu của bạn.*

- `!nlm hỏi: [Câu hỏi]` : Hỏi đáp nhanh với tài liệu. 
  *(Ví dụ: `!nlm hỏi: Tóm tắt cho tôi 3 rủi ro chính trong file này`)*
- `!nlm hỏi 2: [Câu hỏi]` : Hỏi đáp với dữ liệu nằm trên Tài khoản 2.

### 🧹 Quản Lý Dữ Liệu
*Kiểm tra và dọn dẹp các dự án.*

- `!nlm list` : Xem toàn bộ danh sách Notebook trên Tài khoản 1.
- `!nlm list 2` : Xem danh sách Notebook trên Tài khoản 2.
- `!nlm clear` : Xóa nhanh Notebook cuối cùng bạn vừa tạo để dọn dẹp dữ liệu rác.

---

## 3. Ví Dụ Một Chu Trình Làm Việc Mẫu (Workflow)

Giả sử bạn đang viết một file báo cáo `baocao_thang5.md` và muốn nhờ NotebookLM kiểm tra:

1. Đang mở file, bạn gõ vào chat:
   `!nlm up`
2. Đợi Antigravity báo tải xong (mất khoảng vài giây), bạn gõ tiếp:
   `!nlm hỏi: Hãy tìm ra những điểm bất hợp lý trong báo cáo này.`
3. Đọc kết quả phân tích. Sau đó, nếu muốn nghe lại trên đường đi làm, bạn gõ:
   `!nlm audio`
4. Khi đã hoàn tất và không cần dùng notebook đó nữa, bạn gõ:
   `!nlm clear`

**🎉 Mọi thứ diễn ra tự động, trơn tru và hoàn toàn trong Antigravity!**
