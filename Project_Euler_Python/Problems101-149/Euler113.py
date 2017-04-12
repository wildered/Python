# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 16:49:22 2017

@author: Home
"""

#Using combinatorics we get all increasing numbers choosing with replacent
#from 0 to 10. This gives nChoosek(10 + digits - 1, digits) combinations.
#reversing these numbers give decreasing numbers, but only of that length,
#bar 0. The sum gives all non-bouncy numbers, where 0 is counted double and
#any number of the form xxxxx. 
#time: 0.4ms


from datetime import datetime
from eulerTools import nChoosek
from timeit import default_timer as timer


def count_incr(exp_10):
    return nChoosek(10 + exp_10 - 1, exp_10)


startTime = datetime.now()
start = timer()
decr = 0
for exp_10 in range(1, 100 + 1):
    incr = count_incr(exp_10)
    new_decr = decr + incr - 1                      #counting 0 double
    non_bouncy = incr + new_decr - 9*exp_10 -1      #0 and constant digit
    decr = new_decr

print("Result =", non_bouncy)
print(datetime.now() - startTime)
print((timer()-start)*1000)
#time: 0.4ms

