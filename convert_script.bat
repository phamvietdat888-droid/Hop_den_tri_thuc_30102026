@echo off
setlocal enabledelayedexpansion
cd /d "%~dp0"

rem === Chi convert rieng file kich ban chinh YouTube (06_kich_ban_hoan_thien.md) ===
rem Cach dung:
rem   1) Keo-tha thu muc chu de vao file .bat nay, HOAC
rem   2) Chay: convert_script.bat "Ten_Chu_De" (ten thu muc trong outputs\), HOAC
rem   3) Double-click truc tiep -> tu dong lay thu muc MOI NHAT trong outputs\

set "TOPIC_ARG=%~1"
set "BASE="

if "%TOPIC_ARG%"=="" goto :skiparg
if exist "%TOPIC_ARG%\" set "BASE=%TOPIC_ARG%"
if "%BASE%"=="" if exist "outputs\%TOPIC_ARG%\" set "BASE=outputs\%TOPIC_ARG%"
:skiparg

if not "%BASE%"=="" goto :skipsearch
for /f "delims=" %%D in ('dir /b /ad /o-d "outputs\20*_*" 2^>nul') do (
    set "BASE=outputs\%%D"
    goto :skipsearch
)
:skipsearch

if "%BASE%"=="" (
    echo [LOI] Khong tim thay thu muc chu de nao trong outputs\
    echo Cach dung: convert_script.bat "Ten_Chu_De"  ^(hoac keo-tha thu muc vao file nay^)
    pause
    exit /b 1
)

set "MD_FILE=%BASE%\YouTube\06_kich_ban_hoan_thien.md"

echo ========================================================
echo   GiaiMa360 - Convert YouTube Script to DOCX
echo   Chu de: %BASE%
echo ========================================================

if not exist "%MD_FILE%" (
    echo [LOI] Khong tim thay: %MD_FILE%
    pause
    exit /b 1
)

powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0scripts\convert_markdown_to_docx.ps1" -ProjectRoot "%~dp0." -InputMd "%MD_FILE%" -OutputDocx "%BASE%\YouTube\06_kich_ban_hoan_thien.docx"

if errorlevel 1 (
    echo.
    echo [LOI] Convert that bai. Xem thong bao loi ben tren.
    pause
    exit /b 1
)

echo.
echo ========================================================
echo Saved: %BASE%\YouTube\06_kich_ban_hoan_thien.docx
echo ========================================================
pause


