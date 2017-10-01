# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 22:48:27 2017

@author: Home
"""

from datetime import datetime
from timeit import default_timer as timer
from eulerTools import nChoosek


def square_calc(l, w):
    if l == 0 or w == 0:
        return 0
    return nChoosek(l+1, 2) * nChoosek(w+1, 2)


startTime = datetime.now()
start = timer()

square_arr = [0 for i in range(44)]
hard_square_arr = [0 for i in range(44)]

for idx in range(2, 44):
    count = 0
    length = 2*(idx - 1)
    width = 2
    while length > width:
        count += 2*nChoosek(length + 1, 2) * nChoosek(width + 1, 2)
        length -= 2
        width += 2
    if length == width:
        count += nChoosek(length + 1, 2)**2
    hard_square_arr[idx] = count
    count -= hard_square_arr[idx - 1]
    square_arr[idx] = count
        
res = 0

for a in range(43 + 1):
    res += square_arr[a]
    res += square_calc(a, a)
    base_count = 0
    for x in range(1, 2*a):
        for y in range(1, min(2*a + 1 - x, x)):
            side_sum = x + y
            base_count += 2 * (2*a + 1 - side_sum)
        if 2*x <= 2*a:
            base_count += 2*a + 1 - 2*x
            
    cum_count = square_arr[a] + base_count
    for b in range(a + 1, 43 + 1):
        res += 2*cum_count
        res += 2*square_calc(a, b)
        cum_count += base_count
    for b in range(44, 47 + 1):
        res += cum_count
        res += square_calc(a, b)
        cum_count += base_count


print("Result =", res)
print(datetime.now() - startTime)
print((timer()-start)*1000)
#time: 14ms