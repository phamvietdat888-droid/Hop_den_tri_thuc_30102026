@echo off
echo ========================================================
echo   GiaiMa360 - DOCX Converter Tool
echo ========================================================
echo Converting markdown files to DOCX format...

:: 1. Convert YouTube Script
python scripts\md_to_docx_v2.py outputs\2026-07-19_Bac_Ho_Giao_Duc_Khai_Phong\YouTube\06_kich_ban_hoan_thien.md outputs\2026-07-19_Bac_Ho_Giao_Duc_Khai_Phong\YouTube\06_kich_ban_hoan_thien.docx

:: 2. Convert YouTube SEO Package
python scripts\md_to_docx_v2.py outputs\2026-07-19_Bac_Ho_Giao_Duc_Khai_Phong\YouTube\06b_goi_seo.md outputs\2026-07-19_Bac_Ho_Giao_Duc_Khai_Phong\YouTube\06b_goi_seo.docx

:: 3. Convert Facebook Post
python scripts\md_to_docx_v2.py outputs\2026-07-19_Bac_Ho_Giao_Duc_Khai_Phong\Facebook\06d_bai_dang_fb.md outputs\2026-07-19_Bac_Ho_Giao_Duc_Khai_Phong\Facebook\06d_bai_dang_fb.docx

echo.
echo Copying thumbnail to target folder...
copy "C:\Users\BIC-MT\.gemini\antigravity-ide\brain\ea554ad9-64c2-4364-8905-95f00b0f3daf\youtube_thumbnail_1784452159685.png" "outputs\2026-07-19_Bac_Ho_Giao_Duc_Khai_Phong\YouTube\thumbnail.png" /Y

echo.
echo ========================================================
echo   Conversion and thumbnail copy completed successfully!
echo ========================================================
pause
