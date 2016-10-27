# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 21:25:40 2016

@author: Home
"""

#https://en.wikipedia.org/wiki/Pell%27s_equation#Fundamental_solution_via_continued_fractions

from datetime import datetime
startTime = datetime.now()
from math import sqrt
from eulerTools import gcd
squares = [i*i for i in range(40)]

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

def func(n):
    temp = pattern(n)
    c = temp[1]
    a0 = temp[0][0]
    arr = temp[0][1:]
    h0 = a0
    k0 = 1
    
    if h0*h0 - n*k0*k0 == 1:
        return h0, k0
    
    a1 = arr[0]
    h1 = a1*a0 + 1
    k1 = a1
    
    if h1*h1 - n*k1*k1 == 1:
        return h1, k1

    hn2 = h0
    kn2 = k0
    hn1 = h1
    kn1 = k1
    adx = 1
    
    while True:
        hn = arr[adx]*hn1+hn2
        kn = arr[adx]*kn1 + kn2
        if hn*hn - n*kn*kn == 1:
            return hn, kn
        adx = (adx+1)%c
        hn2, kn2 = hn1, kn1
        hn1, kn1 = hn, kn

        
max_D = 0
max_x = 0
for D in range(1,1000):
    if D in squares:
        continue
    temp_x = func(D)[0]
    if max_x < temp_x:
        max_x = temp_x
        max_D = D
print func(7)

print "Maximal minimal x = " + str(max_D)

        
print datetime.now() - startTime
#time 50ms        
    

