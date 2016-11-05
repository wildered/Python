# -*- coding: utf-8 -*-
"""
Created on Sat Nov 05 17:18:35 2016

@author: Home
"""

from math import factorial
from datetime import datetime
startTime = datetime.now()

done = {}
sts = [i for i in range(10)]
s = [factorial(i) for i in range(10)]
follow = {}

def stap(c):
    return sum([s[int(l)] for l in c])

def signature(n):
    a = str(n)
    return "".join(sorted(list(a)))
        
def permsdic(d):
    r = s[sum([d[el] for el in d])]
    for el in d:
        if d[el] == 0:
            continue
        r /= s[d[el]]
    return r
    
def perms(k):
    n = str(k)
    if n == "0":
        return 1
    d = {}
    for c in str(n):
        d[c] = 0
    for c in str(n):
        d[c] += 1
        
    if "0" not in d:
        r = s[len(str(n))]
        for el in d:
            r /= s[d[el]]
        return r
    else:
        #number cannot start with 0; to prevent problems
        r = 0
        for i in d:
            if i == '0':
                continue
            d[i] -= 1
            r += permsdic(d)
            d[i] += 1
        return r

def func(r, idx, end):
    """Fills list of signatures"""
    if end == 5:
        for i in sts[idx:]:
            done[r+str(i)] = done[r] + s[i]
    else:
        for i in sts[idx:]:
            new_r = r+str(i)
            done[new_r] = done[r] + s[i]
            func(new_r, i, end+1)

loop_d = {}
inj_d = {}

done[""] = 0
done["0"] = 1
func("", 0, 0)

for el in done:
    follow[el] = signature(done[el])

clen = 60
a = list(done)

todo = list(done)
res = 0

def volg(curr):
    if curr not in follow:
        new_curr = signature(stap(curr))
    else:
        new_curr = follow[curr]
    return new_curr

def lengthfinder(curr):
    prev = []
    counter = 1
    flag = False
    
    while True:
        prev.append(curr)
        
        new_curr = volg(curr)
        
        if new_curr in prev:
            break
        
        if new_curr in loop_d:
            counter += loop_d[new_curr]
            if counter == clen-1:
                #case in which cycle is of length len(cycle)+1 by permutation
                currtemp = new_curr
                while volg(currtemp) != new_curr:
                    currtemp = volg(currtemp)
                if stap(curr) == stap(currtemp):
                    pass
                else:
                    counter += 1
                    
            flag = True
            break
        if new_curr in inj_d:
            counter += inj_d[new_curr]
            flag = True
            break
        curr = new_curr
        counter += 1
        
    if not flag:
        for idx in range(prev.index(new_curr)):
            inj_d[prev[idx]] = counter-idx
            if prev[idx] in follow:
                todo.remove(prev[idx])
        
        lc = len(prev)-prev.index(new_curr)
        for bdx in range(prev.index(new_curr), len(prev)):
            loop_d[prev[bdx]] = lc
            if prev[bdx] in follow:
                todo.remove(prev[bdx])
    else:
        for idx in range(len(prev)):
            inj_d[prev[idx]] = counter-idx
            if prev[idx] in follow:
                todo.remove(prev[idx])
    return counter

done_set = set()
while len(todo) > 0:
    sig = todo[0]
    curr = sig
    
    counter = lengthfinder(curr)
    
    if counter >= clen:
        out = counter
        tcurr = curr
        while out > clen:
            if curr in inj_d:
                tcurr = volg(tcurr)
                out -= 1
            else:
                tcurr = volg(tcurr)
                out -= 1
        if tcurr in done_set:
            pass
        else:
            #In case clen < maximum, then multiple might take same path
            done_set.add(tcurr)
            res += perms(str(tcurr))
            print sig           

print "Final Result = " + str(res)
print datetime.now() - startTime
#time: 120ms

