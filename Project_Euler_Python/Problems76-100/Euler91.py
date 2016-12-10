# -*- coding: utf-8 -*-
"""
Created on Fri Dec 09 23:58:09 2016

@author: Home
"""

from fractions import gcd

from datetime import datetime
startTime = datetime.now()
#print datetime.now() - startTime


xm, ym = 50, 50
m = 50

def corner_calc_vierkant(m):
    """Calculates the amount of triangles with its right corner
    in the left bottom"""
#    return 2*sum([m+1-k for k in range(1, m+1)])-m
#    return 2*m**2 + m - (m*(m+1))
    return m**2


def other_calc(x, y, m):
    """calculates the amount of triangles given a second point outside
    of the origin, in the lower half (thus below y = x). We assume that the right angle is at this point, 
    and calculate the amount of possible triangles, and multiply it
    by 2 because of the symmetry. If on the line x = y, only look 
    right downwards to prevent double counts. """
    c = gcd(x,y)
    vector = (y/c, -x/c)
    
    res = 0
#    xt, yt = x, y
#    xt += vector[0]
#    yt += vector[1]
#    while ((0 <= xt <= m) and (0 <= yt <= m)):
#        res += 1
#        xt += vector[0]
#        yt += vector[1]
    if vector[0] == 0:
        res += -y/vector[1]
    elif vector[1] == 0:
        res += (m-x)/vector[0]
    else:
        res += min(-y/vector[1], (m-x)/vector[0])
    if x != y:
        vector = (-vector[0], -vector[1])
        if vector[0] == 0:
            res += (m-y)/vector[1]
        elif vector[1] == 0:
            res += -x/vector[0]
        else:
            res += min((m-y)/vector[1], -x/vector[0])
#        xt, yt = x, y
#        xt += vector[0]
#        yt += vector[1]
#        while ((0 <= xt <= m) and (0 <= yt <= m)):
#            res += 1
#            xt += vector[0]
#            yt += vector[1]
            
    return 2*res
    
ans = corner_calc_vierkant(m)

for x in range(1, m+1):
    for y in range(0, x+1):
        ans += other_calc(x, y, m)
        
print "Triangle count = " + str(ans)
print datetime.now() - startTime



