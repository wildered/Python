# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 21:21:20 2017

@author: Home
"""

#Once a bouncy subsequence is found, we can just skip over the remaining
#digits as they'll form bouncy numbers as well and count these.
#In order not to skip over the target, we only increment by one should we 
#exceed the target. However, it is true that the ratio sequence is **not**
#strictly increasing. However, at every n we stop the 100% of the numbers we 
#skip, should res >= 1, are bouncy. Therefore this ratio sequence is 
#increasing with regard to the previous entry. (If none found it will be
#decreasing). Conclusion: we **don't** skip the target. 
#time: 0.10s

from datetime import datetime

startTime = datetime.now()


def incr_one(n_arr, startIdx, more=1):
    for idx in range(startIdx, -1, -1):
        n_arr[idx] += 1
        if n_arr[idx] != 10:
            return None
        n_arr[idx] = 0
    if idx == 0:
        n_arr.insert(0, 1)
    return None


def set_arr(n_arr, idx, number):
    if number != 0:
        n_arr[idx] = number
    else:
        n_arr[idx] = 0
        for bdx in range(idx-1, -1, -1):
            n_arr[bdx] += 1
            if n_arr[bdx] != 10:
                break
            n_arr[bdx] = 0


def bouncy(n_arr, teller, n):
    sign = 0
    prev = n_arr[0]
    for idx in range(1, len(n_arr)):
        curr = n_arr[idx]
        new_sign = (curr > prev) - (curr < prev)
        if sign == 0:
            sign = new_sign
        elif new_sign != 0 and sign != new_sign:
            if sign == 1:
                k = prev - curr
                new_d = prev
            else:
                k = 10 - curr
                new_d = 0
                
            d_left = len(n_arr) - 1 - idx
            res = k*10**d_left
            temp_n = n + res
            if (teller + res)/temp_n > 0.99:
                incr_one(n_arr, len(n_arr) - 1)
                return 1, n+1
            set_arr(n_arr, idx, new_d)
            return res, temp_n
                
        prev = curr
            
    incr_one(n_arr, len(n_arr) - 1)
    return 0, n + 1


n_arr = [1, 0, 0]
n = 100
teller = 0
ratio = teller/n

while ratio != 0.99:
    incr, n = bouncy(n_arr, teller, n)
    teller += incr
    ratio = teller/n

print("result = " + str(n))
print(datetime.now() - startTime)
#time: 0.10s

