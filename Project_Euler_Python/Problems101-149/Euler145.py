# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 12:29:52 2017

@author: Home
"""

from datetime import datetime
from timeit import default_timer as timer

startTime = datetime.now()
start = timer()
startTime = datetime.now()
res = 0

high_exp = 9
for exponent in range(high_exp):
    digit_count = exponent + 1
    if digit_count%4 == 1:
        continue
    if digit_count%4 == 3:
        res += 20 * 5 * (20 * 25)**((digit_count-3)//4)
    else:
        res += 20*30**((digit_count - 2)//2)

print("Result =", res)  
print(datetime.now() - startTime)
print((timer()-start)*1000)
#time: 0.20ms
