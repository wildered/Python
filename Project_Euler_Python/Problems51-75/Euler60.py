# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 21:42:50 2016

@author: Home
"""

from eulerTools import isPrime
from eulerTools import sieve_for_primes_to

from datetime import datetime
startTime = datetime.now()
hoog = 10000


def digitsum(n):
    return sum([int(c) for c in str(n)])

primes = sieve_for_primes_to(hoog)
primes.remove(2)
arr = [0 for i in xrange(hoog)]
d = {}
for i in range(len(primes)):
    d[primes[i]] = i

def func():
    idx = 0
    m = len(primes)
    
    while True:
        p = primes[idx]
        cdx = idx+1    
        
        while cdx < m:
            temp = [p]
            a1 = digitsum(p)%3
            
            bdx = cdx
            while bdx < m:
                new_p = primes[bdx]
                if ((digitsum(new_p))%3) != a1:
                    bdx += 1
                    continue
                flag = True
                for pr in temp:
                    front = int(str(pr) + str(new_p))
                    back = int(str(new_p)+ str(pr))
                    if not(isPrime(front) and isPrime(back)):
                        flag = False
                        break
                if flag:
                    temp.append(new_p)
                if len(temp) >= 5:
                    print "FOUND ONE"
                    print temp
                    print "Result = " + str(sum(temp))
                    return
                    
                bdx += 1
            
            if len(temp) > 1:
                cdx = d[temp[1]]+1
            else:
                break
        
        idx += 1

func()
#I am aware that this is not guaranteed to give the lowest sum (it does in this case) and a guess for an
#upper bound has no argumentation
print datetime.now() - startTime
start = 3
#time 6s
    



