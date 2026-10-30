@echo off
cd /d "%~dp0"
echo ========================================================
echo   Hop Den Tri Thuc - Git Push Tool
echo ========================================================
echo.

:: Check if git is installed
where git >nul 2>nul
if %errorlevel% neq 0 (
    echo [ERROR] Git is not installed or not in PATH. Please install Git and try again.
    pause
    exit /b
)

echo Initializing Git repository if not already done...
if not exist .git (
    git init
)

echo.
echo Staging all project files...
git add .

echo.
echo Committing files...
git commit -m "Cap nhat toan bo du an Hop Den Tri Thuc ngay 30/10/2026"

echo.
echo Setting remote repository...
git remote remove origin >nul 2>nul
git remote add origin https://github.com/phamvietdat888-droid/Hop_den_tri_thuc_30102026.git

echo.
echo Renaming default branch to main...
git branch -M main

echo.
echo Pushing to GitHub (origin/main)...
echo [NOTE] If a login window appears, please authorize to continue the push.
git push -u origin main --force

echo.
echo ========================================================
echo   Push process finished!
echo ========================================================
pause
