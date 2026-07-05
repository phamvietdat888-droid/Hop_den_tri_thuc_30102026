# post_to_fb.ps1 — Bản dịch chuyển bài viết & đăng Fanpage tự động cho Sếp
$pageId = "341500382389972"
$token = "EAF0ozkHdc7MBRFm3ElZCd6VbT1YMhnVDiqVsSZB2RVXzdYKjrajQRleRD3epkuHGQZAy574EZCksnx7m2Vpyhaz9QiK1A2obOQKWcGCCu3ufwY6HYQAIqpuMHTVqVHEJzPLqheKXZCEAZCdPBuZAzfmGEvKenYYFnHKY26dEyO0OEcS2w5Rw6d1FVNg4e0AbDdX2n0GO2qk"

$mdFile = "t:\Antigravity\NhatKyTacChien\outputs\2026-05-23_Nha_Cho_Thue\Facebook\06d_bai_dang_fb.md"
$imagePath = "t:\Antigravity\NhatKyTacChien\outputs\2026-05-23_Nha_Cho_Thue\Facebook\thumbnail_fb.png"
$tempFile = "t:\Antigravity\NhatKyTacChien\drafts\temp_fb_message.txt"

if (-not (Test-Path $mdFile)) {
    Write-Error "Khong tim thay file bai viet MD tai: $mdFile"
    exit 1
}

# Đọc bài viết và bỏ qua 5 dòng metadata đầu
$lines = Get-Content -Path $mdFile -Encoding UTF8
$messageLines = $lines | Select-Object -Skip 5
$message = $messageLines -join "`r`n"

# Dọn dẹp các ký tự in đậm ** trong Markdown để hiển thị text sạch trên Facebook
$message = $message -replace "\*\*",""
$message = $message.Trim()

# Lưu tin nhắn sạch vào file tạm UTF-8 không BOM để curl truyền tải chính xác tiếng Việt
$bytes = [System.Text.Encoding]::UTF8.GetBytes($message)
[System.IO.File]::WriteAllBytes($tempFile, $bytes)

Write-Host "--------------------------------------------------"
Write-Host "DANG CHUAN BI DANG BAI LEN FANPAGE CHECKVAR 247..."
Write-Host "--------------------------------------------------"

if (Test-Path $imagePath) {
    # Chế độ A: Đăng bài kèm ảnh thu nhỏ 6:16
    Write-Host "Phat hien anh thumbnail tai: $imagePath"
    Write-Host "Tien hanh dang post kem anh..."
    $uri = "https://graph.facebook.com/v19.0/$pageId/photos"
    cmd.exe /c "curl.exe --ssl-no-revoke -s -X POST `"$uri`" -F `"access_token=$token`" -F `"message=<$tempFile;type=text/plain;charset=utf-8`" -F `"source=@$imagePath`""
} else {
    # Chế độ B: Đăng bài dạng Text-Only (nếu Sếp chưa tải ảnh về thư mục Facebook)
    Write-Host "Khong tim thay anh thumbnail tai $imagePath (Sếp co the quen chua tai anh ve)." -ForegroundColor Yellow
    Write-Host "Tien hanh dang post dang van ban (Text-only)..."
    $uri = "https://graph.facebook.com/v19.0/$pageId/feed"
    cmd.exe /c "curl.exe --ssl-no-revoke -s -X POST `"$uri`" -F `"access_token=$token`" -F `"message=<$tempFile;type=text/plain;charset=utf-8`""
}

Write-Host "`n--------------------------------------------------"
Write-Host "CONG VIEC HOAN TAT! Sep check lai tren Fanpage nhe!"
Write-Host "--------------------------------------------------"
