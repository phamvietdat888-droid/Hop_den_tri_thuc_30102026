@echo off
echo ========================================================
echo   Converting YouTube scripts to DOCX...
echo ========================================================

echo -- Converting 06_kich_ban_hoan_thien.md
python scripts\md_to_docx_v2.py outputs\2026-07-26_Hanh_Trinh_500_Ngay_Dem_Tim_Hai_Cot_Liet_Si\YouTube\06_kich_ban_hoan_thien.md outputs\2026-07-26_Hanh_Trinh_500_Ngay_Dem_Tim_Hai_Cot_Liet_Si\YouTube\06_kich_ban_hoan_thien.docx

echo -- Converting 06g_kich_ban_rut_gon_160_tu.md
python scripts\md_to_docx_v2.py outputs\2026-07-26_Hanh_Trinh_500_Ngay_Dem_Tim_Hai_Cot_Liet_Si\YouTube\06g_kich_ban_rut_gon_160_tu.md outputs\2026-07-26_Hanh_Trinh_500_Ngay_Dem_Tim_Hai_Cot_Liet_Si\YouTube\06g_kich_ban_rut_gon_160_tu.docx

echo Done!
pause
