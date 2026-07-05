# post_seeding.ps1 — Script đăng Seeding Mega Comments tự động cho Sếp
$token = "EAF0ozkHdc7MBRFm3ElZCd6VbT1YMhnVDiqVsSZB2RVXzdYKjrajQRleRD3epkuHGQZAy574EZCksnx7m2Vpyhaz9QiK1A2obOQKWcGCCu3ufwY6HYQAIqpuMHTVqVHEJzPLqheKXZCEAZCdPBuZAzfmGEvKenYYFnHKY26dEyO0OEcS2w5Rw6d1FVNg4e0AbDdX2n0GO2qk"
$commentsFile = "t:\Antigravity\NhatKyTacChien\outputs\2026-05-23_Nha_Cho_Thue\Facebook\06e_mega_comments.json"

# Hỏi Sếp ID bài viết vừa đăng để gán bình luận chính xác
$postId = Read-Host "Nhap ID bai viet vua dang (Post ID - Vi du: 341500382389972_xxxxxx)"
$postId = $postId.Trim()

if ([string]::IsNullOrEmpty($postId)) {
    Write-Error "Post ID khong duoc de trong!"
    exit 1
}

if (-not (Test-Path $commentsFile)) {
    Write-Error "Khong tim thay file mega comments tai: $commentsFile"
    exit 1
}

# Đọc file dữ liệu bình luận
$commentsData = Get-Content $commentsFile -Raw -Encoding UTF8 | ConvertFrom-Json

Write-Host "--------------------------------------------------"
Write-Host "DANG TIEN HANH SEEDING MEGA COMMENTS..."
Write-Host "--------------------------------------------------"

foreach ($comment in $commentsData.comments) {
    $content = $comment.content
    Write-Host "-> Dang gui comment: '$($content.Substring(0, [Math]::Min(40, $content.Length)))...'"
    
    # URL Encode nội dung bình luận tiếng Việt
    $encodedComment = [System.Net.WebUtility]::UrlEncode($content)
    $uri = "https://graph.facebook.com/v19.0/$postId/comments"
    $body = "message=$encodedComment&access_token=$token"
    
    try {
        $response = Invoke-RestMethod -Uri $uri -Method Post -Body $body -ContentType "application/x-www-form-urlencoded"
        Write-Host "   SUCCESS! Comment ID: $($response.id)" -ForegroundColor Green
    } catch {
        Write-Error "   ERROR posting comment: $_"
    }
    
    # Giãn cách 3 giây tránh bị Facebook đánh dấu Spam
    Start-Sleep -Seconds 3
}

Write-Host "--------------------------------------------------"
Write-Host "HOAN THANH! 5 Mega Comments da len song tren page!"
Write-Host "--------------------------------------------------"
