# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 20:08:16 2016

@author: Home
"""

#Sorting the numbers based on radicals for 1 <= n <= 100000
#Using a memoized recursive primefactorization.


from datetime import datetime
startTime = datetime.now()

from math import sqrt
from eulerTools import sieve_for_primes_to

primes = set(sieve_for_primes_to(100000))
primes.add(1)
mem_dic = {}
for p in primes:
    mem_dic[p] = {p}


def prod(arr):
    res = 1
    for el in arr:
        res *= el
    return res


def primeFactor(n):
    if n in mem_dic:
        return mem_dic[n]
    
    res = set()
    for i in range(2, int(sqrt(n))+1):
        if n%i == 0:
            break
    div = i
    other = n//div
    for factor in primeFactor(div):
        res.add(factor)
    for factor2 in primeFactor(other):
        res.add(factor2)
    mem_dic[n] = res
    return res


res = [[0]]
for i in range(1,100000+1):
    res.append([prod(primeFactor(i)), i])

res.sort()
print("E(10000) = " + str(res[10000][1]))
print(datetime.now() - startTime)
#time: 0.65s

