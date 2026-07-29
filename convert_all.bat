@echo off
setlocal enabledelayedexpansion
cd /d "%~dp0"

rem === Xac dinh thu muc chu de ===
rem Cach dung:
rem   1) Keo-tha thu muc chu de vao file .bat nay, HOAC
rem   2) Chay: convert_all.bat "Ten_Chu_De" (ten thu muc trong outputs\), HOAC
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
    echo Cach dung: convert_all.bat "Ten_Chu_De"  ^(hoac keo-tha thu muc vao file nay^)
    pause
    exit /b 1
)

if not exist "%BASE%\" (
    echo [LOI] Khong tim thay thu muc: %BASE%
    pause
    exit /b 1
)

echo ========================================================
echo   GiaiMa360 - Complete Pipeline DOCX Converter Tool
echo   Chu de: %BASE%
echo ========================================================

rem === Danh sach file chuan v3.2 (duong dan tuong doi trong BASE, khong co duoi) ===
set "FILES=YouTube\06_kich_ban_hoan_thien YouTube\06b_goi_seo YouTube\06e_seeding_comments Facebook\06d_bai_dang_fb YouTube_Shorts\06f_shorts_scripts"

set "CONVERTED=0"
for %%F in (%FILES%) do (
    if exist "%BASE%\%%F.md" (
        echo.
        echo -- Converting %%F.md
        powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0scripts\convert_markdown_to_docx.ps1" -ProjectRoot "%~dp0." -InputMd "%BASE%\%%F.md" -OutputDocx "%BASE%\%%F.docx"
        if errorlevel 1 (
            echo.
            echo [LOI] Convert that bai: %BASE%\%%F.md
            pause
            exit /b 1
        )
        set /a CONVERTED+=1
    )
)

echo.
if %CONVERTED%==0 (
    echo ========================================================
    echo   Khong tim thay file .md nao de convert trong %BASE%
    echo ========================================================
) else (
    echo ========================================================
    echo   Hoan tat. Da convert %CONVERTED% file .docx trong: %BASE%
    echo ========================================================
)
pause
