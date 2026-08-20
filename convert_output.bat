@echo off
cd /d "%~dp0"
echo Converting Markdown files to DOCX...
echo.

python scripts\md_to_docx_v2.py outputs\2026-08-05_Do_Thi_San_Bay_Long_Thanh\YouTube\06_kich_ban_hoan_thien.md outputs\2026-08-05_Do_Thi_San_Bay_Long_Thanh\YouTube\06_kich_ban_hoan_thien.docx
python scripts\md_to_docx_v2.py outputs\2026-08-05_Do_Thi_San_Bay_Long_Thanh\YouTube\06b_goi_seo.md outputs\2026-08-05_Do_Thi_San_Bay_Long_Thanh\YouTube\06b_goi_seo.docx
python scripts\md_to_docx_v2.py outputs\2026-08-05_Do_Thi_San_Bay_Long_Thanh\Facebook\06d_bai_dang_fb.md outputs\2026-08-05_Do_Thi_San_Bay_Long_Thanh\Facebook\06d_bai_dang_fb.docx
python scripts\md_to_docx_v2.py outputs\2026-08-05_Do_Thi_San_Bay_Long_Thanh\YouTube_Shorts\short_01\kich_ban_short.md outputs\2026-08-05_Do_Thi_San_Bay_Long_Thanh\YouTube_Shorts\short_01\kich_ban_short.docx
python scripts\md_to_docx_v2.py outputs\2026-08-05_Do_Thi_San_Bay_Long_Thanh\YouTube_Shorts\short_02\kich_ban_short.md outputs\2026-08-05_Do_Thi_San_Bay_Long_Thanh\YouTube_Shorts\short_02\kich_ban_short.docx
python scripts\md_to_docx_v2.py outputs\2026-08-05_The_He_Sandwich_Tuoi_Gia\Facebook\06d_bai_dang_fb.md outputs\2026-08-05_The_He_Sandwich_Tuoi_Gia\Facebook\06d_bai_dang_fb.docx
python scripts\md_to_docx_v2.py outputs\2026-08-05_The_He_Sandwich_Tuoi_Gia\06b_10_tieu_de_thu_hut.md outputs\2026-08-05_The_He_Sandwich_Tuoi_Gia\06b_10_tieu_de_thu_hut.docx

echo.
echo DONE CONVERTING DOCX!
pause
