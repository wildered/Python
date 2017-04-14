# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 00:24:10 2017

@author: Home
"""

from math import gcd
from eulerTools import primeFactor, eulerPhi
from datetime import datetime

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
n = int(1e6)
while True:
    if gcd(n, 10) != 1:
        n += 1
        continue
    if order_of_10(9*n) > 1e6:
        break
    n += 1

print("Result =",  n)
print(datetime.now() - startTime)

