# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 13:38:43 2017

@author: Home
"""

#For each tile, we only have to check the first and the last tile.
#For any tile that is not the above nor a corner, there will be 2 neighbours
#of the same ring, giving a difference of 1 which is not prime. 
#For the inner and outer ring, there will be 2 subsequent neighbours, which 
#will give (in total) 2 odd differences, and 2 even differences. Outside of 
#the first ring, differences cannot be 2, so an even difference will not be
#prime, so at most we have 2 prime numbers. For the corner cells, we have
#that they border 1 inner corner ring cell, and 3 subsequent outer ring cells
#of which the middle is a corner as well. 
#Because each ring constists of 6 parts of length k, where k is the ring 
#number, the parity of the corners will be either both even, or the curent
#corner cell one parity, and the neighbouring parities opposing. We now have 
#2 odd and 2 even differences, giving at most 2 prime differences. 
#
#time: 100ms


from eulerTools import isPrime, sieve_for_primes_to
from datetime import datetime
from timeit import default_timer as timer

startTime = datetime.now()
start = timer()

max_prime = int(1e6)
primes = set(sieve_for_primes_to(max_prime))

def prime(n):
    if n > max_prime:
        return isPrime(n)
    return n in primes

idx = 0
k = 0
target = 2000
resSet = set()

while idx < target:
    p_1 = 6*(k+1) - 1
    if prime(p_1):
        resSet.add(p_1)
        p_2 = p_1 + 2
        p_3 = p_1 + p_2 + 5
        if prime(p_2) and prime(p_3):
            idx += 1
            
        p_5 = p_1 + 6
        p_6 = p_1 + p_1 - 5
        if prime(p_5) and prime(p_6):
            idx += 1
        
    k += 1

k -= 1
if idx == target:
    n = n1 = 2 + 3*k*(k+1)
else:
    n = 2 + 3*(k+1)*(k+2) - 1

print("Result =", n)
print(datetime.now() - startTime)
print((timer()-start)*1000)
#time: 100mss


