$content = Get-Content -Path 'C:\Users\BIC-MT\.gemini\antigravity-ide\brain\efd85e27-c1f5-4d6b-999f-817acf32588a\.system_generated\steps\5\content.md' -Raw
$matches = [regex]::Matches($content, '<p[^>]*>(.*?)</p>')
foreach ($m in $matches) {
    $txt = $m.Groups[1].Value -replace '<[^>]+>', ''
    $txt = $txt.Trim()
    if ($txt.Length -gt 0) {
        Write-Host "P: $txt`n"
    }
}
