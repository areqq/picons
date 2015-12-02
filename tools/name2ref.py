#!/usr/bin/python
import os, os.path
import hashlib

def dub(c1, c2):

    p1 = set()
    m1 = {}
    for f in os.listdir(c1):
        if f.endswith('.png'):
    	    p = c1 + '/' + f
    	    m = hashlib.md5(open(p).read()).hexdigest()
            p1.add(p)
            m1[m] = f

    p2 = set()
    m2 = {}
    for f in os.listdir(c2):
        if f.endswith('.png'):
    	    p = c2 + '/' + f
            m = hashlib.md5(open(p).read()).hexdigest()
            if m1.has_key(m):
        	print f[:-4], m1[m][:-4]

dub('wynik/out', 'picon_220x132')
