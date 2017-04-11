# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 20:56:13 2016

@author: Home
"""

# First we look for a prime with the most repeating digits, and then count
# how many there are.


import copy
from eulerTools import isPrime
from math import factorial

from datetime import datetime
startTime = datetime.now()


d = 10
tenD = [10**i for i in range(d)]


def prod(arr):
    res = 0
    for i in range(1, len(arr)+1):
        res += arr[-i]*tenD[i-1]
    return res


def permute(arr, repeater, depth):
    if depth == 0:
        return [arr]
    res = []
    for idx in range(len(arr)):
        if arr[idx] != repeater:
            continue
        for k in range(9+1):
            if k == repeater:
                continue
            if idx == 0 and k == 0:
                continue
            temp = copy.deepcopy(arr)
            temp[idx] = k
            for nieuw in permute(temp, repeater, depth-1):
                res.append(nieuw)
    return res
    

def M(n, digit):
    hoeveel = 1
    array = n*[digit]
    while True:
        nrs = permute(array, digit, hoeveel)
        for nr in nrs:
            if nr[0] == 0:
                continue
            if isPrime(prod(nr)):
                return nrs, hoeveel
        hoeveel += 1
    
        
def count(arrs, depth):
    res = 0
    for arr in arrs:
        if arr[0] == 0:
            continue
        if isPrime(prod(arr)):
            res += prod(arr)
    return res//factorial(depth)


n = 10
resSum = 0
for repeat in range(9+1):
    arrs, diep = M(n ,repeat)
    resSum += count(arrs, diep)
    
print("result = " + str(resSum))
print(datetime.now() - startTime)


