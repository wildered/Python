# -*- coding: utf-8 -*-

from datetime import datetime
startTime = datetime.now()

def digitSum(n):
    res = 0    
    for c in str(n):
        res += int(c)
    return res

result = 0
for a in range(1, 100):
    for b in range(1, 100):
        temp = digitSum(a**b)
        if temp > result:
            result = temp
            
print result
print datetime.now() - startTime
#time 0.39s


