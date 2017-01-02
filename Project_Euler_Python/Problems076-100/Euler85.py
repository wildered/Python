# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 21:44:16 2016

@author: Home
"""

from math import sqrt

from datetime import datetime
startTime = datetime.now()
#print datetime.now() - startTime

def calc(n):
    """It is basic combinatorics that from n points we can choose
    n choose 2 = n*(n-1)/2 pairs of points. This is of use, as a 
    subrectangle is fully defined by the domain on both axes.
    [a,b] = [a_1, b_1] x [a_2, b_2], a, b in R^2, a_i, b_i in R.
    Also note that a side length of lengt k gives rise to 
    (k+1) choose 2 combinations of points by integer partitioning.
    """
    return n*(n-1)/2

k = 2000000.0           #float of value to avoid repeated casting
l = 2000000             #integer value to use

out = None              #unnecessary initialisation
klein = float('inf')    #necessary initialisation
idx = 2                 #starting length of longest side of rectangle
while True:         
    point = calc(idx+1) 
    a = k/point         #ideal amount of combinations on remainling length (+1)
    n = int(sqrt(2*a+0.25)+0.5) #closest guess to ideal side length (+1)
    if n < idx:         #assuming (wlog) idx is the longest side 
        break           #therefore stopping if not the case anylonger
    a, b, c = n-1, n, n+1   #in case of rounding problems
    
    for walk in [a,b,c]:
        if abs(l - point*calc(walk)) < klein:
            klein = abs(l - point*calc(walk))
            out = (idx)*(walk-1)  
    idx += 1            
    
print "Result = " + str(out)
print "min_dist = "+ str(klein)

print datetime.now() - startTime
#time: <1ms


