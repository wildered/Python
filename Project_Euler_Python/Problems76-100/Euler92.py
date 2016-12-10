# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 12:39:27 2016

@author: Home
"""

"""
The algorithm works as follows: 
It is clear that the next step in a sequence is defined fully by the
set of digits (the order doesn't matter). It remains to find all 
unique sets of digits below 10 000 000, determine if they reach 89, 
and if so, multiply by the amount of (allowed) permutations of the
set. During each sequence every set reached can be counted and doesn't
have to be counted again. 

"""

#%%
from math import factorial
from datetime import datetime
startTime = datetime.now()


done = {}
sts = [i for i in range(10)]
sqs = [i**2 for i in range(10)]
s = [factorial(i) for i in range(10)]
follow = {}

def stap(c):
    return sum([sqs[int(l)] for l in c])

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
    if end == 6:
        for i in sts[idx:]:
            done[r+str(i)] = done[r] + sqs[i]
    else:
        for i in sts[idx:]:
            new_r = r+str(i)
            done[new_r] = done[r] + sqs[i]
            func(new_r, i, end+1)

end_d = {}
end_d["1"] = False
end_d["89"] = True

done[""] = 0
done["0"] = 0
func("", 0, 0)

for el in done:
    follow[el] = signature(done[el])

clen = 60
a = list(done)

todo = list(done)
del todo[0]

def volg(curr):
    if curr not in follow:
        new_curr = signature(stap(curr))
    else:
        new_curr = follow[curr]
    return new_curr



def lengthfinder(curr):
    global todo, ans
    prev = []
    
    while True:
        prev.append(curr)
        
        new_curr = volg(curr)
        
        if new_curr in end_d:
            res = end_d[new_curr]
            break
        curr = new_curr
        
    if not res:
        for el in prev:
            end_d[el] = res
            todo.remove(el)
    else:
        for el in prev:
            end_d[el] = res
            todo.remove(el)
            ans += perms(str(el))
            
    return res

ans = 0

#%%
while len(todo) > 0:
    sig = todo[0]
    curr = sig
    if follow[curr] == "0":
        del todo[0]
        continue
    
    counter = lengthfinder(curr)
      

print "Final Result = " + str(ans)
print datetime.now() - startTime
#time: 280ms

