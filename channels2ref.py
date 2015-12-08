#!/usr/bin/python
import os, os.path
import shutil
import re
import time

R = {}
for l in open('ref2channels.txt'):
    l = l.strip()
    if [0] != '#':
        ref, pic = l.split(None, 2)
        R[ref] = pic

for p in [ 'picon/100x60/gos_marcin', 'picon/220x132/gos_marcin', 'picon/220x132/zet71_transparent_ciemne_tlo_32bit' ]:
    out = 'out/' + p.replace('/','_')
    if os.path.exists(out):
        os.rename(out, out + '.old.' + str(time.time()))
    print "Create picons set:", out 
    os.mkdir(out) 

    for r in R:
        png = R[r] + '.png'
        spng = p + '/' + png
        dpng = out + '/' + png
        if os.path.exists(spng):
            if not os.path.exists(dpng):
                shutil.copy(spng, dpng)
            os.symlink( png, out + '/' + r + '_0_0_0.png')
        else:
            print "error not found:", spng, "needed by ", r
