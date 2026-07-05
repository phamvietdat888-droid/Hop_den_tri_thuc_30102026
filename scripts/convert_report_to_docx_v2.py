import sys
import os
import re
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

def set_cell_border(cell, **kwargs):
    """
    Set cell border
    Usage: set_cell_border(cell, top={"sz": 12, "val": "single", "color": "#000000"}, ...)
    """
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    for side in ('top', 'start', 'bottom', 'end'):
        if side in kwargs:
            tag = 'w:{}'.format(side)
            element = tcPr.find(qn(tag))
            if element is not None:
                tcPr.remove(element)
            element = OxmlElement(tag)
            for attr, val in kwargs[side].items():
                element.set(qn('w:{}'.format(attr)), str(val))
            tcPr.append(element)

def convert_report_to_docx(md_path, docx_path):
    if not os.path.exists(md_path):
        print(f"Error: {md_path} not found")
        return

    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    doc = Document()
    
    # Global settings
    style = doc.styles['Normal']
    style.font.name = 'Times New Roman'
    style.font.size = Pt(12)
    
    # Split content by lines
    lines = content.split('\n')
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        if not line:
            i += 1
            continue
            
        # Divider
        if line == '---':
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            run = p.add_run('────────────────────────')
            run.font.color.rgb = RGBColor(200, 200, 200)
            i += 1
            continue
            
        # Headers
        if line.startswith('# '):
            h = doc.add_heading(line[2:], 0)
            h.alignment = WD_ALIGN_PARAGRAPH.CENTER
            i += 1
            continue
        elif line.startswith('## '):
            doc.add_heading(line[3:], 1)
            i += 1
            continue
        elif line.startswith('### '):
            doc.add_heading(line[4:], 2)
            i += 1
            continue
            
        # Blockquote
        if line.startswith('> '):
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Cm(1)
            text = line[2:]
            # Parse bolding
            parts = re.split(r'(\*\*.*?\*\*)', text)
            for part in parts:
                if part.startswith('**') and part.endswith('**'):
                    run = p.add_run(part[2:-2])
                    run.bold = True
                else:
                    run = p.add_run(part)
            run.italic = True
            run.font.color.rgb = RGBColor(100, 100, 100)
            i += 1
            continue
            
        # Table
        if line.startswith('|') and i + 1 < len(lines) and lines[i+1].strip().startswith('|---'):
            # Detect table rows
            table_lines = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                if not lines[i].strip().startswith('|---'): # Skip separator line
                    table_lines.append(lines[i].strip())
                i += 1
            
            if table_lines:
                # Create table
                rows = [ [cell.strip() for cell in row.split('|') if cell.strip() or row.count('|') > 1] for row in table_lines ]
                # Filter out empty strings at start/end if they exist
                # (Markdown tables usually start and end with |)
                
                table = doc.add_table(rows=len(rows), cols=len(rows[0]))
                table.style = 'Table Grid'
                
                for r_idx, row_data in enumerate(rows):
                    for c_idx, cell_data in enumerate(row_data):
                        if c_idx < len(table.rows[r_idx].cells):
                            cell = table.rows[r_idx].cells[c_idx]
                            # Handle bolding in cell
                            p = cell.paragraphs[0]
                            parts = re.split(r'(\*\*.*?\*\*)', cell_data)
                            for part in parts:
                                if part.startswith('**') and part.endswith('**'):
                                    run = p.add_run(part[2:-2])
                                    run.bold = True
                                else:
                                    run = p.add_run(part)
                            if r_idx == 0:
                                for run in p.runs:
                                    run.bold = True
            continue

        # Lists
        if line.startswith('- ') or line.startswith('* '):
            p = doc.add_paragraph(style='List Bullet')
            text = line[2:]
            parts = re.split(r'(\*\*.*?\*\*)', text)
            for part in parts:
                if part.startswith('**') and part.endswith('**'):
                    run = p.add_run(part[2:-2])
                    run.bold = True
                else:
                    run = p.add_run(part)
            i += 1
            continue
            
        # Code block
        if line.startswith('```'):
            code_lines = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith('```'):
                code_lines.append(lines[i])
                i += 1
            if code_lines:
                p = doc.add_paragraph()
                p.paragraph_format.left_indent = Cm(0.5)
                run = p.add_run('\n'.join(code_lines))
                run.font.name = 'Courier New'
                run.font.size = Pt(10)
            i += 1
            continue

        # Normal Paragraph
        p = doc.add_paragraph()
        parts = re.split(r'(\*\*.*?\*\*)', line)
        for part in parts:
            if part.startswith('**') and part.endswith('**'):
                run = p.add_run(part[2:-2])
                run.bold = True
            else:
                run = p.add_run(part)
        i += 1

    doc.save(docx_path)
    print(f"Successfully created {docx_path}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python convert_report_to_docx.py <input_md> <output_docx>")
        sys.exit(1)
    
    convert_report_to_docx(sys.argv[1], sys.argv[2])
