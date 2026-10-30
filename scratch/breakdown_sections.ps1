param([string]$FilePath)
$lines = Get-Content -Path $FilePath -Encoding UTF8
$currentSection = "Header"
$sectionWords = @{}

foreach ($line in $lines) {
    if ($line -match '^##\s+(.+)$' -or $line -match '^###\s+(.+)$') {
        $currentSection = $matches[1]
        if (-not $sectionWords.ContainsKey($currentSection)) {
            $sectionWords[$currentSection] = 0
        }
    } else {
        $w = ($line.Trim() -split '\s+' | Where-Object { $_ -ne '' }).Count
        if (-not $sectionWords.ContainsKey($currentSection)) {
            $sectionWords[$currentSection] = 0
        }
        $sectionWords[$currentSection] += $w
    }
}

foreach ($k in $sectionWords.Keys) {
    Write-Host "$k : $($sectionWords[$k]) words"
}
