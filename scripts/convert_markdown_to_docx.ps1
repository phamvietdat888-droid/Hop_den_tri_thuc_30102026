param(
    [Parameter(Mandatory = $true)]
    [string]$InputMd,

    [string]$OutputDocx = "",

    [string]$ProjectRoot = ""
)

$ErrorActionPreference = "Stop"

if ([string]::IsNullOrWhiteSpace($ProjectRoot)) {
    $ProjectRoot = Split-Path -Parent $PSScriptRoot
}

$ProjectRoot = (Resolve-Path -LiteralPath $ProjectRoot).Path
$Converter = Join-Path $ProjectRoot "scripts\md_to_docx_v2.py"

function Resolve-ProjectPath {
    param([string]$PathValue)

    if ([System.IO.Path]::IsPathRooted($PathValue)) {
        return $PathValue
    }

    return (Join-Path $ProjectRoot $PathValue)
}

function Test-FileLocked {
    param([string]$PathValue)

    if (-not (Test-Path -LiteralPath $PathValue)) {
        return $false
    }

    $stream = $null
    try {
        $stream = [System.IO.File]::Open($PathValue, 'Open', 'ReadWrite', 'None')
        return $false
    } catch [System.IO.IOException] {
        return $true
    } catch [System.UnauthorizedAccessException] {
        return $true
    } finally {
        if ($stream) {
            $stream.Close()
            $stream.Dispose()
        }
    }
}

$InputMd = Resolve-ProjectPath $InputMd

if ([string]::IsNullOrWhiteSpace($OutputDocx)) {
    $OutputDocx = [System.IO.Path]::ChangeExtension($InputMd, ".docx")
} else {
    $OutputDocx = Resolve-ProjectPath $OutputDocx
}

if (-not (Test-Path -LiteralPath $Converter)) {
    throw "Converter not found: $Converter"
}

if (-not (Test-Path -LiteralPath $InputMd)) {
    throw "Input markdown not found: $InputMd"
}

$RequestedOutputDocx = $OutputDocx
$OutputDir = Split-Path -Parent $OutputDocx
if (-not [string]::IsNullOrWhiteSpace($OutputDir) -and -not (Test-Path -LiteralPath $OutputDir)) {
    New-Item -ItemType Directory -Path $OutputDir -Force | Out-Null
}

if (Test-FileLocked $OutputDocx) {
    $stamp = Get-Date -Format "yyyyMMdd_HHmmss"
    $name = [System.IO.Path]::GetFileNameWithoutExtension($OutputDocx)
    $OutputDocx = Join-Path $OutputDir ("{0}_unlocked_{1}.docx" -f $name, $stamp)
    Write-Warning "Target DOCX is open/locked, so Windows will not allow overwrite: $RequestedOutputDocx"
    Write-Warning "Created a safe new DOCX instead: $OutputDocx"
}

$PythonCmd = Get-Command python -ErrorAction SilentlyContinue
$PythonArgs = @()

if ($PythonCmd) {
    $PythonExe = $PythonCmd.Source
} else {
    $PyCmd = Get-Command py -ErrorAction SilentlyContinue
    if (-not $PyCmd) {
        throw "Python was not found. Install Python 3 or add it to PATH."
    }
    $PythonExe = $PyCmd.Source
    $PythonArgs = @("-3")
}

Write-Host "[INFO] Project: $ProjectRoot"
Write-Host "[INFO] Input:   $InputMd"
Write-Host "[INFO] Output:  $OutputDocx"

& $PythonExe @PythonArgs $Converter $InputMd $OutputDocx
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}

if (-not (Test-Path -LiteralPath $OutputDocx)) {
    throw "DOCX was not created: $OutputDocx"
}

if ($OutputDocx -ne $RequestedOutputDocx) {
    Write-Host "[OK] DOCX created without overwriting locked file: $OutputDocx"
    Write-Host "[NOTE] Close the locked file, then run conversion again to update the original name: $RequestedOutputDocx"
} else {
    Write-Host "[OK] DOCX created: $OutputDocx"
}
