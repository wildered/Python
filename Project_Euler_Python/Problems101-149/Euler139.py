# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 18:24:11 2017

@author: Home
"""

from math import gcd, sqrt
from datetime import datetime
from timeit import default_timer as timer


startTime = datetime.now()
start = timer()
res = 0
high = 10**8 - 1

def function(n, m):
    temp_res = 0
    a = m*m - n*n
    d = abs(a - 2*m*n)
    if (a*a)%d == 0:
        L = 2*(m + n)*m
        temp_res += high//L
    return temp_res

for m in range(2, 10**4//2 + 1, 2):
    #m even
    for n in range(1, m, 2):
        if gcd(n, m) != 1:
            continue
        res += function(n, m)


for m in range(3, 10**4//2 + 1, 2):
    #m odd
    for n in range(2, m, 2):
        if gcd(n, m) != 1:
            continue
        res += function(n, m)

for m in range(10**4//2, int(10**4/sqrt(2)), 2):
    #m even
    for n in range(1, m, 2):
        if 2*m*(m+n) > high:
            break
        if gcd(n, m) != 1:
            continue
        res += function(n, m)

for m in range(10**4//2 + 1, int(10**4/sqrt(2)), 2):
    #m odd
    for n in range(2, m, 2):
        if 2*m*(m+n) > high:
            break
        if gcd(n, m) != 1:
            continue
        res += function(n, m)
    
    
print(res)

print(datetime.now() - startTime)
print((timer()-start)*1000)
#time: 6.5s
