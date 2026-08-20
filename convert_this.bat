@echo off
echo ========================================================
echo   Converting YouTube scripts to DOCX...
echo ========================================================

echo -- Converting 06_kich_ban_hoan_thien.md
python scripts\md_to_docx_v2.py outputs\2026-07-26_Hanh_Trinh_500_Ngay_Dem_Tim_Hai_Cot_Liet_Si\YouTube\06_kich_ban_hoan_thien.md outputs\2026-07-26_Hanh_Trinh_500_Ngay_Dem_Tim_Hai_Cot_Liet_Si\YouTube\06_kich_ban_hoan_thien.docx

echo -- Converting 06_bai_viet_va_goi_seo_giao_duc_2045.md
python scripts\md_to_docx_v2.py outputs\2026-08-13_Dau_Tu_Giao_Duc_2045\06_bai_viet_va_goi_seo_giao_duc_2045.md outputs\2026-08-13_Dau_Tu_Giao_Duc_2045\06_bai_viet_va_goi_seo_giao_duc_2045.docx
python scripts\md_to_docx_v2.py outputs\2026-08-13_Dau_Tu_Giao_Duc_2045\YouTube\06_kich_ban_hoan_thien.md outputs\2026-08-13_Dau_Tu_Giao_Duc_2045\YouTube\06_kich_ban_hoan_thien.docx
python scripts\md_to_docx_v2.py outputs\2026-08-16_Huan_Hoa_Hong_Bi_Khoi_To\YouTube\06_kich_ban_hoan_thien.md outputs\2026-08-16_Huan_Hoa_Hong_Bi_Khoi_To\YouTube\06_kich_ban_hoan_thien.docx
python scripts\md_to_docx_v2.py outputs\2026-08-16_Huan_Hoa_Hong_Bi_Khoi_To\YouTube\06b_goi_seo.md outputs\2026-08-16_Huan_Hoa_Hong_Bi_Khoi_To\YouTube\06b_goi_seo.docx
python scripts\md_to_docx_v2.py outputs\2026-08-16_Giai_Ma_Huan_Ban_Nuoc_Hoa_300_Ty\YouTube\06_kich_ban_hoan_thien.md outputs\2026-08-16_Giai_Ma_Huan_Ban_Nuoc_Hoa_300_Ty\YouTube\06_kich_ban_hoan_thien.docx
python scripts\md_to_docx_v2.py outputs\2026-08-16_Giai_Ma_Huan_Ban_Nuoc_Hoa_300_Ty\YouTube\06b_goi_seo.md outputs\2026-08-16_Giai_Ma_Huan_Ban_Nuoc_Hoa_300_Ty\YouTube\06b_goi_seo.docx
python scripts\md_to_docx_v2.py outputs\2026-08-16_Bai_Viet_Hoan_Thien_Huan_Hoa_Hong\YouTube\06_kich_ban_hoan_thien.md outputs\2026-08-16_Bai_Viet_Hoan_Thien_Huan_Hoa_Hong\YouTube\06_kich_ban_hoan_thien.docx
python scripts\md_to_docx_v2.py outputs\2026-08-16_Bai_Viet_Hoan_Thien_Huan_Hoa_Hong\YouTube\06b_goi_seo.md outputs\2026-08-16_Bai_Viet_Hoan_Thien_Huan_Hoa_Hong\YouTube\06b_goi_seo.docx

python scripts\md_to_docx_v2.py outputs\2026-08-16_Can_Bao_Nhieu_Tien_De_Nghi_Huu_Thoai_Mai\Facebook\06d_bai_dang_fb.md outputs\2026-08-16_Can_Bao_Nhieu_Tien_De_Nghi_Huu_Thoai_Mai\Facebook\06d_bai_dang_fb.docx
python scripts\md_to_docx_v2.py outputs\2026-08-16_Can_Bao_Nhieu_Tien_De_Nghi_Huu_Thoai_Mai\YouTube\06b_goi_seo.md outputs\2026-08-16_Can_Bao_Nhieu_Tien_De_Nghi_Huu_Thoai_Mai\YouTube\06b_goi_seo.docx
python scripts\md_to_docx_v2.py outputs\2026-08-17_Tu_Duy_Chinh_Quyen_Moi\06_bai_viet_tu_duy_chinh_quyen.md outputs\2026-08-17_Tu_Duy_Chinh_Quyen_Moi\06_bai_viet_tu_duy_chinh_quyen.docx
python scripts\md_to_docx_v2.py outputs\2026-08-17_Tu_Duy_Chinh_Quyen_Moi\06b_goi_seo.md outputs\2026-08-17_Tu_Duy_Chinh_Quyen_Moi\06b_goi_seo.docx

echo Done!
pause



