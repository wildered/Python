# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 22:46:41 2017

@author: Home
"""

from eulerTools import sieve_for_primes_to
from datetime import datetime


startTime = datetime.now()
high = 50000000
max_val = []

p_list = sieve_for_primes_to(high)
p_list = p_list[1:]

lst = []

res = 2         #[2, 2] and [2, 2, 2, 2]
for p in p_list:
    if (p + 1)%4 == 0:
        res += 1

idx = 0
while 4*p_list[idx] < high:     #could be optimized with binary search 
    idx += 1                    #but only small gain relative to total
res += idx

idx = 0
while 16*p_list[idx] < high:
    idx += 1
res += idx

print("Result =", res)
print(datetime.now() - startTime)
#time: 3.8s

