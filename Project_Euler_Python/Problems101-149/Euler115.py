# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 19:12:04 2016

@author: Home
"""

#recursive algorithm
#time: 16ms

from datetime import datetime
startTime = datetime.now()

def F(m, n):
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
                if idx+m in dic[1]:
                    r2 = dic[0][idx+m]
                else:
                    r2 = count(idx+m, 1, high)
                    dic[1][idx+m] = r2
                
                return r1 + r2
            
    return count(0, 0, n)
        

res = 0
k = 50
while res <= 1e6:
    res = F(50, k)
    k += 1

k -= 1

print("result = " + str(k))
print(datetime.now() - startTime)
#time: 16ms

