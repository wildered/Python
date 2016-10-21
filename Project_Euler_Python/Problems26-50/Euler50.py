# -*- coding: utf-8 -*-
from eulerTools import sieve_for_primes_to

from datetime import datetime
startTime = datetime.now()

primes = sieve_for_primes_to(1000000)

def primeFunc(lowest):
    currentP = lowest
    idx = primes.index(lowest)

    s = 0
    stored = 0
    l = 0
    storedL = 0
    while s < 1000000:
        stored = s
        storedL = l
        currentP = primes[idx+1]
        idx += 1
        s += currentP
        l += 1
    return [stored, storedL]

resP = 0
resL = 0

[resP, resL] = primeFunc(2)
last = 1000000

for i in primes:
    if last / i < resL:
        break
    [tempP, tempL] = primeFunc(i)
    if tempL >= resL:
        resL = tempL
        resP = tempP

[stored, storedL] = [resP, resL]
print "final: " + str(stored)
print "length : " + str(storedL)
    
print datetime.now() - startTime
#time 7ms

