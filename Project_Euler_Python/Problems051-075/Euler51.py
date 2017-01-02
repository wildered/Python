# -*- coding: utf-8 -*-

from eulerTools import sieve_for_primes_to
import copy

from datetime import datetime
startTime = datetime.now()

arr = [0 for i in xrange(1000000)]
primes = sieve_for_primes_to(1000000)
for p in primes:
    arr[p] = 1
def binGen(lijst, plek):
    if plek >= len(lijst[0]):
        return
    
    for idx in range(len(lijst)):
        sub = lijst[idx]
        other = copy.copy(sub)
        sub[plek] = 0
        other[plek] = 1
        lijst.append(other)
    binGen(lijst, plek+1)
    
n = 10
flag = False
toDo = [1 for i in range(1000000)]
nrray = []
c = 0
curr_bit = 0
while True:
    if toDo[n] == 0:
        n += 1
        continue
    if arr[n] == 0:
        n += 1
        continue
    c =  len(str(n))
    if c != curr_bit:
        curr_bit = c
        guide = [(c-1)*[None]]
        binGen(guide, 0)
        toDel = c*[0]
        for sub in guide:
            sub.append(0)
        guide.remove(toDel)

    fake = []
    lengte = len(str(n))
    word = str(n)
    for conf in guide:
        teller = 0
        letters = list(word)
        for i in range(10):
            if i == 0 and conf[0] == 1:
                continue
            for idx in range(lengte):
                if conf[idx] == 1:
                    letters[idx] = str(i)
            newP = int("".join(letters))
            fake.append(newP)
            if arr[newP] == 1:
                teller += 1
        
        if teller == 8:
            flag = True
            break
        if not flag:
            for el in fake:
                toDo[el] = 0
            fake = []
    if flag:
        for i in range(10):
            if conf[0] == 1 and i == 0:
                continue
            for idx in range(lengte):
                if conf[idx] == 1:
                    letters[idx] = str(i)
            newP = int("".join(letters))
            
            if arr[newP] == 1:
                break
        print newP
        break
    n += 1

print datetime.now() - startTime   
#time 1.2s        
        
