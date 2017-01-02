# -*- coding: utf-8 -*-

from eulerTools import primeFactor
from datetime import datetime
startTime = datetime.now()

def primePhi(p, k):
    return (p-1)*p**(k-1)

def eulerPhi(n):
    res = 1
    factors = primeFactor(n)
    cDic = {}
    for p in factors:
        cDic[p] = 0
    for p2 in factors:
        cDic[p2] += 1
    for prime in set(factors):
        res *= primePhi(prime, cDic[prime])
    return res



#res = 0
#for n in range(1, 10**6+1):
#    res += eulerPhi(n)

hoog = 10**6+1

from eulerTools import sieve_for_primes_to

from datetime import datetime
startTime = datetime.now()

primes = sieve_for_primes_to(hoog)
m = len(primes)

res = [0]
    
def func(val, currPhi, idx):
    if val*primes[idx] >= hoog:
        return
    if idx >= m:
        return
    
    for walk in range(idx, m):
        p = primes[walk]
        new_val = val*p

        if new_val >= hoog:
            return
        if val%(p) == 0:
            new_phi = currPhi*p
        else:
            new_phi = currPhi*(p-1)
        
        res[0] += new_phi
        
        func(new_val, new_phi, walk)

func(1,1,0)

print "result is: " + str(res[0])
print datetime.now() - startTime
#time 7s



