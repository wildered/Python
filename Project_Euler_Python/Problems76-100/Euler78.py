# -*- coding: utf-8 -*-
"""
Created on Wed Nov 09 21:23:44 2016

@author: Home
"""

from datetime import datetime
startTime = datetime.now()

max_size = 1000000
max_n = 1000000

nArray = [0 for i in range(max_size+1)]
nArray[0] = 1
nArray[1] = 1

from math import sqrt
n = 2
while True:
    res = 0
    k = 1
    a = 1
    for k in xrange(1, int((1+sqrt(1+24*n))/6)+1, 2):
        a = n-k*(3*k-1)/2
        b = n-k*(3*k+1)/2
        res += nArray[a]
        res += nArray[b]
    if b < 0:
        res -= nArray[b]
    for k in xrange(2, int((1+sqrt(1+24*n))/6)+1, 2):
        a = n-k*(3*k-1)/2
        b = n-k*(3*k+1)/2
        res -= nArray[a]
        res -= nArray[b]
    if b < 0:
        res += nArray[b]
    nArray[n] = res%1000000
    if res%1000000 == 0:
        break

    n += 1

print "result = " + str(n)


print datetime.now() - startTime
#time: 5s
