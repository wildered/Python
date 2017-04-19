# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 13:20:01 2016

@author: Home
"""

#Recursive function counting the chance of winning
#Note that having 8 blue discs implies a certain win, and 8 red a loss.
#Time: 20ms

from math import gcd
from datetime import datetime


def func(blue, red, depth, disks, chance_a, chance_b):
    if blue >= 8:
        return chance_a, chance_b
    if depth == 0 or red >= 8:
        return (0, 1)
    a, b = chance_a, chance_b
    #grab blue
    a1, b1 = func(blue+1, red, depth-1, disks+1, a, disks*b)
    #grab red
    a2, b2 = func(blue, red+1, depth-1, disks+1, (disks-1)*a, disks*b)
    r1, r2 = a1*b2+a2*b1, b1*b2
    p = gcd(r1, r2)
    return (r1//p, r2//p)
    
    
startTime = datetime.now()
current = (0, 0)
a,b = func(0, 0, 15, 2, 1, 1)
print ("chance = " + str(a) + " / " + str(b))
print ("money = " + str(b//a))
    
print(datetime.now() - startTime)
#Time: 20ms

