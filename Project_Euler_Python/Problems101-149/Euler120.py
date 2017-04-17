# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 18:00:24 2017

@author: Home
"""

#use the binomial theorem + modular arithmetic  => answer
#n even can be skipped, n odd gives unique smallest n for maximal answer.
#time: 0.5ms
#Bonus: Sum can also be written as sum([2*k*(4*k+3) for k in range(1, 500)])
#which takes 9µs. Direct formula for the sum can also be found. 

from datetime import datetime
from timeit import default_timer as timer

startTime = datetime.now()
start = timer()

res = 0
for a in range(3, 1000+1):
    n = (a-1)//2
    res += 2*n*a

print("Result =", res)
print(datetime.now() - startTime)
print((timer()-start)*1000)
#time: 0.5ms

