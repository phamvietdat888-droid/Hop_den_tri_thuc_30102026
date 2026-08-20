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
$ConverterWrapper = Join-Path $ProjectRoot "scripts\convert_markdown_to_docx.ps1"
$PythonHome = "C:\Program Files\Python311"
$PythonExe = Join-Path $PythonHome "python.exe"

if (-not (Test-Path -LiteralPath $ConverterWrapper)) {
    throw "Converter wrapper not found: $ConverterWrapper"
}

if (-not (Test-Path -LiteralPath $PythonExe)) {
    throw "The verified Python interpreter was not found: $PythonExe"
}

# Antigravity may inherit the Microsoft Store App Execution Alias before the
# real interpreter. Prepending the verified installation prevents the alias
# from failing with "Access is denied".
$env:PATH = "$PythonHome;$PythonHome\Scripts;$env:PATH"

$pythonVersion = & $PythonExe --version 2>&1
if ($LASTEXITCODE -ne 0) {
    throw "Python could not be started: $PythonExe"
}

Write-Host "[ANTIGRAVITY] Python: $PythonExe ($pythonVersion)"

$arguments = @{
    ProjectRoot = $ProjectRoot
    InputMd     = $InputMd
}
if (-not [string]::IsNullOrWhiteSpace($OutputDocx)) {
    $arguments.OutputDocx = $OutputDocx
}

& $ConverterWrapper @arguments
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}
