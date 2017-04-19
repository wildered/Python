# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 23:23:20 2017

@author: Home
"""

#Time: 25s

from datetime import datetime
startTime = datetime.now()

dic = {}
dic[0] = [0, [set()]]
dic[1] = [0, [set()]]
dic[2] = [1, [{2}]]

high = 200
for k in range(3, high + 1):
    curr_l = high + 1
    output = [None, high + 1]
    for i in range(1, k//2 + 1):
        l1 = dic[i][0]
        for sol1 in dic[i][1]:
            l2 = dic[k-i][0]
            for sol2 in dic[k-i][1]:
                rest = sol1.intersection(sol2)
                l = l1 + l2 +  1 - len(rest)
                if l == curr_l:
                    res = sol1.union(sol2)
                    res.add(k)
                    output.append(res)
                elif l < curr_l:
                    res = sol1.union(sol2)
                    res.add(k)
                    output = [res]
                    curr_l = l
    dic[k] = [curr_l, output]
    
counter = 0
for n in range(1, high+1):
    counter += dic[n][0]

print("result = " + str(counter))
print(datetime.now() - startTime)
#time: 25s

