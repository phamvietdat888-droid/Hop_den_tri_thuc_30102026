import sys
import os

sys.path.append(r't:\CLAUDE\Hop_Den_Tri_Thuc\scripts')
from md_to_docx_v2 import convert_md_to_docx

def main():
    yt_dir = r't:\CLAUDE\Hop_Den_Tri_Thuc\outputs\2026-07-24_Can_Bo_So_Sai\YouTube'
    outputs_dir = r't:\CLAUDE\Hop_Den_Tri_Thuc\outputs'
    
    script_md = os.path.join(yt_dir, '06_kich_ban_rut_ngon_720_tu.md')
    script_docx = os.path.join(yt_dir, '06_kich_ban_rut_ngon_720_tu.docx')
    so_sai_2_docx = os.path.join(outputs_dir, 'Sợ sai 2.docx')
    
    print(f"Converting: {script_md} -> {script_docx}")
    convert_md_to_docx(script_md, script_docx)
    
    print(f"Converting: {script_md} -> {so_sai_2_docx}")
    convert_md_to_docx(script_md, so_sai_2_docx)
    
    print("ALL DONE CONVERTING SCRIPT TO DOCX!")

if __name__ == '__main__':
    main()
