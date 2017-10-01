# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 21:03:45 2017

@author: Home
"""

#bruteforcing...

from datetime import datetime
from math import sqrt, gcd
from eulerTools import primeFactor
ressum = 0

startTime = datetime.now()

vals = [3, 102, 130, 312, 759, 2496, 2706, 3465, 6072, 6111, 8424, \
        14004, 16005, 36897, 37156, 92385, 98640, 112032, 117708, 128040, \
        351260, 378108, 740050]


for n in vals:
    m = n*n
    for d in range(2, n + 1):
        if m%d == 0:
            continue
        q = m // d
        r = m % d
        if q**2 == r*d or r**2 == q*d or d**2 == r*q:
            print("n = {:>6}, n^2 = {:>12}, q = {:>6}, d = {:>6}, r = {:>6}, a = {}/{}".format(n, m, q, d, r, d//gcd(d, r), r//gcd(d, r)))
#            print("n = {:>6}, n^2 = {:>12}, q = {:>6}, d = {:>6}, r = {:>6}, a = {}/{}, {}".format(n, m, q, d, r, d//gcd(d, r), r//gcd(d, r), gcd(n**2-r, r**2)))
#            print("n = {:>6}, {}, q = {:>6}, {}, d = {:>6}, "
#            "{}, r = {:>6}, {}, a = {}/{}".format(n, primeFactor(n), q, primeFactor(q), \
#             d, primeFactor(d), r, primeFactor(r), d//gcd(d, r), r//gcd(d, r)))
#            print("q = {:>6}, {}, d = {:>6}, "
#            "{}, r = {:>6}, {}, a = {}/{}".format(q, primeFactor(q), \
#             d, primeFactor(d), r, primeFactor(r), d//gcd(d, r), r//gcd(d, r)))
            y = d//gcd(d, r)
            x = r//gcd(d, r)
#            print(q**3*n**2//r, primeFactor(q**3*n**2//r))
#            print(m%x == 0)
#            print(gcd(n**2-r, r**2), (n**2-r)//gcd(n**2-r, r**2), r**2//gcd(n**2-r, r**2))
#            print((2*y**3 *r**2)**(1/2))
#            print(q*d/r, m%r == 0)
#            print("n = {:>6}, factors: {}, d = {}, factors: {}".format(n, primeFactor(n), d, primeFactor(d)))
            ressum += m


l = []
for idx in range(2, len(vals)):
    l.append(vals[idx] - 3*vals[idx-1])

print(l)

#for n in range(2, 10000):
#    m = n*n
#    d_t = 1
#    flag = True
#    while True:
#        for mult in [1, 2, 3, 5, 10, 15, 23]:
#            d = d_t*d_t * mult
#            if m%d == 0:
#                continue
#            q = m // d
#            r = m % d
#            if q**2 == r*d or r**2 == q*d or d**2 == r*q:
#                print("n = {}, n^2 = {}, q = {}, d = {}, r = {}, a = {}/{}".format(n, m, q, d, r, d//gcd(d, r), r//gcd(d, r)))
#                ressum += m
#        d_t += 1
#        if d_t*d_t >= n:
#            break

#n = 38300
#
#total_flag = True
#while True:
#    m = n*n
#    if n%100 == 0:
#        print(n)
#    for d in range(2, n):
#        if n%d == 0:
#            continue
#        q = m // d
#        r = m % d
#        if r*q == d**2 or r*d == q**2:
#            print("n = {}, n^2 = {}, q = {}, d = {}, r = {}, a = {}/{}".format(n, m, q, d, r, d//gcd(d, r), r//gcd(d, r)))
#            total_flag = False
#            break
#    if not total_flag:
#        break
#            
#
#    n += 1



print(ressum)
print(datetime.now() - startTime)
#time: 3.6s


#: 98640 q = 123201 d = 78975 r = 50625

