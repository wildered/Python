# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 21:27:24 2017

@author: Home
"""

from eulerTools import primeFactor, sieve_for_primes_to
from math import sqrt
from datetime import datetime
from collections import OrderedDict


def func(n):
    k = 1
    res = 0
    while k*k <= 3*n:
        if n%k == 0:
            other = n // k
            if (k + other)%4 == 0:
                d = (k + other) // 4
                x = other - d
                if x > 0:
                    res += 1
#                    print(x, x+d, x+d+d, -x**2 - (x+d)**2 + (x+2*d)**2)
                    if res > 10:
                        return 11
        k += 1
    return res

startTime = datetime.now()

high = 1000000

done_list = [0 for z in range(high)]
p_list = sieve_for_primes_to(high)


#single product
idx = 0
max_idx = len(p_list)
while idx < max_idx:
    p1 = p_list[idx]
    done_list[p1] = 1
    idx += 1

#double product
idx = 0
while idx < max_idx:
    bdx = idx
    p1 = p_list[idx]
    while bdx < max_idx:
        p2 = p_list[bdx]
        new_n = p1 * p2
        if new_n >= high:
            break
        done_list[new_n] = 1
        bdx += 1
    idx += 1
    if p1*p1 >= high:
        break
        
#triple product
idx = 0
while idx < max_idx:
    bdx = idx
    p1 = p_list[idx]
    while bdx < max_idx:
        p2 = p_list[bdx]
        cdx = 0
        while cdx < max_idx:
            p3 = p_list[cdx]
            new_n = p1 * p2 * p3
            if new_n >= high:
                break
            done_list[new_n] = 1
            cdx += 1
        if p1*p2*p2 >= high:
            break
        bdx += 1
    idx += 1
    if p1*p1*p1 >= high:
        break    


lst = []

res = 0
for m in range(high):
    if done_list[m] == 1:
        continue
    if func(m) == 10:
        res += 1

#        lst.append(len(primeFactor(m)))
##        l = primeFactor(m)
#        temp_d = {z: l.count(z) for z in l}
#        s = "{"
#        for key in sorted(temp_d):
#            s += str(key) + ": " + str(temp_d[key]) + ", "
#        print(m,  s + "}")
       
print("Result =", res)
print(datetime.now() - startTime)
#time: long
