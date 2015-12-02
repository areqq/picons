#!/usr/bin/python
import os, os.path
import re, unicodedata

def parse_lamede( f = 'enigma2/lamedb' ):
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

def toname( e2dir = 'enigma2/', picond = 'picon_220x132', outd = 'out'):

    N = parse_lamede(e2dir + '/lamedb')
    P = set()
    for f in os.listdir(picond):
        if f.startswith('1_0_') and f.endswith('0_0_0.png'):
            P.add(f) 
  
    for b in [ 'bouquets.tv', 'bouquets.radio']:
        for p in open(e2dir + b):
            if p.startswith('#SERVICE'):
                p = p.replace(':0:user', ':0:"user').strip().split('"')[1]
                for l in open(e2dir + p ):
                    l = l.replace('\r','').strip().upper()
                    if l.startswith('#SERVICE 1:0'):
                        reff = '_'.join( l.split()[1].split(':')[3:7] )
                        if N.has_key(reff):
                            pn = '%s/%s.png' % (outd, N[reff][0])
                            if not os.path.exists(pn):
                                for prec in [7, 6]:
                                    ref = '_'.join( l.split()[1].split(':')[3:prec] )
                                    for pi in P:
                                        if pi.find(ref) > 0:
                                            break
                                    else:
                                        pi = ''
                                    if pi != '':
                                	print picond + '/' + pi, pn
                                        os.rename( picond + '/' + pi, pn)
                                        P.remove(pi)
                                        break
                                else:
                                    print "not found", reff, pn
                        else:
                            print "unknown name", reff
                                
    if 0:                     
                        try:
                            q = picond + '/' +  '_'.join(ref.split(':', 10)[:10])  + '.png'
                            pn = '%s/%s.png' % (outd, N[ref][0])
                            if os.path.exists(q):
                                #print ref, name, "ok"
                                os.rename(q, pn)
                            elif os.path.exists(q.replace('_13E_', '_71_')):
                                q = q.replace('_13E_', '_71_')
                                #print ref, name, "ok"
                                os.rename(q, pn)
                            elif not os.path.exists(pn):
                                print ref, N[ref][0], "brak", q
                        except:
                            print "not found"

toname()
