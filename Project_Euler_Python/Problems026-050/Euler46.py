# -*- coding: utf-8 -*-
from datetime import datetime
q = datetime.now()
from math import *

def isPrime(k):
    if k == 2 or k == 3:
        return True
    if k%2 == 0 or k == 1:
        return False
    else:
        for i in range(2, int(ceil(sqrt(k))+1)):
            if i == k:
                break
            if k%i == 0:
                return False
        return True
n = 1
king = False
volg = False
primeList = []

while king == False:
    n += 2
    if not isPrime(n):
        volgende = False
        for s in range(1,int(sqrt(n/2))+1):
            res = n - 2*s**2
            if isPrime(res):
                volgende = True
        if not volgende:
            print n
            king = True
            
                
print datetime.now()-q
#time: 0.3s
