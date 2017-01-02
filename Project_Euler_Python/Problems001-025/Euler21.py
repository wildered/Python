# -*- coding: utf-8 -*-
from datetime import datetime
startTime = datetime.now()
from math import sqrt

def d(a):
    if a <= 0:
        return 0
    if a == 1:
        return 1   #special case
    res = 1 #1 is always a divisor
    i = 0
    for i in range(2,int(sqrt(a))):
        if a%i == 0:
            res += i + a/i
    i += 1
    if i**2 == a:
        res += i
    return res

tres = 0
for k in range(1,10000):
    temp = d(k)
    if k != temp and k == d(temp):
        tres += k

print tres                                                                                                

print datetime.now()-startTime

#Running time on creator system: 110ms















