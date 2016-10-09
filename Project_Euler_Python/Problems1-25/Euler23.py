# -*- coding: utf-8 -*-

from math import sqrt

from datetime import datetime
startTime = datetime.now()

def d(a):
    if a <= 0:
        return 0
    if a == 1:
        return 1   #special case
    res = 1 #1 is always a divisor
    i = 0
    for i in range(2,int(sqrt(a))+1):
        if a%i == 0:
            res += i + a/i
    if i**2 == a:
        res -= i
    return res


def check(number):
    if d(number) > number:
        return 1
    else:
        return 0

abundlist = [12,18,20]
abundlist = []
for num in range(1,28123+1):
    if check(num):
        abundlist.append(num)
    """
    if check(num) and num%6 != 0 and num%20 != 0:
        #print num
        abundlist.append(num)
        """
print "created list"



r = [0 for i in range(28123+1)]
for idx1 in range(len(abundlist)):
    el1 = abundlist[idx1]
    if 2*el1 > 28123:
        break
    for idx2  in range(idx1, len(abundlist)):
        el2 = abundlist[idx2]
        if el1 + el2 > 28123:
            break
        r[el1 + el2] = 1

print "try = ",
print sum([i for i in range(len(r)) if r[i] == 0])

print datetime.now()-startTime
#computation time on system: 3.1s ...






