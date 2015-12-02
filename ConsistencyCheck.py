#!/usr/bin/python
import os
import re

ch = []
i = 0
for l in open('channels.txt'):
    l = l.strip()
    i += 1
    if re.match('^[a-z0-9]+( #.+)?$',l):
        ch.append(l)
    elif l[0] != '#':
        print "channels.txt wrong line nr:", i," :", l

ch_dubel = set([x for x in ch if ch.count(x) > 1])
if ch_dubel:
    print "channels.txt doubled:", ch_dubel
ch = set(ch)

i = 0
R = {}
for l in open('ref2channels.txt'):
    l = l.strip()
    i += 1
    if re.match('^([A-F0-9]+_){6}[A-F0-9]+ [a-z0-9]+( #.+)?$',l):
        ref, pic = l.split(None, 2)
        if not pic in ch:
            print "ref2channels.txt line nr:", i," unknown channel", pic
        else:
    	    R[ref] = pic
    elif l[0] != '#':
        print "ref2channels.txt wrong line nr:", i," :", l

lackofref = ch - set(R.values())
if lackofref:
    print "No reference for channels:", lackofref

picons = {}
for root, dir, files in os.walk("picon"):
    if len(dir) == 0 and len(files) > 0:
	picons[root] = set()
        for f in files:
            if f[:-4] not in ch:
                print "picon set:", root, "unknown channel:", f[:-4]
        else:
    	    picons[root].add(f[:-4])

        lackof = ch - set([f[:-4] for f in files])
        if lackof:
            print "picon set:", root, "lack of:", lackof

