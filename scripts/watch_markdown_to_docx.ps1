param(
    [string]$ProjectRoot = "",
    [string]$Topic = ""
)

$ErrorActionPreference = "Stop"

if ([string]::IsNullOrWhiteSpace($ProjectRoot)) {
    $ProjectRoot = Split-Path -Parent $PSScriptRoot
}

$ProjectRoot = (Resolve-Path -LiteralPath $ProjectRoot).Path
if ([string]::IsNullOrWhiteSpace($Topic)) {
    $candidates = Get-ChildItem -LiteralPath (Join-Path $ProjectRoot "outputs") -Directory -Filter "20*_*" | Sort-Object LastWriteTime -Descending
    if (-not $candidates) {
        throw "No topic folder found in outputs."
    }
    $TopicPath = $candidates[0].FullName
} elseif ([System.IO.Path]::IsPathRooted($Topic)) {
    $TopicPath = (Resolve-Path -LiteralPath $Topic).Path
} else {
    $TopicPath = Join-Path (Join-Path $ProjectRoot "outputs") $Topic
    $TopicPath = (Resolve-Path -LiteralPath $TopicPath).Path
}

$Converter = Join-Path $ProjectRoot "scripts\convert_markdown_to_docx.ps1"
$known = @{}

Write-Host "[WATCH] Project: $ProjectRoot"
Write-Host "[WATCH] Topic:   $TopicPath"
Write-Host "[WATCH] Auto-converting changed .md files. Press Ctrl+C to stop."

while ($true) {
    Get-ChildItem -LiteralPath $TopicPath -Recurse -Filter "*.md" | ForEach-Object {
        $md = $_.FullName
        $docx = [System.IO.Path]::ChangeExtension($md, ".docx")
        $key = $md.ToLowerInvariant()
        $stamp = $_.LastWriteTimeUtc.Ticks
        $docxIsStale = -not (Test-Path -LiteralPath $docx) -or ((Get-Item -LiteralPath $docx).LastWriteTimeUtc -lt $_.LastWriteTimeUtc)

        if ($docxIsStale -and ((-not $known.ContainsKey($key)) -or $known[$key] -ne $stamp)) {
            $known[$key] = $stamp
            Write-Host ""
            Write-Host "[WATCH] Changed: $md"
            & powershell -NoProfile -ExecutionPolicy Bypass -File $Converter -ProjectRoot $ProjectRoot -InputMd $md -OutputDocx $docx
        }
    }
    Start-Sleep -Seconds 3
}
