import re

with open(r'outputs\2026-09-26_Dai_Dung_World_Cup_Cu_Dau\06_kich_ban_hoan_thien.md', 'r', encoding='utf-8') as f:
    text = f.read()

words = re.findall(r'\b\S+\b', text)
print(f"Word count: {len(words)}")
