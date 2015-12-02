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
            m1[m] = p

    p2 = set()
    m2 = {}
    for f in os.listdir(c2):
        if f.endswith('.png'):
    	    p = c2 + '/' + f
            m = hashlib.md5(open(p).read()).hexdigest()
            if m1.has_key(m):
        	print p, "->", m1[m]
        	os.remove(p)
    	    else:
    		print p
  

dub('out', 'picon_220x132')
dub('out', 'picon_100x60')
