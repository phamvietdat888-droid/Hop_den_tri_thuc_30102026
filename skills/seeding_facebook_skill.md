# 💬 KỸ NĂNG: SEEDING BÌNH LUẬN — Mega Comments Giải Mã 360
> **Nguồn gốc:** Hấp thụ từ `binhluan.md` (Kỹ năng Viết Bình Luận Mega Prompt)
> **Chuyển hệ:** AI/Affiliate → Địa Chính Trị | CTA Trung Caha → CTA Giải Mã 360
> **Agent:** 04_Publisher | **Trigger:** Tự động sau Bước 6d (đăng bài FB)
> **Phiên bản:** 1.0 | **Cập nhật:** 2026-04-21

---

## 🎯 MỤC ĐÍCH

Sau khi đăng bài Facebook trên Fanpage Giải Mã 360, hệ thống sẽ **tự động tạo và đăng Mega Comments** — các bình luận bổ sung đào sâu nội dung bài viết. Chiến thuật này:

1. **Kéo reach:** Facebook tính mỗi comment = 1 lượt engagement → đẩy bài lên newsffeed
2. **Giữ chân:** Người đọc lướt bài → xuống comment → thấy nội dung sâu → ở lại lâu hơn
3. **Tạo discussion:** Mega comment mồi → fan thật comment phản hồi → vòng lặp tương tác

---

## 📐 CẤU TRÚC 1 MEGA COMMENT

```
[Emoji] [SỐ]. [TIÊU ĐỀ IN HOA — Ngắn gọn, sắc sảo]

[Phân tích / Bối cảnh / Insight — 3-5 câu]

💡 [Câu kết / Insight chốt — 1 câu mạnh]
```

### Ví dụ mẫu (Bài về Chiến tranh Thương mại Mỹ-Trung):
```
🔍 1. MỸ ĐANG ĐÁNH VÀO ĐÂU?

Nhiều anh em nghĩ đây chỉ là "đánh thuế" đơn thuần. Nhưng thật ra, mũi nhọn chính là CHIPS — công nghệ bán dẫn.

Mỹ không cấm Trung Quốc bán đồ. Mỹ cấm Trung Quốc MUA — mua công nghệ lõi để tự chế tạo. Đây mới là đòn chí mạng.

💡 Ai kiểm soát chip, người đó kiểm soát thế giới.
```

---

## ⚖️ QUY TẮC SỐ LƯỢNG

| Loại bài | Số Mega Comments |
|---|---|
| Bài phân tích sự kiện (Template T1, T4) | 3-5 comments |
| Bài FAQ / Bản đồ tình hình (Template T3, T5) | 5-7 comments (= số phần trong bài) |
| Bài liên hệ lịch sử (Template T2) | 2-3 comments |
| Bài ngắn / tin nhanh | 1-2 comments |

### Quy tắc nội dung Mega Comments

| Giữ | Cấm |
|---|---|
| Giọng "Người Giải Mã" — sắc sảo, ví von | Tục, xúc phạm |
| Xưng hô "anh em" / "các anh em" | "Bạn", "mình", "các bạn" |
| Tiểu từ tình thái: nhá, cơ, ấy, đấy | Giọng AI: "đáng chú ý là", "thực tế cho thấy" |
| Số liệu chính xác + nguồn (nếu có) | BỊA số liệu, sự kiện |
| Câu hỏi tu từ kích comment | Link spam, quảng cáo (trừ 2 CTA chính thức) |

---

## 📌 2 COMMENT CTA BẮT BUỘC — LUÔN THÊM SAU MEGA COMMENTS

> **Quy tắc TUYỆT ĐỐI:** Sau khi đăng hết Mega Comments, LUÔN thêm **2 comment CTA riêng biệt** theo đúng thứ tự. **KHÔNG BAO GIỜ bỏ qua.**

### Comment CTA 1: Kênh YouTube
```
🎬 Xem full video phân tích chi tiết — Giải Mã 360:
👉 https://www.youtube.com/channel/UCPDfSFNU08CLMPD3l4Bp8Og
```

### Comment CTA 2: Group thảo luận
```
💬 Tham gia Group Bàn Luận Thời Sự của Giải Mã 360 — nơi anh em trao đổi, tranh luận, cùng hiểu thế giới:
👉 https://www.facebook.com/share/g/1DmLcHA8Rb/
```

### Thứ tự đăng đầy đủ
```
Comment 1:   Mega Comment #1 (phân tích sâu khía cạnh 1)
Comment 2:   Mega Comment #2 (phân tích sâu khía cạnh 2)
...
Comment N:   Mega Comment #N (comment cuối có hashtag)
Comment N+1: CTA 1 — Kênh YouTube Giải Mã 360      ← BẮT BUỘC
Comment N+2: CTA 2 — Group Bàn Luận Thời Sự              ← BẮT BUỘC
```

> [!IMPORTANT]
> - 2 comment CTA **LUÔN LUÔN** đăng cuối cùng, **KHÔNG BAO GIỜ** bỏ qua
> - Đăng **TÁCH RIÊNG** 2 comment, **KHÔNG** gộp chung
> - Nội dung CTA giữ **NGUYÊN VĂN** — không sửa đổi, không thêm bớt

---

## ⚙️ KỸ THUẬT ĐĂNG COMMENT QUA API

