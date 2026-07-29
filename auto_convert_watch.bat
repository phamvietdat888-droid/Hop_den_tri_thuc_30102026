@echo off
setlocal
cd /d "%~dp0"
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0scripts\watch_markdown_to_docx.ps1" -ProjectRoot "%~dp0."
pause
