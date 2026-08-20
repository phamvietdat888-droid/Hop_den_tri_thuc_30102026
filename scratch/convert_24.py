import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))
from md_to_docx_v2 import convert_md_to_docx

root = r't:\CLAUDE\Hop_Den_Tri_Thuc'

convert_md_to_docx(
    os.path.join(root, 'drafts', '24_ngan_hang_san_tmdt_chia_se_du_lieu_thue.md'),
    os.path.join(root, 'outputs', '2026-08-20_Ngan_Hang_San_TMDT_Chia_Se_Du_Lieu_Thue', 'Facebook', '06_bai_viet.docx')
)

convert_md_to_docx(
    os.path.join(root, 'drafts', '24_goi_seo.md'),
    os.path.join(root, 'outputs', '2026-08-20_Ngan_Hang_San_TMDT_Chia_Se_Du_Lieu_Thue', 'Facebook', '06b_goi_seo.docx')
)

print("Done!")
