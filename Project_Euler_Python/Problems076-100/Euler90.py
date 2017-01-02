# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 15:02:32 2016

@author: Home
"""

#it works

from datetime import datetime
startTime = datetime.now()
#print datetime.now() - startTime


def test(arr1, arr2):
    if (0 in arr1 and 1 in arr2) or \
    (1 in arr1 and 0 in arr2):
        if (0 in arr1 and 4 in arr2) or \
        (4 in arr1 and 0 in arr2):
            if (0 in arr1 and (6 in arr2 or 9 in arr2)) or \
            (0 in arr2 and (6 in arr1 or 9 in arr1)):
                if (1 in arr1 and (6 in arr2 or 9 in arr2)) or \
                (1 in arr2 and (6 in arr1 or 9 in arr1)):
                    if (2 in arr1 and 5 in arr2) or \
                    (5 in arr1 and 2 in arr2):
                        if (3 in arr1 and (6 in arr2 or 9 in arr2)) or \
                        (3 in arr2 and (6 in arr1 or 9 in arr1)):
                            if (4 in arr1 and (6 in arr2 or 9 in arr2)) or \
                            (4 in arr2 and (6 in arr1 or 9 in arr1)):
                                if (1 in arr1 and 8 in arr2) or \
                                (8 in arr1 and 1 in arr2):
                                    return True    
    
    return False

cube1 = []

for a in range(0, 4+1):
    for b in  range(a+1, 5+1):
        for c in range(b+1, 6+1):
            for d in range(c+1, 7+1):
                for f in range(d+1, 8+1):
                    for g in range(f+1, 9+1):
                        cube1.append([a,b,c,d,f,g])

res = 0

for a in cube1:
    for b in cube1:
        if a != b:
            if test(a,b):
                res += 1
    
print "unique count = " + str(res/2)
print datetime.now() - startTime
#time: 45ms



