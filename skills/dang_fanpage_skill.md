# Skill: Đăng Fanpage — Bước 6d "Phát Sóng Fanpage"
> **Agent:** 04_Publisher | **Trigger:** Tự động sau Bước 6c HOẶC `/dang_fb [chủ đề]`
> **Phiên bản:** 1.0 | **Cập nhật:** 2026-04-21

---

## 📌 THÔNG TIN KẾT NỐI

### Fanpage: Giải Mã 360
- **Page ID**: `341500382389972`
- **Danh mục**: Thể thao & giải trí / Chuyên gia tin tức
- **Mô tả**: Kênh phân tích, bình luận chính trị - xã hội với phong cách sáng tạo, hài hước, sâu sắc và "cà khịa" tinh tế
- **Followers**: 177
- **Page Access Token**: `EAF0ozkHdc7MBRFm3ElZCd6VbT1YMhnVDiqVsSZB2RVXzdYKjrajQRleRD3epkuHGQZAy574EZCksnx7m2Vpyhaz9QiK1A2obOQKWcGCCu3ufwY6HYQAIqpuMHTVqVHEJzPLqheKXZCEAZCdPBuZAzfmGEvKenYYFnHKY26dEyO0OEcS2w5Rw6d1FVNg4e0AbDdX2n0GO2qk`
- **Quyền**: ADVERTISE, ANALYZE, CREATE_CONTENT, MESSAGING, MODERATE, MANAGE

### API
- **Base URL**: `https://graph.facebook.com/v19.0`

---

## ⚔️ CHẾ ĐỘ A: CHUYỂN THỂ TỪ KỊCH BẢN YOUTUBE (Bước 6d tự động)

### Khi nào kích hoạt
- **Tự động** sau khi hoàn thành Bước 6c (Cập nhật Kho Vũ Khí)
- HOẶC Sếp gọi lệnh `/dang_fb` khi đã có kịch bản hoàn chỉnh trong `outputs/`

### Quy trình 5 bước

#### Bước 6d.1: GỌT KỊCH BẢN

**Input:** `outputs/[YYYY-MM-DD]_[Topic]/YouTube/06_kich_ban_hoan_thien.md`

**Tham chiếu bắt buộc:**
- `.shared/format_facebook.md` — Quy chuẩn format FB
- `.shared/tone_guide.md` — Giọng điệu
- `.shared/tu_cam.md` — Từ cấm

**Quy trình gọt:**
1. Đọc `06_kich_ban_hoan_thien.md` (format Audio Clean — chỉ Lời bình, bỏ thẻ màu)
2. Giữ lại:
   - Hook (gọt xuống 50-80 từ)
   - 2-3 insight SẮC nhất (ưu tiên Lớp Bề Chìm + Vĩ Mô)
   - 1 ví von hay nhất
   - 1-2 đoạn nhập vai đối thoại (nếu cực tốt)
   - Liên hệ lịch sử VN (nếu cực hay — không ép)
3. Bỏ:
   - Pacing Marker, tag kỹ thuật
   - Cột Visual
   - CTA Like/Sub YouTube
   - Phần Cầu Nối dài, Dẫn Dắt - Bối Cảnh dài
4. Chuyển đổi:
   - Xưng hô: "các bác" / "bà con" → **"anh em"**
   - Câu > 20 từ → tách thành 2-3 câu ngắn
   - Kết bài mở → CTA Facebook + hashtag
5. Giãn dòng: Mỗi đoạn ≤ 4 dòng, 1 dòng trống giữa các đoạn

**⚠️ TRỌNG TÂM LỖI E13:** Bản nháp xuất ra `06d_fb_post.md` **PHẢI trần trụi**. Tuyệt đối KHÔNG gài thêm `# 06d. BÀI VIẾT FACEBOOK` hay bất kỳ Blockquote metadata nào ở đầu file. API sẽ post toàn bộ những gì có trong file này!

**Output:** Bản nháp bài Facebook SẠCH (không lẫn markdown tags), 500-800 từ

#### Bước 6d.2: LẤY TIÊU ĐỀ

**Input:** `outputs/[YYYY-MM-DD]_[Topic]/YouTube/06b_goi_seo.md`

