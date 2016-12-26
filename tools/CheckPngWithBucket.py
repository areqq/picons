#!/usr/bin/python
import os, os.path, sys
import re, unicodedata

if len(sys.argv) < 3:
    print " usage:  ./CheckBucketwithpng.py /home/areq/pikony/E2_HD_HB_2015-12-01/userbouquet.dbe00.tv dir_with_picons"

RC = {}
for l in open('../ref2channels.txt'):
    l = l.strip()
    if [0] != '#':
        ref, pic = l.split(None, 2)
        RC[ref] = pic

b = sys.argv[1]
picons = sys.argv[2]

R = set()
  
for l in open(b):
    l = l.replace('\r','').strip().upper()
    if l.startswith('#SERVICE 1:0'):
	r = '_'.join( l.split()[1].split(':')[0:7] )
	if RC.has_key(r):
	    if not os.path.exists( picons + '/' + RC[r] + '.png'):
		print "png not fonud", RC[r], r
	else:
	    print "not found", r, "in ref2channels.txt"

if 0:
    add_to_ref = []
    for r in R:
        if not RC.has_key(r):
            n = N.get('_'.join( r.split('_')[3:7] ), [ None])[0]
            if n in ch:
                add_to_ref.append( r + ' ' + n)
            else:
                print "new channel? :", r, n

    if len(add_to_ref) > 0:
        print "Do dodania do ref2channels.txt:"
        for a in add_to_ref:
            print a

    q = open("new-ref2channels.txt","w")
    for r in sorted(RC):
        if not r[6:] in N:
            print r, RC[r], "outdated ?"
        else:
            q.write(r + " " + RC[r] +"\n")
