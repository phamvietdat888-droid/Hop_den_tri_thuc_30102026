# cleanup_workspace.ps1
# Script dọn dẹp workspace Giải Mã 360 tự động và an toàn.
# Chạy script bằng cách: powershell -ExecutionPolicy Bypass -File scripts\cleanup_workspace.ps1

$ErrorActionPreference = "Continue"
$ProjectRoot = Resolve-Path "$PSScriptRoot\.."

Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host "BẮT ĐẦU DỌN DẸP WORKSPACE: $ProjectRoot" -ForegroundColor Cyan
Write-Host "==========================================================" -ForegroundColor Cyan

# Hàm xóa file an toàn, tránh bị dừng chương trình nếu file bị khóa bởi Google Drive
function Remove-Safe {
    param(
        [string]$Path,
        [switch]$Recurse,
        [switch]$Force
    )
    if (Test-Path -LiteralPath $Path) {
        try {
            Write-Host "Đang xóa: $Path" -ForegroundColor Gray
            if ($Recurse) {
                Remove-Item -LiteralPath $Path -Recurse -Force -ErrorAction Stop
            } else {
                Remove-Item -LiteralPath $Path -Force -ErrorAction Stop
            }
            Write-Host "=> ĐÃ XÓA THÀNH CÔNG" -ForegroundColor Green
        } catch {
            Write-Warning "Không thể xóa: $Path. Lỗi: $_"
        }
    }
}

# 1. Xóa các file rác FUSE ẩn và file tạm ở gốc
Write-Host "`n[1/5] Xóa các file rác hệ thống và file tạm ở gốc..." -ForegroundColor Yellow
$fuseFiles = Get-ChildItem -Path $ProjectRoot -Filter ".fuse_hidden*" -Force
foreach ($file in $fuseFiles) {
    Remove-Safe -Path $file.FullName
}

Remove-Safe -Path (Join-Path $ProjectRoot ".antigravityignore.k31MBi")
Remove-Safe -Path (Join-Path $ProjectRoot "XXFQepwv")
Remove-Safe -Path (Join-Path $ProjectRoot ".agents") -Recurse
Remove-Safe -Path (Join-Path $ProjectRoot "_to_delete") -Recurse

# 2. Xóa các file FUSE trong thư mục .agent/agents/ và .agent/workflows/
Write-Host "`n[2/5] Xóa các file rác FUSE trong thư mục .agent..." -ForegroundColor Yellow
$agentFuse = Get-ChildItem -Path (Join-Path $ProjectRoot ".agent") -Filter ".fuse_hidden*" -Recurse -Force
foreach ($file in $agentFuse) {
    Remove-Safe -Path $file.FullName
}

# 3. Dọn dẹp drafts/ (Chỉ xóa nội dung bên trong, giữ lại thư mục drafts/)
Write-Host "`n[3/5] Dọn dẹp thư mục drafts/..." -ForegroundColor Yellow
$draftsPath = Join-Path $ProjectRoot "drafts"
if (Test-Path -LiteralPath $draftsPath) {
    $draftItems = Get-ChildItem -Path $draftsPath -Force
    foreach ($item in $draftItems) {
        Remove-Safe -Path $item.FullName -Recurse
    }
}

# 4. Dọn dẹp scratch/ (Chỉ xóa nội dung bên trong, giữ lại thư mục scratch/)
Write-Host "`n[4/5] Dọn dẹp thư mục scratch/..." -ForegroundColor Yellow
$scratchPath = Join-Path $ProjectRoot "scratch"
if (Test-Path -LiteralPath $scratchPath) {
    $scratchItems = Get-ChildItem -Path $scratchPath -Force
    foreach ($item in $scratchItems) {
        Remove-Safe -Path $item.FullName -Recurse
    }
}

# 5. Xóa các file .md lẻ tẻ nằm ngoài quy hoạch ở outputs/ (không xóa thư mục con của outputs/)
Write-Host "`n[5/5] Xóa các file .md lẻ tẻ tại thư mục outputs/..." -ForegroundColor Yellow
$outputsPath = Join-Path $ProjectRoot "outputs"
if (Test-Path -LiteralPath $outputsPath) {
    $outputsFiles = Get-ChildItem -Path $outputsPath -File -Filter "*.md" -Force
    foreach ($file in $outputsFiles) {
        Remove-Safe -Path $file.FullName
    }
}

Write-Host "`n==========================================================" -ForegroundColor Cyan
Write-Host "HOÀN TẤT QUY TRÌNH DỌN DẸP" -ForegroundColor Cyan
Write-Host "==========================================================" -ForegroundColor Cyan