**Quy trình:**
1. Lấy tiêu đề mà Sếp đã chọn (Top 1 trong bộ SEO)
2. Viết HOA toàn bộ tiêu đề → làm dòng đầu bài Facebook
3. Nếu tiêu đề YT quá dài (> 55 ký tự) → gọt cho phù hợp feed FB

#### Bước 6d.3: TẠO ẢNH THUMBNAIL

**Quy tắc:**
- Kích thước: 1200x630px (tối ưu Facebook feed)
- Phong cách: Biểu tượng / Minh họa nghệ thuật / Geopolitical Art
- TUYỆT ĐỐI KHÔNG chèn text vào ảnh
- Tone: Kịch tính, tương phản cao, bắt mắt mobile

**Prompt template cho generate_image:**
```
[Chủ đề minh họa] in dramatic geopolitical illustration style,
dark moody lighting, cinematic composition,
symbolic elements representing [yếu tố chính trị chính],
no text, no watermarks, no human faces,
landscape format 1200x630
```

**Số lượng:** Tạo **1 ảnh** (khác với skill cũ tạo 3 ảnh — tiết kiệm)

#### Bước 6d.4: COMPLIANCE GATE & PREVIEW

**🛡️ YÊU CẦU BẮT BUỘC (COMPLIANCE GATE):**
Trước khi hiển thị Preview, Agent 04 **PHẢI** tự động quét toàn bộ nội dung bài viết qua bộ lọc `.shared/compliance_shield.md`.
- Nếu phát hiện vi phạm Blacklist T1/T2 → **HỦY ĐĂNG NGAY LẬP TỨC**, báo lỗi E14 cho Sếp.
- Nếu an toàn (PASS) → Tiến hành hiển thị Preview.

Hiển thị cho Sếp duyệt:
```
═══════════════════════════════════════════
📱 PREVIEW BÀI FACEBOOK — Giải Mã 360
═══════════════════════════════════════════

📌 TIÊU ĐỀ: [Tiêu đề IN HOA]

📝 NỘI DUNG: [Toàn bộ bài viết]

🖼️ ẢNH: [Hiển thị ảnh thumbnail]

⏰ HẸN GIỜ: 19:00 VN ngày [DD/MM/YYYY]

📊 THỐNG KÊ:
   - Tổng từ: [X] từ
   - Số đoạn: [Y]
   - Hashtag: [Z]
═══════════════════════════════════════════
```

**`[CHỜ SẾP DUYỆT]`** — Sếp có thể:
- ✅ Duyệt → Chuyển sang Bước 6d.5
- ✏️ Yêu cầu sửa → Quay lại Bước 6d.1
- ⏰ Đổi giờ đăng → Cập nhật timestamp
- ❌ Hủy → Không đăng

#### Bước 6d.5: ĐĂNG BÀI LÊN FACEBOOK

**Lưu ý kỹ thuật quan trọng:**
- Sử dụng `cmd.exe /c curl.exe` để tránh lỗi ký tự `<` trong PowerShell
- Lưu message vào file tạm UTF-8 trước khi gửi
- Bọc trong try-catch

##### 5a. Đăng ngay (không ảnh):
```powershell
$pageId = "341500382389972"
$token = "EAF0ozkHdc7MBRFm3ElZCd6VbT1YMhnVDiqVsSZB2RVXzdYKjrajQRleRD3epkuHGQZAy574EZCksnx7m2Vpyhaz9QiK1A2obOQKWcGCCu3ufwY6HYQAIqpuMHTVqVHEJzPLqheKXZCEAZCdPBuZAzfmGEvKenYYFnHKY26dEyO0OEcS2w5Rw6d1FVNg4e0AbDdX2n0GO2qk"
$message = "<NỘI_DUNG_BÀI>"

$encodedMessage = [System.Net.WebUtility]::UrlEncode($message)

$uri = "https://graph.facebook.com/v19.0/$pageId/feed"
$body = "message=$encodedMessage&access_token=$token"

try {
    $response = Invoke-RestMethod -Uri $uri -Method Post -Body $body -ContentType "application/x-www-form-urlencoded"
    Write-Host "✅ Post ID: $($response.id)"
    Write-Host "🔗 Link: https://www.facebook.com/$($response.id)"
} catch {
    $errorStream = $_.Exception.Response.GetResponseStream()
    $reader = New-Object System.IO.StreamReader($errorStream)
    $errorBody = $reader.ReadToEnd() | ConvertFrom-Json
    Write-Host "❌ Lỗi: $($errorBody.error.message)"
    Write-Host "Mã lỗi: $($errorBody.error.code)"
}
```

