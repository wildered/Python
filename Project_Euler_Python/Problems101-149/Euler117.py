# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 19:57:36 2016

@author: Home
"""

#Recursive algorithm, see 115 and 114
#time: 0.3ms


from datetime import datetime
from timeit import default_timer as timer


def F_block_comb(n, block1, block2, block3):
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
            #fill in block 1
            if idx+block1 in dic[1]:
                r2 = dic[1][idx+block1]
            else:
                r2 = count(idx+block1, 1, high)
                dic[1][idx+block1] = r2
            #fill in block 2
            if idx+block2 in dic[1]:
                r3 = dic[1][idx+block2]
            else:
                r3 = count(idx+block2, 1, high)
                dic[1][idx+block2] = r3
            #fill in block 3
            if idx+block3 in dic[1]:
                r4 = dic[1][idx+block3]
            else:
                r4 = count(idx+block3, 1, high)
                dic[1][idx+block3] = r4
            
            return r1 + r2 + r3 + r4
            
    return count(0, 0, n)
        
n = 50
startTime = datetime.now()
start = timer()
res = F_block_comb(n, 2, 3, 4)

print("result = " + str(res))
print(datetime.now() - startTime)
print((timer()-start)*1000)
#time: 0.3ms

