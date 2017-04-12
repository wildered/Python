# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 19:24:11 2016

@author: Home
"""

#time: 0.4ms

from datetime import datetime
from timeit import default_timer as timer


def F_block(m, n):
    dic = {}
    dic[0] = {}
    dic[1] = {}
    
    def count(idx, last, high):
        if idx > high:
            return 0
        elif idx == high:
            return 1
        else:
#            fill in 0
            if idx+1 in dic[0]:
                r1 = dic[0][idx+1]
            else:
                r1 = count(idx+1, 0, high)
                dic[0][idx+1] = r1
            #fill in 1
            if idx+m in dic[1]:
                r2 = dic[1][idx+m]
            else:
                r2 = count(idx+m, 1, high)
                dic[1][idx+m] = r2
            
            return r1 + r2

    return count(0, 0, n)


n = 50
startTime = datetime.now()
start = timer()
res = F_block(2, n) + F_block(3, n) + F_block(4, n) - 3

print("result = " + str(res))
print(datetime.now() - startTime)
print((timer()-start)*1000)
#time: 0.4ms