##### 5b. Đăng kèm ảnh (từ file local):
```powershell
$pageId = "341500382389972"
$token = "EAF0ozkHdc7MBRFm3ElZCd6VbT1YMhnVDiqVsSZB2RVXzdYKjrajQRleRD3epkuHGQZAy574EZCksnx7m2Vpyhaz9QiK1A2obOQKWcGCCu3ufwY6HYQAIqpuMHTVqVHEJzPLqheKXZCEAZCdPBuZAzfmGEvKenYYFnHKY26dEyO0OEcS2w5Rw6d1FVNg4e0AbDdX2n0GO2qk"
$imagePath = "<ĐƯỜNG_DẪN_ẢNH>"
# Luôn đọc file nguồn UTF-8 chuẩn xác
$message = Get-Content -Path "<FILE_MD>" -Raw -Encoding UTF8

# Tránh dùng `WriteAllText` với `UTF8` encoding vì PS 5.1 sẽ thêm BOM, gây lỗi mojibake với curl. 
# CHỈ dùng GetBytes để xuất UTF-8 Without BOM.
$messageFile = "t:\Antigravity\GiaiMa360\drafts\temp_fb_message.txt"
$bytes = [System.Text.Encoding]::UTF8.GetBytes($message)
[System.IO.File]::WriteAllBytes($messageFile, $bytes)

# Upload ảnh kèm bài viết qua cmd.exe (Lưu ý: Bắt buộc khai báo charset=utf-8)
$uri = "https://graph.facebook.com/v19.0/$pageId/photos"
cmd.exe /c "curl.exe --ssl-no-revoke -s -X POST `"$uri`" -F `"access_token=$token`" -F `"message=<$messageFile;type=text/plain;charset=utf-8`" -F `"source=@$imagePath`""
```

##### 5c. Hẹn giờ 19:00 VN (Scheduled Post):
```powershell
$pageId = "341500382389972"
$token = "EAF0ozkHdc7MBRFm3ElZCd6VbT1YMhnVDiqVsSZB2RVXzdYKjrajQRleRD3epkuHGQZAy574EZCksnx7m2Vpyhaz9QiK1A2obOQKWcGCCu3ufwY6HYQAIqpuMHTVqVHEJzPLqheKXZCEAZCdPBuZAzfmGEvKenYYFnHKY26dEyO0OEcS2w5Rw6d1FVNg4e0AbDdX2n0GO2qk"
$message = "<NỘI_DUNG_BÀI>"

# Tính 19:00 VN hôm nay (hoặc ngày mai nếu đã qua)
$now = [DateTimeOffset]::Now
$target = [DateTimeOffset]::new($now.Year, $now.Month, $now.Day, 19, 0, 0, [TimeSpan]::FromHours(7))
if ($target -lt $now) { $target = $target.AddDays(1) }
$unixTimestamp = $target.ToUnixTimeSeconds()

$encodedMessage = [System.Net.WebUtility]::UrlEncode($message)

$uri = "https://graph.facebook.com/v19.0/$pageId/feed"
$body = "message=$encodedMessage&published=false&scheduled_publish_time=$unixTimestamp&access_token=$token"

try {
    $response = Invoke-RestMethod -Uri $uri -Method Post -Body $body -ContentType "application/x-www-form-urlencoded"
    Write-Host "⏰ Scheduled Post ID: $($response.id)"
    Write-Host "📅 Sẽ đăng vào: $($target.ToString('yyyy-MM-dd HH:mm:ss zzz'))"
} catch {
    $errorStream = $_.Exception.Response.GetResponseStream()
    $reader = New-Object System.IO.StreamReader($errorStream)
    $errorBody = $reader.ReadToEnd() | ConvertFrom-Json
    Write-Host "❌ Lỗi: $($errorBody.error.message)"
}
```

##### 5d. Hẹn giờ 19:00 VN kèm ảnh (Scheduled Photo Post):
```powershell
$pageId = "341500382389972"
$token = "EAF0ozkHdc7MBRFm3ElZCd6VbT1YMhnVDiqVsSZB2RVXzdYKjrajQRleRD3epkuHGQZAy574EZCksnx7m2Vpyhaz9QiK1A2obOQKWcGCCu3ufwY6HYQAIqpuMHTVqVHEJzPLqheKXZCEAZCdPBuZAzfmGEvKenYYFnHKY26dEyO0OEcS2w5Rw6d1FVNg4e0AbDdX2n0GO2qk"
$imagePath = "<ĐƯỜNG_DẪN_ẢNH>"
$message = Get-Content -Path "<FILE_MD>" -Raw -Encoding UTF8

