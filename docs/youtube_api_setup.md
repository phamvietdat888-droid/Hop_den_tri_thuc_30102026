# HƯỚNG DẪN BẢO MẬT: Lấy Client Secrets của YouTube API (OAuth 2.0)

> ⚠️ **NGUYÊN TẮC BẢO MẬT — KHÔNG NGOẠI LỆ:**
> File `client_secrets.json` **TUYỆT ĐỐI KHÔNG được nằm trong thư mục dự án**.
> Lý do: nếu dự án bị index, commit lên Git, hay upload đâu đó, OAuth secret coi như rò rỉ → bất kỳ ai có file đều có thể giả mạo ứng dụng của Sếp để xin quyền truy cập YouTube của người khác.
>
> **Vị trí lưu chuẩn:** `C:\Users\BIC-MT\.credentials\nktc\client_secrets.json`
> Script `scripts/youtube_analytics.py` đã được cấu hình đọc từ đường dẫn này (qua biến `CREDENTIALS_DIR`). Có thể override bằng biến môi trường `NKTC_CREDENTIALS_DIR` nếu muốn đổi chỗ.

---

Sếp chỉ cần làm 3 bước này MỘT LẦN DUY NHẤT (mất khoảng 3 phút).

### BƯỚC 1: Bật API trên Google Cloud
1. Truy cập: [Google Cloud Console](https://console.cloud.google.com/)
2. Chọn **Select a project** → **New Project** → đặt tên `GiaiMa360-Analytics` → **Create**.
3. Đi tới **APIs & Services** → **Library**.
4. Tìm và **Enable** hai API:
   - `YouTube Data API v3`
   - `YouTube Analytics API`

### BƯỚC 2: Thiết lập OAuth Consent Screen
1. Menu trái, chọn **OAuth consent screen**.
2. Chọn **External** → **Create**.
3. Điền các ô bắt buộc:
   - Tên ứng dụng: `NKTC Analytics`
   - User support email: (email của Sếp)
   - Developer contact info: (email của Sếp)
4. **Save and Continue**. Scopes và Test users bấm Next bỏ qua.

### BƯỚC 3: Tạo Chìa khóa (client_secrets.json)
1. Menu trái → **Credentials**.
2. **+ CREATE CREDENTIALS** → **OAuth client ID**.
3. *Application type*: chọn **Desktop app**. Tên: `NKTC Bot`.
4. **Create** → bấm **DOWNLOAD JSON**.
5. **QUAN TRỌNG:** Đổi tên file vừa tải về thành `client_secrets.json` và lưu vào:
   ```
   C:\Users\BIC-MT\.credentials\nktc\client_secrets.json
   ```
   (Tạo thư mục `.credentials\nktc\` nếu chưa có. KHÔNG bao giờ đặt file này vào trong thư mục `T:\Antigravity\GiaiMa360\` hay bất kỳ thư mục project nào.)

---

### Khi credential bị nghi rò rỉ — Quy trình xoay vòng

Nếu file `client_secrets.json` từng bị index, commit, hay chia sẻ nhầm:

1. Vào [Credentials trong Cloud Console](https://console.cloud.google.com/apis/credentials).
2. Chọn project `GiaiMa360-Analytics`.
3. Tìm OAuth client cũ → **Delete** (hoặc bấm icon thùng rác).
4. Tạo OAuth client mới theo Bước 3 ở trên.
5. Tải `client_secrets.json` mới về thay file cũ tại `C:\Users\BIC-MT\.credentials\nktc\`.
6. Xóa file `token.pickle` cũ trong cùng thư mục (nếu có) — buộc script đăng nhập lại.

---

### Cấu hình nâng cao (tuỳ chọn)

Nếu Sếp muốn lưu credential ở chỗ khác, set biến môi trường trước khi chạy script:

```powershell
$env:NKTC_CREDENTIALS_DIR = "D:\Secrets\nktc"
python scripts\youtube_analytics.py --video <video_id>
```

---

Xong! Lần đầu chạy lệnh lấy số liệu, hệ thống mở 1 tab trình duyệt để Sếp bấm "Cho phép". Từ đó về sau, mọi thứ tự động.
