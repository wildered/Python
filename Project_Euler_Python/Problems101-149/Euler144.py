# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 15:26:41 2017

@author: Home
"""

from datetime import datetime
from timeit import default_timer as timer

from decimal import Decimal

startTime = datetime.now()
start = timer()

a, b = Decimal(0), Decimal(10.1)
x, y = Decimal(1.4), Decimal(-9.6)


#a, b = 0, 10.1
#x, y = 1.4, -9.6
res = 0

while not (-0.01 <= x <= 0.01 and y > 0):
    alpha = (-20*x*x + 100) * (x-a) - 8*x*y*(y-b)
    beta = (20*x*x - 100) * (y-b) - 8*x*y*(x-a)
    t = (-8*x*alpha - 2*y*beta)/(4*alpha*alpha + beta*beta)
    a, b = x, y
    x, y = x + t*alpha, y + t*beta
    #print(x, y)
    res += 1

print("Result =", res)
print(datetime.now() - startTime)
print((timer()-start)*1000)
#time: 20ms
