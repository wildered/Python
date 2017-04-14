# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 16:08:02 2017

@author: Home
"""

#See problem 129

from math import gcd
from eulerTools import primeFactor, eulerPhi, sieve_for_primes_to
from datetime import datetime

primes = set(sieve_for_primes_to(int(1e6)))

idx = 0
def order_of_10(n):
    nt = eulerPhi(n)
    primes = set(primeFactor(nt))
    order_10_m = nt
    for p in primes:
        while order_10_m%p == 0 and pow(10, order_10_m, n) == 1:
            order_10_m //= p
        if pow(10, order_10_m, n) != 1:
            order_10_m *= p
    return order_10_m


startTime = datetime.now()
n = 90
idx = 0
resSum = 0
while idx < 25:
    if gcd(n, 10) != 1 or n in primes:
        n += 1
        continue
    if (n-1)%order_of_10(9*n) == 0:
        resSum += n
        idx += 1
    n += 1

print("Result =",  resSum)
print(datetime.now() - startTime)

