# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 15:35:38 2016

@author: Home
"""

from math import atan2, pi
from datetime import datetime
startTime = datetime.now()

triangles = []
f = open('p102_triangles.txt', 'r')

for placeholder in f:
    coords = placeholder.replace("\n", "").split(',')
    coords = map(int, coords)
    triangles.append(coords)
f.close()

def check_support(a0, b0, a1, b1, a2, b2):
    l0 = atan2(0-a0, 0-b0)%(2*pi)
    l1 = atan2(a1-a0, b1-b0)%(2*pi)
    l2 = atan2(a2-a0, b2-b0)%(2*pi)
    if l1 > l2:
        l1, l2 = l2, l1
    if l2 - l1 > pi:
        if not ((0 <= l0 <= l1) or (2*pi > l0 >= l2)):
            return False
    else:
        if not (l1 <= l0 <= l2):
            return False
    return True


def check(x0, y0, x1, y1, x2, y2):
    if not check_support(x0, y0, x1, y1, x2, y2):
        return False
    if not check_support(x1, y1, x0, y0, x2, y2):
        return False
    if not check_support(x2, y2, x1, y1, x0, y0):
        return False
    return True
     
    
resSum = 0
for comb in triangles:
    [x0, y0, x1, y1, x2, y2] = comb
    if check(x0, y0, x1, y1, x2, y2):
        resSum += 1

print "result = " + str(resSum)
print datetime.now() - startTime
#time: 7ms
