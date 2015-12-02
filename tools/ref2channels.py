#!/usr/bin/python
import os

R = {}
for l in open('ref2channels.txt'):
    l = l.strip()
    if [0] != '#':
        ref, pic = l.split(None, 2)
        R[ref] = pic

d = '/home/areq/pikony/picon_100x60/'

for f in os.listdir(d):
    if f.startswith('1_0') and f.endswith('.png'):
        r = f[:-10]
        if R.has_key(r):
                print r, "->", R[r]
                os.rename(d + f, d + R[r] + '.png')
