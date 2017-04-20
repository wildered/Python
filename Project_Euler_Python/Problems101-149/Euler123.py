# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 13:58:12 2017

@author: Home
"""

#Using logarithmic density of primes we can estimate that at N = 300 000
#The remainder exceeds 10^9. The remainder for any prime is 2*n*p_n, which
#is almost always smallar than p_n^2. Found using a binary search.
#time: 15ms

from eulerTools import sieve_for_primes_to
from datetime import datetime
from timeit import default_timer as timer


def binSearch(arr, a, b, target):
    if a == b:
        return a
    
    mid = (a + b)//2
    val = 2 * (2*mid+1) * arr[mid]
    if target <= val:
        return binSearch(arr, a, mid, target)
    else:
        return binSearch(arr, mid + 1, b, target)


startTime = datetime.now()
start = timer()
max_prime = 300000
primes = sieve_for_primes_to(max_prime)
sprimes = [primes[idx] for idx in range(0, len(primes), 2)]
resIdx = binSearch(sprimes, 0, len(sprimes), 10**10)

print("Result =", 2*resIdx + 1)
print (datetime.now() - startTime)
print((timer()-start)*1000)
#time: 15ms

