# -*- coding: utf-8 -*-
from datetime import datetime
q = datetime.now()
from math import *

def isPrime(n):
    if n == 2 or n == 3:
        return True
    if n == 1 or n%2 == 0:
        return False
    for k in range(2, int(sqrt(n)) + 1):
        if n%k == 0:
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
        for i in range(2, int(sqrt(n))+1):
            if n%i == 0:
                break
        div = i
        other = n/div
#        for factor in primeFactor(div):
#            res.append(factor)
#        for factor2 in primeFactor(other):
#            res.append(factor2)
        for factor in primeFactor(div):
            if factor not in res:
                res.append(factor)
        for factor2 in primeFactor(other):
            if factor2 not in res:
                res.append(factor2)
        return res
        
    
c = 644
counter = 0
while True:
    c +=  1
    if len(primeFactor(c)) == 4:
        counter += 1
    else:
        counter = 0
    if counter == 4:
        print c - 3
        break
print datetime.now()-q           
#time: 2.5s
