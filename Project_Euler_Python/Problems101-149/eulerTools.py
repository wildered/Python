# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 19:08:41 2016

@author: Home
"""

from math import factorial as fact
from math import ceil, sqrt
#from fractions import gcd

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

def isPrime(n):
    if n == 2:
        return True
    if n <= 1 or n%2 == 0:
        return False
    for i in range(3, int(ceil(sqrt(n))+1), 2):
        if n%i == 0:
            return False
    return True

def primeFactor(n):
    i = 2
    res = []
    while i*2 <= n:
        if n%i == 0:
            while n%i == 0:
                res.append(i)
                n //= i
        i += 1
    if n != 1:
        res.append(n)
    return res

def primeFactor_listset(n):
    i = 2
    res = []
    while i*2 <= n:
        if n%i == 0:
            res.append(i)
            while n%i == 0:
                n //= i
        i += 1
    if n != 1:
        res.append(n)
    return res

def eulerPhi(n):
    prime_set = primeFactor_listset(n)
    res = n
    for p in prime_set:
        res = res * (p-1) // p
    return res


def nChoosek(n, k):
    if n-k < k:
        k = n-k
    f = n
    res = 1
    for i in range(k):
        res *= f
        f -= 1
    return res//fact(k)

def palindromeCheck(word):
    if type(word) != str:
        word = str(word)
    return word == word[::-1]

