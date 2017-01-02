# -*- coding: utf-8 -*-

from datetime import datetime
startTime = datetime.now()
#print datetime.now() - startTime

#python modules...
from math import sqrt
from decimal import Decimal
from decimal import getcontext
getcontext().prec = 105

def digitSum(number):
    temp = int(sqrt(number))
    b = Decimal(number).sqrt()
    woord = str(b)
    return temp+sum([int(el) for el in woord[2:101]])
    for i in range(2,101):
        inc = int(woord[i])
        temp += inc
    return temp

arr = list(set(range(1,101)).difference([i*i for i in range(1,101)]))
res = sum(map(digitSum, arr))
    
print "result = " + str(res)

print datetime.now() - startTime
#time 10ms

