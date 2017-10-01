# -*- coding: utf-8 -*-
"""
Created on Sat May 20 17:02:59 2017

@author: Home
"""

from eulerTools import sieve_for_primes_to
from datetime import datetime

startTime = datetime.now()
high = int(1e6)

primes = sieve_for_primes_to(high)

dtriangle_set = set()
dtriangle_set.add(2)
max_n = 1
max_dtriangle = 2

def isDTriangle(n):
    global max_dtriangle, max_n
    if max_dtriangle < n:
        while max_dtriangle < n:
            max_n += 1
            max_dtriangle = max_n * (max_n + 1)
            dtriangle_set.add(max_dtriangle)
    return n in dtriangle_set

counter = 0

for p in primes:
    if (p-1)%3 == 0:
        if isDTriangle((p-1)/3):
            counter += 1

print("Result = " + str(counter))
print(datetime.now() - startTime)
#time: 90ms
