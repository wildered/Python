# -*- coding: utf-8 -*-
"""
Created on Wed Nov 02 23:18:28 2016

@author: Home
"""

from eulerTools import sieve_for_primes_to
from datetime import datetime
startTime = datetime.now()
reach= 12000

hoog = reach+1
primes = sieve_for_primes_to(hoog)
mod3 = [p%3 for p in primes]
m = len(primes)
res = [0]
    
def calc(n):
    return (-2-(-2)**(n+1))/3

def func(val, currPhi, idx, mod3_count):
    if val*primes[idx] >= hoog:
        return
    if idx >= m:
        return
    for walk in range(idx, m):
        p = primes[walk]
        new_val = val*p

        if new_val >= hoog:
            return
        new_mod3_count = mod3_count 
        if val%(p) == 0:
            new_phi = currPhi*p
        else:
            new_phi = currPhi*(p-1)
            new_mod3_count += (mod3[walk] == 2)
        
        a = new_phi%3
        if a == 0:
            temp = new_phi/2 - new_phi/3
        else:
            temp = new_phi/2
            ground = new_phi/3 + (a == 2)
            ground -= (-1)**(a == 2)*calc(new_mod3_count-1)/2
            temp -= ground
            
        res[0] += temp
        func(new_val, new_phi, walk, new_mod3_count)

func(1,1,0,0)
        
print "results = " + str(res[0])
print datetime.now() - startTime
#time 25ms

