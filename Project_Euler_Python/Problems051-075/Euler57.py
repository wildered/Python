# -*- coding: utf-8 -*-

import sys
sys.setrecursionlimit(10000)
from datetime import datetime
startTime = datetime.now()

def stap(n):
    if n == 0:
        return (1,2)
    a,b = stap(n-1)
    return (b, 2*b+a)
    
for i in range(8):
    a,b = stap(i)
#    print str(a+b) + " / " + str(b)

counter = 0
for i in range(1000):
    a, b = stap(i)
    if len(str(a+b)) > len(str(b)):
        counter += 1
        
print counter
print datetime.now() - startTime
#time 0.32s


