# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 00:49:45 2017

@author: Home
"""

from math import gcd
from datetime import datetime

startTime = datetime.now()


link_dic = {}

m = 1
while True:
    for n in range(1, m):
        if gcd(n, m) != 1:
            continue
        if m%3 == n%3:
            continue
        p = 2*m*n + n*n
        q = m*m - n*n
        if p + q > 120000:
            break
        for k in range(1, 120000//(p+q) + 1):
            if k*p in link_dic:
                link_dic[k*p].add(k*q)
            else:
                link_dic[k*p] = set([k*q])
            if k*q in link_dic:
                link_dic[k*q].add(k*p)
            else:
                link_dic[k*q] = set([k*p])
    
    m += 1
    if m*m + 2*m > 120000:
        break
    
keys = list(link_dic.keys())
keys.sort()

res_set = set()

sort_link_dic = {}
for key in keys:
    sort_link_dic[key] = sorted(list(link_dic[key]))

for idx in range(len(keys)):
    link1 = keys[idx]
    links = sort_link_dic[link1]
    for link2 in links:
        if link2 > link1:
            break
        for link3 in sort_link_dic[link2]:
            if link3 > link2:
                break
            if link1 in link_dic[link3]:
#                print("Found: ", link1, link2, link3)
                temp_sum = link1 + link2 + link3
                if temp_sum <= 120000:
                    res_set.add(temp_sum)

        
print("Res =", sum(res_set))
print(datetime.now() - startTime)
#time: 0.78s