### Đăng 1 comment vào bài viết
```powershell
$postId = "<POST_ID>"  # ID bài vừa đăng (lấy từ response Bước 6d)
$token = "EAF0ozkHdc7MBRFm3ElZCd6VbT1YMhnVDiqVsSZB2RVXzdYKjrajQRleRD3epkuHGQZAy574EZCksnx7m2Vpyhaz9QiK1A2obOQKWcGCCu3ufwY6HYQAIqpuMHTVqVHEJzPLqheKXZCEAZCdPBuZAzfmGEvKenYYFnHKY26dEyO0OEcS2w5Rw6d1FVNg4e0AbDdX2n0GO2qk"
$comment = "<NỘI_DUNG_COMMENT>"

$encodedComment = [System.Net.WebUtility]::UrlEncode($comment)
$uri = "https://graph.facebook.com/v19.0/$postId/comments"
$body = "message=$encodedComment&access_token=$token"

try {
    $response = Invoke-RestMethod -Uri $uri -Method Post -Body $body -ContentType "application/x-www-form-urlencoded"
    Write-Host "Comment ID: $($response.id)"
} catch {
    $errorStream = $_.Exception.Response.GetResponseStream()
    $reader = New-Object System.IO.StreamReader($errorStream)
    $errorBody = $reader.ReadToEnd() | ConvertFrom-Json
    Write-Host "Loi: $($errorBody.error.message)"
}
```

### Đăng batch Mega Comments (có delay)
```powershell
$postId = "<POST_ID>"
$token = "<TOKEN>"

# Lưu comments vào file JSON UTF-8 trước (tránh lỗi encoding)
$commentsFile = "t:\Antigravity\GiaiMa360\drafts\temp_mega_comments.json"
$commentsData = Get-Content $commentsFile -Raw -Encoding UTF8 | ConvertFrom-Json

foreach ($comment in $commentsData.comments) {
    $encodedComment = [System.Net.WebUtility]::UrlEncode($comment)
    $uri = "https://graph.facebook.com/v19.0/$postId/comments"
    $body = "message=$encodedComment&access_token=$token"
    
    try {
        $response = Invoke-RestMethod -Uri $uri -Method Post -Body $body -ContentType "application/x-www-form-urlencoded"
        Write-Host "Posted comment: $($response.id)"
    } catch {
        Write-Host "Error posting comment"
    }
    
    # Delay 3 giây giữa mỗi comment (tránh rate limit)
    Start-Sleep -Seconds 3
}
```

---

## ⚠️ LƯU Ý KỸ THUẬT

### Encoding
- **LUÔN viết tiếng Việt CÓ DẤU** — JSON UTF-8 hỗ trợ tốt
- **KHÔNG dùng emoji keycap** (1️⃣ 2️⃣) trong code → lỗi surrogates
- **Dùng thay thế:** `1.` `2.` hoặc emoji text thường (🔍 ⚖️ 💡)

### Lưu comments
- Lưu trong file JSON: `drafts/temp_mega_comments.json`
- Script đọc từ JSON → post qua Facebook API → tránh encoding PowerShell

### Lọc tự động với Compliance Shield
- 🛡️ **COMPLIANCE GATE:** TRƯỚC KHI lưu và đăng API, Agent 04 PHẢI quét từng comment qua hệ thống `.shared/compliance_shield.md` (Blacklist T1 + T2).
- Nếu phát hiện từ cấm → **Dừng lại ngay lập tức** → báo Sếp, KHÔNG được thực thi `Invoke-RestMethod`.

### Rate limit
- `Start-Sleep -Seconds 3` giữa mỗi comment
- Không đăng quá 30 comments/phút trên 1 page

### Template JSON
```json
{
  "post_id": "PAGE_ID_POST_ID",
  "title": "Tên bài ngắn gọn",
  "comments": [
    "🔍 1. MỸ ĐANG ĐÁNH VÀO ĐÂU?\n\nNhiều anh em nghĩ đây chỉ là \"đánh thuế\" đơn thuần...\n\n💡 Ai kiểm soát chip, người đó kiểm soát thế giới.",
    "⚖️ 2. TRUNG QUỐC ĐÁP TRẢ BẰNG GÌ?\n\n...",
    "🎬 Xem full video phân tích chi tiết — Giải Mã 360:\n👉 https://www.youtube.com/channel/UCPDfSFNU08CLMPD3l4Bp8Og",
    "💬 Tham gia Group Bàn Luận Thời Sự của Giải Mã 360 — nơi anh em trao đổi, tranh luận, cùng hiểu thế giới:\n👉 https://www.facebook.com/share/g/1DmLcHA8Rb/"
  ]
}
```

---

## 🚨 LỖI THƯỜNG GẶP — BẮT BUỘC ĐỌC

| Lỗi | Mô tả | Quy tắc |
|---|---|---|
| Viết comment KHÔNG DẤU | AI sợ encoding → tự viết không dấu | ❌ NGHIÊM CẤM. JSON UTF-8 hỗ trợ tiếng Việt 100% |
| Hardcode text trong Python/PowerShell | Lỗi UnicodeEncodeError | ✅ LUÔN lưu nội dung trong file JSON riêng |
| Gộp 2 CTA thành 1 comment | Giảm engagement | ✅ LUÔN tách riêng thành 2 comment |
| Quên 2 CTA cuối | Mất traffic về YouTube/Group | ✅ KHÔNG BAO GIỜ bỏ qua |
| Ngôn từ "thối mồm" (E14) | Seeding nhập vai quá trớn, xúc phạm | ✅ LUÔN quét qua `.shared/compliance_shield.md` |

---

## 📚 THAM CHIẾU

| File | Mục đích |
|---|---|
| `.shared/compliance_shield.md` | 🛡️ Bộ quét từ cấm T1+T2 chuyên dụng (BẮT BUỘC ĐỌC) |
| `.shared/viet_bai_viral.md` | Nội dung bài viết (source cho mega comments) |
| `.shared/tone_guide.md` | Giọng "Người Giải Mã" |
| `.shared/tu_cam.md` | Từ tục, Clickbait rỗng |
| `skills/dang_fanpage_skill.md` | Quy trình đăng bài (lấy Post ID) |
