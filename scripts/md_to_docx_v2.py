"""
md_to_docx_v2.py — Chuyển đổi kịch bản Markdown (Audio Clean) → Word (.docx)
Chuẩn định dạng: Tham chiếu từ 2026-04-22_Trump_5_Thang_Lich_Su/YouTube/06_kich_ban_hoan_thien.docx
Quy chuẩn: .shared/format_output.md (mục QUY CHUẨN FILE WORD)

Sử dụng: python md_to_docx_v2.py <input.md> <output.docx>
"""

import re
import sys
import docx
from docx.shared import Pt, RGBColor, Cm, Emu
from docx.enum.text import WD_ALIGN_PARAGRAPH

# === MÀU SẮC CHUẨN (từ file mẫu) ===
COLOR_MAP = {
    'red': RGBColor(204, 0, 0),       # CC0000 — Nhấn mạnh, bức xúc
    'green': RGBColor(0, 128, 0),      # 008000 — Dữ liệu, con số
    'blue': RGBColor(0, 102, 204),     # 0066CC — Mỉa mai, châm biếm
    'orange': RGBColor(230, 80, 0),    # E65000 — Câu hỏi, tò mò
}
COLOR_BLACK = RGBColor(0, 0, 0)
COLOR_DIVIDER = RGBColor(200, 200, 200)  # C8C8C8
DIVIDER_CHAR = '─' * 40


def parse_inline(text):
    """
    Parse inline formatting: <red>, <green>, <blue>, <orange>, <underline>,
    **bold**, *italic* — trả về list các segment:
    [{'text': ..., 'color': RGBColor|None, 'bold': bool, 'italic': bool, 'underline': bool}, ...]
    """
    segments = []
    
    # Regex tìm tất cả thẻ inline
    # Thứ tự: color tags > underline > bold > italic
    pattern = re.compile(
        r'<(red|green|blue|orange|underline)>(.*?)</\1>'
        r'|\*\*(.+?)\*\*'
        r'|\*(.+?)\*'
        r'|([^<*]+)'
        r'|(.)',  # fallback cho ký tự lẻ
        re.DOTALL
    )
    
    for m in pattern.finditer(text):
        if m.group(1):  # Color/underline tag
            tag = m.group(1)
            inner = m.group(2)
            if tag == 'underline':
                # Parse nội dung bên trong cho bold/italic
                for sub in _parse_bold_italic(inner):
                    sub['underline'] = True
                    segments.append(sub)
            else:
                color = COLOR_MAP[tag]
                for sub in _parse_bold_italic(inner):
                    sub['color'] = color
                    segments.append(sub)
        elif m.group(3):  # **bold**
            segments.append({
                'text': m.group(3), 'color': None,
                'bold': True, 'italic': False, 'underline': False
            })
        elif m.group(4):  # *italic*
            segments.append({
                'text': m.group(4), 'color': None,
                'bold': False, 'italic': True, 'underline': False
            })
        elif m.group(5):  # plain text
            segments.append({
                'text': m.group(5), 'color': None,
                'bold': False, 'italic': False, 'underline': False
            })
        elif m.group(6):  # fallback single char
            segments.append({
                'text': m.group(6), 'color': None,
                'bold': False, 'italic': False, 'underline': False
            })
    
    return segments


def _parse_bold_italic(text):
    """Parse **bold** and *italic* inside a color/underline tag."""
    segments = []
    pattern = re.compile(r'\*\*(.+?)\*\*|\*(.+?)\*|([^*]+)', re.DOTALL)
    for m in pattern.finditer(text):
        if m.group(1):
            segments.append({
                'text': m.group(1), 'color': None,
                'bold': True, 'italic': False, 'underline': False
            })
        elif m.group(2):
            segments.append({
                'text': m.group(2), 'color': None,
                'bold': False, 'italic': True, 'underline': False
            })
        elif m.group(3):
            segments.append({
                'text': m.group(3), 'color': None,
                'bold': False, 'italic': False, 'underline': False
            })
    return segments


def add_runs_to_paragraph(para, segments, default_color=COLOR_BLACK):
    """Add formatted runs to a paragraph from parsed segments."""
    for seg in segments:
        run = para.add_run(seg['text'])
        # Color: segment override > default
        color = seg.get('color') or default_color
        run.font.color.rgb = color
        if seg.get('bold'):
            run.bold = True
        if seg.get('italic'):
            run.italic = True
        if seg.get('underline'):
            run.underline = True


def convert_md_to_docx(md_path, docx_path):
    """Main conversion function."""
    doc = docx.Document()
    
    # === DOCUMENT SETUP (từ file mẫu) ===
    style = doc.styles['Normal']
    style.font.name = 'Times New Roman'
    style.font.size = Pt(14)
    
    for section in doc.sections:
        section.top_margin = Emu(720090)
        section.bottom_margin = Emu(720090)
        section.left_margin = Emu(720090)
        section.right_margin = Emu(720090)
    
    # === ĐỌC FILE MD ===
    with open(md_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    i = 0
    while i < len(lines):
        line = lines[i].rstrip('\n')
        
        # Skip dòng trống
        if not line.strip():
            i += 1
            continue
        
        # === DIVIDER: --- ===
        if line.strip() == '---':
            p = doc.add_paragraph()
            p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
            run = p.add_run(DIVIDER_CHAR)
            run.font.color.rgb = COLOR_DIVIDER
            i += 1
            continue
        
        # === HEADING ## ===
        if line.startswith('## '):
            heading_text = line[3:].strip()
            p = doc.add_paragraph()
            run = p.add_run(heading_text)
            # Section heading: text thường, không style Heading
            i += 1
            continue
        
        # === TIÊU ĐỀ # (A/B) ===
        if line.startswith('# '):
            title_text = line[2:].strip()
            p = doc.add_paragraph()
            run = p.add_run(title_text)
            i += 1
            continue
        
        # === BLOCKQUOTE > ===
        if line.startswith('> '):
            bq_text = line[2:].strip()
            # Strip markdown bold/italic markers for clean display
            p = doc.add_paragraph()
            segments = parse_inline(bq_text)
            add_runs_to_paragraph(p, segments)
            i += 1
            continue
        
        # === PARAGRAPHS THƯỜNG ===
        p = doc.add_paragraph()
        segments = parse_inline(line)
        add_runs_to_paragraph(p, segments)
        
        i += 1
    
    # === LƯU ===
    doc.save(docx_path)
    print(f'[OK] Saved: {docx_path}')


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python md_to_docx_v2.py <input.md> <output.docx>')
        sys.exit(1)
    convert_md_to_docx(sys.argv[1], sys.argv[2])