# Tính 19:00 VN
$now = [DateTimeOffset]::Now
$target = [DateTimeOffset]::new($now.Year, $now.Month, $now.Day, 19, 0, 0, [TimeSpan]::FromHours(7))
if ($target -lt $now) { $target = $target.AddDays(1) }
$unixTimestamp = $target.ToUnixTimeSeconds()

# Lưu message UTF-8 (No BOM)
$messageFile = "t:\Antigravity\GiaiMa360\drafts\temp_fb_message.txt"
$bytes = [System.Text.Encoding]::UTF8.GetBytes($message)
[System.IO.File]::WriteAllBytes($messageFile, $bytes)

# Upload ảnh hẹn giờ qua cmd.exe (nhớ khai báo charset=utf-8)
$uri = "https://graph.facebook.com/v19.0/$pageId/photos"
cmd.exe /c "curl.exe --ssl-no-revoke -s -X POST `"$uri`" -F `"access_token=$token`" -F `"message=<$messageFile;type=text/plain;charset=utf-8`" -F `"source=@$imagePath`" -F `"published=false`" -F `"scheduled_publish_time=$unixTimestamp`""

Write-Host "⏰ Ảnh sẽ đăng lúc: $($target.ToString('yyyy-MM-dd HH:mm:ss zzz'))"
```

**Output:** Lưu bài đã đăng vào `outputs/[YYYY-MM-DD]_[Topic]/Facebook/06d_bai_dang_fb.md`

> [!CAUTION]
> **QUY TẮC SỐNG CÒN — KHÔNG BAO GIỜ ĐƯỢC VI PHẠM (Bổ sung 2026-04-29):**
> Sau khi nhận được Post ID thành công từ API Facebook, Agent **PHẢI TỰ ĐỘNG** chuyển sang `seeding_facebook_skill.md` để tạo và đăng Mega Comments **NGAY LẬP TỨC** trong cùng một lượt xử lý.
> **TUYỆT ĐỐI KHÔNG ĐƯỢC:**
> - Dừng lại báo cáo "đã đăng thành công" rồi chờ Sếp nhắc
> - Tách Mega Comments thành bước riêng cần Sếp kích hoạt
> - Quên hoặc bỏ qua bước Seeding vì bất kỳ lý do gì
>
> **THỨ TỰ BẮT BUỘC:** Post bài → Nhận Post ID → Tạo JSON Mega Comments → Đăng Mega Comments → Báo cáo Sếp (1 lần duy nhất, đầy đủ tất cả).

---

## 🆕 CHẾ ĐỘ B: VIẾT BÀI FACEBOOK ĐỘC LẬP

### Khi nào kích hoạt
- Sếp gọi lệnh **`/dang_fb [chủ đề]`** khi KHÔNG có kịch bản YouTube

### Quy trình 6 bước

#### B.1: Nhận chủ đề
- Sếp nhập từ khóa hoặc chủ đề
- Mặc định đăng lên **Giải Mã 360**

#### B.2: Chọn template & viết bài
**Tham chiếu bắt buộc:**
- `.shared/format_facebook.md` — Quy chuẩn format (6 template viral)
- `.shared/tone_guide.md` — Giọng điệu
- `.shared/tu_cam.md` — Từ cấm
- `.shared/storytelling_arsenal.md` — Kỹ thuật kể chuyện

**Quy trình:**
1. Chọn 1 trong 6 Template Viral trong `format_facebook.md` (phần Chế độ B)
2. Chọn 1 trong 12 Dạng Tiêu đề Viral
3. Viết bài 500-800 từ theo đúng giọng "Hộp Đen Tri Thức"
4. Giữ đặc trưng: ví von đời thường, mỉa mai tinh tế, câu hỏi tu từ, tiểu từ tình thái
5. 🛡️ **Quét bài qua Compliance Shield** (`.shared/compliance_shield.md`) trước khi trình bày Preview.

#### B.3: Tạo ảnh thumbnail
- Giống Bước 6d.3 (Chế độ A)

#### B.4: Preview & Gate Check
- Giống Bước 6d.4 (Chế độ A)
- **`[CHỜ SẾP DUYỆT]`**

#### B.5: Đăng bài
- Sếp chọn: Đăng ngay hoặc Hẹn giờ 19:00
- Sử dụng lệnh PowerShell tương ứng từ phần Bước 6d.5

#### B.6: Lưu trữ
- Lưu bài vào `outputs/fb_doc_lap/[YYYY-MM-DD] [Topic].md`

---

## 📊 QUẢN LÝ & THỐNG KÊ

### Xem danh sách bài đã đăng
```powershell
$pageId = "341500382389972"
$token = "<TOKEN>"

