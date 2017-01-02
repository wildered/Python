# -*- coding: utf-8 -*-

from datetime import datetime
q = datetime.now()

def func(n):    
    idx = 1
    nrs = 0
    c = 1
    while True:
        new_idx = 10*idx
        new_nrs = nrs + c*(new_idx-idx)
        c += 1
        if (n <= new_nrs):
            break
        idx = new_idx
        nrs = new_nrs
    c -= 1
    n -= 1
    return int(str(idx + (n-nrs)/c)[(n-nrs)%c])
res = 1
l = 1
for i in range(7):
    res *= func(l)
    l *= 10
    
print res
print datetime.now() - q
#0ms
