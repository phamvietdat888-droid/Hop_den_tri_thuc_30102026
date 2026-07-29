import os
import sys
sys.path.insert(0, os.path.abspath('.'))
from scripts.md_to_docx_v2 import convert_md_to_docx

in_md = os.path.abspath('drafts/de_xuat_trend_2026-07-30.md')
out_docx = os.path.abspath('outputs/2026-07-30_Trinh_Sat_Trend/00_de_xuat_trend.docx')

os.makedirs(os.path.dirname(out_docx), exist_ok=True)
convert_md_to_docx(in_md, out_docx)
print("SUCCESS:", out_docx)