$uri = "https://graph.facebook.com/v19.0/$pageId/feed?fields=id,message,created_time,shares,permalink_url&limit=10&access_token=$token"
$response = Invoke-RestMethod -Uri $uri -Method Get
$response.data | ForEach-Object {
    Write-Host "---"
    Write-Host "ID: $($_.id)"
    Write-Host "Thời gian: $($_.created_time)"
    Write-Host "Nội dung: $($_.message.Substring(0, [Math]::Min(100, $_.message.Length)))..."
    Write-Host "Link: $($_.permalink_url)"
}
```

### Xem thống kê bài viết
```powershell
$postId = "<POST_ID>"
$token = "<TOKEN>"

$uri = "https://graph.facebook.com/v19.0/$postId?fields=shares,reactions.summary(true),comments.summary(true)&access_token=$token"
$response = Invoke-RestMethod -Uri $uri -Method Get

Write-Host "👍 Reactions: $($response.reactions.summary.total_count)"
Write-Host "💬 Comments: $($response.comments.summary.total_count)"
if ($response.shares) { Write-Host "🔄 Shares: $($response.shares.count)" }
```

### Xóa / Chỉnh sửa bài viết
```powershell
# Xóa
$postId = "<POST_ID>"
$token = "<TOKEN>"
Invoke-RestMethod -Uri "https://graph.facebook.com/v19.0/$postId?access_token=$token" -Method Delete

# Chỉnh sửa
$newMessage = "<NỘI_DUNG_MỚI>"
$encodedMessage = [System.Net.WebUtility]::UrlEncode($newMessage)
Invoke-RestMethod -Uri "https://graph.facebook.com/v19.0/$postId" -Method Post -Body "message=$encodedMessage&access_token=$token" -ContentType "application/x-www-form-urlencoded"
```

---

## ⚠️ XỬ LÝ LỖI PHỔ BIẾN

| Mã lỗi | Ý nghĩa | Cách xử lý |
|---|---|---|
| **190** | Token hết hạn / Không hợp lệ | Thông báo Sếp lấy token mới |
| **100** | Tham số không hợp lệ | Kiểm tra lại Page ID, message format |
| **200** | Không đủ quyền | Kiểm tra quyền Page Access Token |
| **368** | Vi phạm chính sách nội dung | Sửa nội dung, kiểm tra `tu_cam.md` |
| **4** | Rate limit (> 200 calls/giờ) | Chờ 1 giờ rồi thử lại |
| **506** | Bài trùng lặp (duplicate) | Sửa nội dung cho khác |

---

## 📚 THAM CHIẾU BẮT BUỘC

| File | Mục đích |
|---|---|
| `.shared/format_facebook.md` | Quy chuẩn format bài FB |
| `.shared/tone_guide.md` | Giọng điệu "Hộp Đen Tri Thức" |
| `.shared/tu_cam.md` | Danh sách từ cấm |
| `.shared/storytelling_arsenal.md` | Kỹ thuật kể chuyện |
| `checklist.md` (nhóm G) | Checklist Facebook |
