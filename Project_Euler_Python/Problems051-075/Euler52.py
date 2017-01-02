# -*- coding: utf-8 -*-
from datetime import datetime
startTime = datetime.now()
import copy

l = 6
n = 0
c = 1
k = pow(10,c)/6
while True:
    n += 1
    if n > k:
        c += 1
        k = pow(10, c)/6
        n = 10**(c-1)
        
    dicArr = []
    flag = True
    for i in xrange(l):
        cDic = {}
        for char in str((i+1)*n):
            cDic[char] = 0
        for char in str((i+1)*n):
            cDic[char] += 1
        if i == 0:
            oldDic = cDic
            continue
        if cDic != oldDic:
            flag = False
            break
        oldDic = cDic
        
    if flag:
        print "The number is: " + str(n)
        break

print "Time: ",
print datetime.now() - startTime
#time = 0.36s

