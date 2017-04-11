# -*- coding: utf-8 -*-
"""For any subset pairs of size i there are n choose 2i ways to choose the 2i
members, and (2i-1) choose (i-2) ways to distribute the members of 
"""
from eulerTools import nChoosek
from datetime import datetime
startTime = datetime.now()

n = 12
resSum = 0

for i in range(2, n//2+1):
    resSum += nChoosek(n, 2*i) * nChoosek(2*i-1, i-2)

print("result = " + str(resSum))
print(datetime.now() - startTime)



