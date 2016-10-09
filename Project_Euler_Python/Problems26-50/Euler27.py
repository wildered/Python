# -*- coding: utf-8 -*-

from math import sqrt
from datetime import datetime
startTime = datetime.now()

d = {}
def Prime(n):
    if n in d:
        return d[n]
    if n == 2:
        d[n] = True
        return True
    elif n == 1:
        d[n] = False
        return False
    else:
        for i in range(2,int(sqrt(n))+1):
            if n%i == 0:
                d[n] = False
                return False
        d[n] = True
        return True

def func(a,b, n):
    return pow(n, 2) + a*n + b
    
end = 0
max_n = 1
flag = True
for k in xrange(-999,1000):
    #only range where numbers >=2 values are achieved in the first max_n terms
    for l in xrange(1000, max(2, 2-max_n**2 - max_n*k)+1, -1):  
        if Prime(l):
            n = 0
            res = func(k, l, n)
            while res >= 0 and Prime(res):
                n += 1
                res = func(k, l, n)
            if n > max_n:
                end = k*l
                max_n = n
        if max_n > l:   #non-prime is always achieved if n = l (= b), therefore break if all lower have lower potential
            flag= False
            break
    if not flag:
        break
                
print end
print datetime.now() - startTime
#computation time: 10ms
