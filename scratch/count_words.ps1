param([string]$FilePath)
$content = Get-Content -Path $FilePath -Encoding UTF8 -Raw
$words = ($content -split '\s+').Count
$emDashes = ([regex]::Matches($content, '—')).Count
Write-Host "Total words: $words"
Write-Host "Total em-dashes: $emDashes"
