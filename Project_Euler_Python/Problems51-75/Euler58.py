# -*- coding: utf-8 -*-
from eulerTools import isPrime
from datetime import datetime

startTime = datetime.now()
totalcount = 0
truecount = 0
length = 1
start = 1
totalcount += 1
increment = 2

while True:
    totalcount += 4
    length += 2
    for i in range(4):
        start += increment
        if i == 3:
            continue
        if isPrime(start):
            truecount += 1
    increment += 2
    if truecount / float(totalcount) < 0.1:
        break

print length    
print datetime.now() - startTime
#time 12s
    

