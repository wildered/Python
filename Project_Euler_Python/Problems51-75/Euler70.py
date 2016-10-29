# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 12:07:53 2016

@author: Home
"""

from datetime import datetime
startTime = datetime.now()

from eulerTools import sieve_for_primes_to

def checkPerm(n1, n2):
    if len(str(n1)) != len(str(n2)):
        return False
    
    d1 = {}
    for c in str(n1):
        d1[c] = 0
    for c in str(n1):
        d1[c] += 1
    d2 = {}
    for c in str(n2):
        d2[c] = 0
    for c in str(n2):
        d2[c] += 1
    
    return d1 == d2

hoog = int((pow(10, 7)))
primes = sieve_for_primes_to(hoog/10) #under assumption that it have no prime-factors 
                                      #below 10, which whould increate the quotient significantly
m = len(primes)

min_n = float("inf")
min_phi = 1
k = len(primes)

#Solution cannot be prime as phi(p) = p-1 for p prime, thus not a permutation
for idx in range(k-1):
    if (primes[idx]*primes[idx+1]) > hoog:
        continue
    if (primes[idx]*min_phi) > min_n*(primes[idx]-1):
        break
    for bdx in range(idx+1, k):
        new_n = primes[idx]*primes[bdx]
        if new_n > hoog:
            break
        new_phi = (primes[idx]-1)*(primes[bdx]-1)
        if new_n*min_phi < min_n*new_phi:
            if checkPerm(new_n, new_phi):
                min_n = new_n
                min_phi = new_phi

print "result = " + str(min_n)

print datetime.now() - startTime
#time 8s
