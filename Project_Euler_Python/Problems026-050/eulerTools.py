# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 19:08:41 2016

@author: Home
"""


import math
from fractions import gcd

#def gcd IMPORTED


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

def isPrime(k):
    if k == 2 or k == 3:
        return True
    if k%2 == 0 or k == 1:
        return False
    else:
        for i in range(2, int(math.ceil(math.sqrt(k))+1)):
            if i == k:
                break
            if k%i == 0:
                return False
        return True

def primeFactor(n):
    if n == 1:
        return [1]
    if n == 2:
        return [2]
    if isPrime(n):
        return [n]
    else:
        res = []
        for i in range(2, int(math.sqrt(n))+1):
            if n%i == 0:
                break
        div = i
        other = n/div
#        for factor in primeFactor(div):
#            res.append(factor)
#        for factor2 in primeFactor(other):
#            res.append(factor2)
        for factor in primeFactor(div):
#            if factor not in res:
            if True:
                res.append(factor)
        for factor2 in primeFactor(other):
#            if factor2 not in res:
            if True:
                res.append(factor2)
        return res


def fact(k):
    if k == 0:
        return 1
    res = 1
    for i in range(1, k+1):
        res *= i
    return res
    
def nChoosek(n, k):
    return fact(n)/fact(k)/fact(n-k)


def palindromeCheck(word):
    if type(word) != str:
        word = str(word)
    return word == word[::-1]

