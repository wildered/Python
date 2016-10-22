# -*- coding: utf-8 -*-
from datetime import datetime
startTime = datetime.now()
from eulerTools import palindromeCheck

def lTest(n):
    for i in range(50):
        n = n + int(str(n)[::-1])
        if palindromeCheck(n):
            return True
    return False

counter = 0
for i in range(1, 10000):
    if not lTest(i):
        counter += 1
          
print counter
print datetime.now() - startTime
#time 90ms

