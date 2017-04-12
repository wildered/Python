"""
Created on Sun Aug 21 16:24:54 2016

@author: Home
"""

from datetime import datetime
from timeit import default_timer as timer

#recursive algorithm
#time: 0.3ms

dic = {}
dic[0] = {}
dic[1] = {}

def count(idx, last, high):
    if idx > high:
        return 0
    elif idx == high:
        return 1
    else:
        if last == 1:
#            fill in 0
            if idx+1 in dic[0]:
                r1 = dic[0][idx+1]
            else:
                r1 = count(idx+1, 0, high)
                dic[0][idx+1] = r1
            #fill in 1
            if idx+1 in dic[1]:
                r2 = dic[1][idx+1]
            else:
                r2 = count(idx+1, 1, high)
                dic[1][idx+1] = r2
            
            return r1 + r2
        else:
            #fill in 0
            if idx+1 in dic[0]:
                r1 = dic[0][idx+1]
            else:
                r1 = count(idx+1, 0, high)
                dic[0][idx+1] = r1
            #fill in three 1
            if idx+3 in dic[1]:
                r2 = dic[0][idx+3]
            else:
                r2 = count(idx+3, 1, high)
                dic[1][idx+3] = r2
            
            return r1 + r2
        
l = 50
startTime = datetime.now()
start = timer()
print("result = " + str(count(0, 0, l)))
print(datetime.now() - startTime)
print((timer()-start)*1000)
#time 0.3ms

