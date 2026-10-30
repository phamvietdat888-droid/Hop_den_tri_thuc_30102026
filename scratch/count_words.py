with open(r'outputs\2026-09-26_Thu_Hoi_Dat_Song_Bang_Gi_Cu_Dau\06_kich_ban_hoan_thien.md', encoding='utf-8') as f:
    text = f.read()

words = text.split()
print("Total word count:", len(words))
sections = text.split("## ")
for i, s in enumerate(sections):
    print(f"Sec {i}: {len(s.split())} words")
