# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 23:34:24 2016

@author: Home
"""

"""After brute-forcing the first few triples I found the following
recursive formula for the non-unique side:
a(n) = 3*a(n-1) + 3*a(n-2) - a(n-3), a(0) = 5, a(1) = 17, a(2) = 65
and for the unique side: b(n) = a(n) + (-1)**n
"""

from datetime import datetime
startTime = datetime.now()

resSum = 0
resSum += 2*5 + 6
resSum += 2*17 + 16
resSum += 2*65 + 66

a_old3 = 5
a_old2 = 17
a_old1 = 65
factor = -1

while True:
    a = 3*a_old1 + 3*a_old2 - a_old3
    perimeter = 3*a + factor
    factor *= -1
    if not (perimeter <= 1e9):
        break
    resSum += perimeter
    a_old3, a_old2, a_old1 = a_old2, a_old1, a

print "Result = " + str(resSum)
print datetime.now() - startTime
#time: <1 ms
