@echo off
echo ========================================================
echo   GiaiMa360 - Complete Pipeline DOCX Converter Tool
echo ========================================================
echo Converting markdown files to DOCX format...

:: 1. Convert YouTube Script
python scripts\md_to_docx_v2.py outputs\2026-07-19_Nang_Diem_Tuyen_Quang_Va_Bang_Cap\YouTube\06_kich_ban_hoan_thien.md outputs\2026-07-19_Nang_Diem_Tuyen_Quang_Va_Bang_Cap\YouTube\06_kich_ban_hoan_thien.docx

:: 2. Convert YouTube SEO Package
python scripts\md_to_docx_v2.py outputs\2026-07-19_Nang_Diem_Tuyen_Quang_Va_Bang_Cap\YouTube\06b_goi_seo.md outputs\2026-07-19_Nang_Diem_Tuyen_Quang_Va_Bang_Cap\YouTube\06b_goi_seo.docx

:: 3. Convert Facebook Post
python scripts\md_to_docx_v2.py outputs\2026-07-19_Nang_Diem_Tuyen_Quang_Va_Bang_Cap\Facebook\06d_bai_dang_fb.md outputs\2026-07-19_Nang_Diem_Tuyen_Quang_Va_Bang_Cap\Facebook\06d_bai_dang_fb.docx

:: 4. Convert YouTube Shorts #01 & #02
python scripts\md_to_docx_v2.py outputs\2026-07-19_Nang_Diem_Tuyen_Quang_Va_Bang_Cap\YouTube_Shorts\short_01\short_01.md outputs\2026-07-19_Nang_Diem_Tuyen_Quang_Va_Bang_Cap\YouTube_Shorts\short_01\short_01.docx
python scripts\md_to_docx_v2.py outputs\2026-07-19_Nang_Diem_Tuyen_Quang_Va_Bang_Cap\YouTube_Shorts\short_02\short_02.md outputs\2026-07-19_Nang_Diem_Tuyen_Quang_Va_Bang_Cap\YouTube_Shorts\short_02\short_02.docx

:: 5. Convert Trend Report & Outline
python scripts\md_to_docx_v2.py scratch\2026-07-19_Bao_Cao_Trinh_Sat_Trend.md outputs\2026-07-19_Bao_Cao_Trinh_Sat_Trend.docx
python scripts\md_to_docx_v2.py outputs\2026-07-19_Nang_Diem_Tuyen_Quang_Va_Bang_Cap\YouTube\03_dan_y.md outputs\2026-07-19_Nang_Diem_Tuyen_Quang_Va_Bang_Cap/YouTube/03_dan_y.docx

echo.
echo ========================================================
echo   All conversions completed successfully!
echo ========================================================
pause
