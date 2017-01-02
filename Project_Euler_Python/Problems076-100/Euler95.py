# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 22:06:55 2016

@author: Home
"""

"""The algorithm works as follows. First we find the image of every 
number <= 1e6 under the sum of divisors function. Then, in order, pick 
an element an if it has found already, skip it. If not, run the 
function until either > 1e6 or a chain has been found. An array is 
maintained with 0 if it can be skipped. Finally min of max length 
chain"""

from datetime import datetime
startTime = datetime.now()

hoog = 1000000

def sieve_for_primes_to(n):
    """prime sieve. It also returns an array from which a prime
    divisor for a number can be deduced"""
    size = n//2
    sieve = [1]*size
    translate = [1]*size
    limit = int(n**0.5)
    for i in range(1,limit):
        if sieve[i]:
            val = 2*i+1
            tmp = ((size-1) - i)//val 
            sieve[i+val::val] = [0]*tmp
            translate[i+val::val] = [val]*tmp
    return [2] + [i*2+1 for i, v in enumerate(sieve) if v and i>0], translate

primes, prime_find_arr = sieve_for_primes_to(hoog+1)

d = {}
d[0] = 0
d[1] = 0
for el in primes:
    d[el] = 1

def recur(n):
    """A more efficient divisor sum calculator than summing i + n/i
    for n%i == 0, i = 2, ... , int(sqrt(n)). If we have a prime 
    divisor (fast because of p_find()) and divide the number by the 
    highest power by which it is still divisible, we have a number 
    ntemp not divisible by the prime p. As such, we will call the 
    divisors from this number the "primitive divisors". e.g. 1, 3, 5 
    for ntemp = 15 (p not 3 or 5). Now for p^k we get as divisors 
    of n = ntemp * p^k the following: a*(1, p^1, .. p^k) for 
    a = 1, 3, 5. As ntemp itself will now also be a divisor, 
    ntemp*(1, p^1, ... , p^(k-1)) will also be divisors. Direct sum 
    for this gives lower computing time. """
    
    if n in d:
        return d[n]
    
    #uses the extra array returned by the sieve to find a prime
    #divisor of i
    if n%2 == 0:
        p = 2
    else:
        p = prime_find_arr[(n-1)/2]
    exp = 1    
    ntemp = n/p
    while ntemp%p == 0:
        exp += 1
        ntemp /= p
    
    primitive = recur(ntemp)
    res = ((1-p**(exp+1))/(1-p))*primitive + \
        ((1-p**(exp))/(1-p))*ntemp
    
    d[n] = res
    return res
    

i = 1
chains = []
arr = [1 for pp in range(hoog+1)]
find_follow = [recur(k) for k in range(hoog+1)]
arr[0] = 0
arr[1] = 0
max_l = 0
longest_path = None

while i <= hoog:
    if arr[i] != 1:
        i += 1
        continue
    
    curr = i
    path = []
    while True:
        volgende = find_follow[curr]
        if volgende  > hoog or arr[volgende] != 1:
            for el in path:
                arr[el] = 0
            break
        
        if volgende in path:
            idx = 0
            while path[idx] != volgende:
                arr[path[idx]] = 0
                idx += 1
                
            if (len(path) - idx) > max_l:
                max_l = (len(path) - idx)
                longest_path = path[idx:]
                
            while idx < len(path):
                arr[path[idx]] = i  #might be useful
                idx += 1            
            break
        path.append(volgende)
        curr = volgende
    i += 1
    
print "Result = " + str(min(longest_path))
print datetime.now() - startTime
#time: 2.4s


