# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 12:15:34 2016

@author: Home
"""
""""""

from datetime import datetime

startTime = datetime.now()
doubles = [2*i for i in range(1,20+1)]
doubles.append(50)

dic = {}

dic[0] = 1

for l in range(1,20+1):
    dic[l] = 1
    if l%2 == 0:
        dic[l] += 1
    if l%3 == 0:
        dic[l] += 1
for d in range(21, 40+1):
    dic[d] = 0
    if d%2 == 0:
        dic[d] += 1
    if d%3 == 0:
        dic[d] += 1
for m in range(41, 60+1):
    dic[m] = 0
    if m%3 == 0:
        dic[m] += 1
for m2 in range(61, 170+1):
    dic[m2] = 0

dic[25] += 1
dic[50] += 1

def calc(k):
    res = 0
    for pos in doubles:
        if k-pos < 0:
            break
        for i in range((k-pos)//2+1):
            if i == k - pos - i:
                if dic[i] == 2:
                    res -= 1
                elif dic[i] == 3:
                    res -= 3
            res += dic[i]*dic[k-pos-i]
        
    return res

resSum = 0
for checkout in range(1, 100):
    resSum += calc(checkout)

print("result = " + str(resSum))
print(datetime.now() - startTime)
#time: 9ms

