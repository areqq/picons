#!/usr/bin/python
import os, os.path, sys
import re, unicodedata

def parse_lamede(f):
    N = {}
    s = False
    k = 1
    for l in open(f):
        l = l.replace('\r', '').strip()
        if l == 'end':
            s = False
        elif l == 'services':
            s = True
        elif s:
            if k == 1:
                sid, namesp, tsid, nid, stype, number = [ hex(int(x,16))[2:] for x in l.split(':', 6) ]
                if stype not in ['1', '2', "16"]: # x16 = 22 - dvb-t
                    stype = '1'
            elif k == 2:
                r = ('_'.join([sid, tsid, nid, namesp ])).upper()
                name = unicodedata.normalize('NFKD', unicode(l, 'utf_8', errors='ignore')).encode('ASCII', 'ignore')
                name = re.sub('[^a-z0-9]', '', name.replace('&', 'and').replace('+', 'plus').replace('*', 'star').lower())
                N[r] = [name, l]
            else:
                k = 0
            k += 1
    return N

if len(sys.argv) < 2:
    print " usage:  ./CheckRefWithBucket.py /home/areq/pikony/E2_HD_HB_2015-12-01/userbouquet.dbe00.tv"

RC = {}
for l in open('../ref2channels.txt'):
    l = l.strip()
    if [0] != '#':
        ref, pic = l.split(None, 2)
        RC[ref] = pic
ch = set(RC.values())


for bouquets in sys.argv[1:]:
    e2dir = os.path.dirname(bouquets)
    N = parse_lamede(e2dir + '/lamedb')
    R = set()
  
    for b in [ bouquets ]:
        for l in open(b):
            l = l.replace('\r','').strip().upper()
            if l.startswith('#SERVICE 1:0'):
                R.add('_'.join( l.split()[1].split(':')[0:7] ))

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
