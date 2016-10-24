# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 13:52:29 2016

@author: Home
"""

from datetime import datetime
startTime = datetime.now()
from math import sqrt
from eulerTools import gcd

def firstStep(number):
    return int(sqrt(number)), 0, 1, int(number), -int(sqrt(number))

def nextNums(sqrt1, int1, sqrt2, int2):
    if sqrt1 == 0:
        a = int(float(int1)/(sqrt(sqrt2)+int2))
        intres2 = int(sqrt2-int2**2)
        sqrtres1 = int1**2*sqrt2
        sqrtres2 = 0
        intres1 = -int2*int1-a*intres2
        #invert it again
        temp = gcd(int1, intres2)
        intres2 /= temp
        sqrtres1 /= temp**2
        intres1 /= temp
        
        return a, sqrtres2, intres2, sqrtres1, intres1 
        
    return a, sqrtres1, intres1, sqrtres2, intres2 
    
def pattern(number):
    p, p1, p2, p3, p4 = firstStep(number)
    
    res = []
    res.append([p, p1, p2, p3, p4])
    out = []
    out.append(p)
    
    while True:
        p, p1, p2, p3, p4 = nextNums(p1, p2, p3, p4)
        if [p, p1, p2, p3, p4] in res:
            idx = res.index([p, p1, p2, p3, p4])
            return out, len(res[idx:])
            
        res.append([p, p1, p2, p3, p4])
        out.append(p)
    return res

counter = 0
for i in range(1, 10000+1):
    if int(sqrt(i))**2 == i:
        continue
    temp, period = pattern(i)
    if period%2 == 1:
        counter += 1
        
print "aantal odd = " + str(counter)
print datetime.now() - startTime
#time 1.1s        
    
