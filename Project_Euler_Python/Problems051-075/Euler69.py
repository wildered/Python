# -*- coding: utf-8 -*-

from eulerTools import isPrime
from datetime import datetime
startTime = datetime.now()

#more prime factors => phi(n) is minimal

hoog = 1000000
r = 1
n = 2
while r < hoog:
    if isPrime(n):
        r *= n
    n += 1
r /= (n-1)

print "res = " + str(r)
print (datetime.now() - startTime)
#5ms
