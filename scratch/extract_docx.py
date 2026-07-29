import docx

doc = docx.Document(r"t:\CLAUDE\Hop_Den_Tri_Thuc\outputs\Sợ sai 2_SỬA.docx")
full_text = []
for p in doc.paragraphs:
    if p.text.strip():
        full_text.append(p.text.strip())

with open(r"t:\CLAUDE\Hop_Den_Tri_Thuc\scratch\script_text.txt", "w", encoding="utf-8") as f:
    f.write("\n\n".join(full_text))

print("Extracted successfully, total paragraphs:", len(full_text))
