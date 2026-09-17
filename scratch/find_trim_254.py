# -*- coding: utf-8 -*-
import sys, os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.abspath('scratch'))
import test_trim_270 as t

print("h:", len((t.hook1+' '+t.bridge+' '+t.scene_shift).split()))
print("p0:", len(t.p0.split()))
print("p1:", len(t.p1.split()))
print("p2:", len(t.p2.split()))
print("p3:", len(t.p3.split()))
print("p_conc:", len(t.p_conc.split()))
