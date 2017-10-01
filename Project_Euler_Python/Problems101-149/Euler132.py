# -*- coding: utf-8 -*-
"""
Created on Sun May 21 19:36:52 2017

@author: Home
"""

from eulerTools import isPrime, sieve_for_primes_to
from datetime import datetime

startTime = datetime.now()
counter = 0
res = 0

primes = sieve_for_primes_to(int(2e5))
primes.remove(2)
primes.remove(5)

m = 10**9
two_count = 9
five_count = 9

for p in primes:
    mod_chain_l = 1
    mod_ten_power = 1
    temp_mod = 1
    while temp_mod != 0:
        mod_ten_power = (10 * mod_ten_power)%p
        temp_mod = (temp_mod + mod_ten_power)%p
        mod_chain_l += 1
        
    temp_str = str(mod_chain_l)
    temp_two_count = 0
    temp_five_count = 0
    while mod_chain_l%2 == 0:
        mod_chain_l /= 2
        temp_two_count += 1
    
    while mod_chain_l%5 == 0:
        mod_chain_l /= 5
        temp_five_count += 1
    
    if mod_chain_l != 1:
        continue
    if temp_two_count > two_count or temp_five_count > five_count:
        continue
    counter += 1
    res += p
    
    if counter == 40:
        break


    
#        print("p =", p)
#    print(p, mod_chain_l)
        
print("First", counter, "primefactors")
print("Result =", res)
print(datetime.now() - startTime)

#time: long


