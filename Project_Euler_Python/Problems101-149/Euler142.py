# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 16:25:03 2017

@author: Home
"""

from math import gcd, sqrt
from datetime import datetime
from timeit import default_timer as timer


startTime = datetime.now()
start = timer()

a_dic = dict()

#could be sped up using SortedDict
min_sum = float("inf")


m = 1
for m in range(1, 1500, 2):
    if m*m//2 > 1500:
        break
    for n in range(1, m, 2):
        if gcd(m, n) != 1:
            continue
        f = (m*m - n*n)//2
        c = m*n
        a = (m*m + n*n)//2
        if a > 1500:
            break
        if f > c:
            f, c = c, f
        for k in range(1, 1500//a + 1):
            an = k*a
            fn = k*f
            cn = k*c
            if an in a_dic:
                a_dic[an].append([fn, cn])
            else:
                a_dic[an] = [[fn, cn]]
        
print("Done generating dictionary")

for key in a_dic:
    a = key
    for comb in a_dic[key]:
        [f, c] = comb
        for other_key in a_dic:
            if a%other_key == 0:
                k = a//other_key
                for other_comb in a_dic[other_key]:
                    e1 = other_comb[0] * k
                    e2 = other_comb[1] * k
                    for e in [e1, e2]:
                        x = (a*a + c*c - e*e)
                        y = (a*a + e*e - c*c)
                        z = (c*c + e*e - a*a)
                        if (x%2 != 0 or y%2 != 0 or z%2 != 0):
                            continue
                        x //= 2
                        y //= 2
                        z //= 2
                        if (x <= 0 or y <= 0 or z <= 0 or x - y <= 0):
                            continue
                        if sqrt(x-y) == int(sqrt(x-y)) and (x > y > z > 0):
                            temp_sum = x + y + z
                            if temp_sum < min_sum:
                                min_sum = temp_sum
                                print("Min sum = ", min_sum)
                                print("a = {}, c = {}, e = {}".format(a, c, e))
                                print("x = {}, y = {}, z = {}".format(x, y, z))
print(datetime.now() - startTime)
print((timer()-start)*1000)
#time: 0.2s
