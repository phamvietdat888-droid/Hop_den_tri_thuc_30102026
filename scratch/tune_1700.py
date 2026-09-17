# -*- coding: utf-8 -*-
import sys, os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.abspath('scratch'))
import count_words as c

total_text = f"{c.hook1}\n\n{c.bridge}\n\n{c.scene_shift}\n\n{c.part0_context}\n\n{c.part1_tang1}\n\n{c.part2_tang2}\n\n{c.part3_tang3}\n\n{c.conclusion}"

words = total_text.split()
print("Current total:", len(words))
print("Excess words to trim:", len(words) - 1700)
