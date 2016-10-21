# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 18:21:40 2016

@author: Home
"""

from datetime import datetime
startTime = datetime.now()

from math import *

def isPrime(n):
    #for large n no special rules required
    for k in range(2, int(sqrt(n))+2):
        if n%k == 0:
            return False
    return True
        
plist = []
for i in range(1001, 10000, 2):
    if isPrime(i):
        plist.append(i)
        
for idx in range(len(plist)):
    bdx = idx+1
    p1 = plist[idx]
    if p1 == 1487:
        continue
    while bdx < len(plist):
        p2 = plist[bdx]
        diff = p2 - p1
        p3 = p2 + diff
        charArray= []
        for p in [p1, p2, p3]:
            charSet = set()
            for c in str(p):
                charSet.add(c)
            charArray.append(charSet)
        if charArray[0] == charArray[1] and charArray[1] == charArray[2]:
            if p3 in plist:
                print "Sequence is: " + "\n" + str(p1) + " ,  " + str(p2) + " , " + str(p3)
                print "Concatenation: " + str(p1) + str(p2) + str(p3)
                break
                
        bdx += 1
        
print datetime.now() - startTime
#time 3s
