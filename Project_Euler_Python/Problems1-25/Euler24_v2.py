# -*- coding: utf-8 -*-

from datetime import datetime
startTime = datetime.now()

from math import factorial

goal_var = 1000000-1

def signature(goal):
    res = [0 for j in range(10)]
    n = 10-1
    value = goal
    idx = 0
    
    while idx < 10:
        
        fill = 0
        
        while value >= factorial(n-idx):
            value -= factorial(n-idx)
            fill += 1
        res[idx] = fill
        
        idx += 1
    return res
    
    
def builder(sig):
    out = [0 for i in range(10)]
    nrs = [i for i in range(10)]
    
    for idx in range(10):
        nrs = [i for i in range(10)]
        for bdx in range(idx):
            nrs.remove(out[bdx])
        nrs.sort()
        out[idx] = nrs[sig[idx]]
    return "".join([str(n) for n in out])
        

a = signature(goal_var)
print builder(a)        

print datetime.now() - startTime
#computation time on system: 0.05μs
