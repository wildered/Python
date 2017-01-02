# -*- coding: utf-8 -*-
"""
Created on Tue Aug 09 16:57:09 2016

@author: Home
"""

from math import sqrt

from datetime import datetime
startTime = datetime.now()

def sieve_for_primes_to(n):
    size = n//2
    sieve = [1]*size
    limit = int(n**0.5)
    for i in range(1,limit):
        if sieve[i]:
            val = 2*i+1
            tmp = ((size-1) - i)//val 
            sieve[i+val::val] = [0]*tmp
    return [2] + [i*2+1 for i, v in enumerate(sieve) if v and i>0]


primes = sieve_for_primes_to(int(sqrt(50e6)+1))

primes1 = sieve_for_primes_to(int(sqrt(50e6)+1))
primes2 = sieve_for_primes_to(int((50e6**(1.0/3))+1))
primes3 = sieve_for_primes_to(int((50e6**(1.0/4))+1))

primes1 = [el**2 for el in primes1]
primes2 = [el**3 for el in primes2]
primes3 = [el**4 for el in primes3]

fulldic = {}

for a in primes1:
    for b in primes2:
        if a + b > 50e6:
            break
        for c in primes3:
            res = a + b + c
            if res >= 50e6:
                break
            fulldic[a + b+ c] = 1

#for a in primes:
#    for b in primes:
#        if a**2 + b**3 > 50e6:
#            break
#        for c in primes:
#            res = a**2 + b**3 + c**4
#            if res >= 50e6:
#                break
#            fulldic[a**2 + b**3 + c**4] = 1
#            


print "result = " + str(len(fulldic))
print datetime.now() - startTime
#time 0.65s


