# -*- coding: utf-8 -*-
"""
Created on Tue Aug 02 12:01:37 2016

@author: Home
"""

from math import sqrt
from fractions import gcd

from datetime import datetime
q = datetime.now()

hoog = 1500000
hoog += 1

k = [0 for i in range(hoog)]

n = 1
while 2*n*n < hoog:
    m = n+2
    a = m*n
    while m*(m+n) < hoog:
        if m%3 == 0 and n%3 == 0:
            m += 2
            continue
        if m%5 == 0 and n%5 == 0:
            m += 2
            continue
        if gcd(n,m) != 1:
            m += 2
            continue
        b = (m*m-n*n)/2
        c = (m*m+n*n)/2
        i = 2
        L = m*(m+n)
        k[L] += 1
        for Li in xrange(2*L, hoog, L):
            k[Li] += 1
        m += 2
    n += 2

res = 0

for l in k:
    if l == 1:
        res += 1

print "result is: "+  str(res)
print datetime.now()-q
#time: 0.6s


