# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 20:27:41 2017

@author: Home
"""

from eulerTools import sieve_for_primes_to, primeFactor_listset
from datetime import datetime
from math import sqrt


def ord10(p):
    n = 2
    p9 = 9*p
    target = 6*(p-1)
    divs = primeFactor_listset(target)
    for n in divs:
        if target%n == 0:
            while (target%n == 0) and (pow(10, target//n, p9) == 1):
                target //= n
        
    return target


startTime = datetime.now()
p_list = sieve_for_primes_to(100000)

res = sum(p_list[:3])
p_list = p_list[3:]
check_list = [[], [2], [5], [2, 5]]

for p in p_list:
    z = ord10(p)
    while z%2 == 0:
        z //= 2
    while z%5 == 0:
        z //= 5
    if z != 1:
        res += p

print("Result =", res)    
print(datetime.now() - startTime)
#time: 3.6s
