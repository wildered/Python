# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 15:47:15 2017

@author: Home
"""

from math import sqrt
from eulerTools import sieve_for_primes_to
from datetime import datetime
from timeit import default_timer as timer

startTime = datetime.now()
start = timer()
res = 0

primes = sieve_for_primes_to(150 * 10**6)
diffs = [2, 4, 2, 4, 14]

for idx in range(len(primes) - 5):
    flag = True
    for bdx in range(5):
        if primes[idx + bdx + 1] - primes[idx + bdx] != diffs[bdx]:
            flag = False
            break
    if flag:
        if sqrt(primes[idx] - 1) == int(sqrt(primes[idx] - 1)):
            res += int(sqrt(primes[idx] - 1))   
            
        
#10
#315410
#927070
    

print("Result =", res)
print(datetime.now() - startTime)
print((timer()-start)*1000)
