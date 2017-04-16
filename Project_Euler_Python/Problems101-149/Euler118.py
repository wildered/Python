# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 00:08:18 2017

@author: Home
"""

#most of the time is spent on handling primes, not finding combinations(80ms)
#total time: 10.3s


from eulerTools import sieve_for_primes_to

from datetime import datetime
startTime = datetime.now()

#note: 123456789 or a permuation is not prime
primes = sieve_for_primes_to(98765432+1)
prime_arr = []
prime_d = {}



for p in primes:
    p_str = str(p)
    if '0' in p_str:
        continue
    p_set = set(p_str)
    if len(p_set) == len(p_str):
        p_tuple = tuple(sorted(list(p_set)))
        if p_tuple in prime_d:
            prime_d[p_tuple] += 1
        else:
            prime_d[p_tuple] = 1

        
p_keys = list(prime_d.keys())
p_keys.sort(reverse=True, key=lambda x: (len(x), x))


print("Time spent on primes:", datetime.now() - startTime)
startTime2 = datetime.now()

length_arr = [0 for k in range(9)]
length_arr[8] = 0
length_arr[0] = len(p_keys)
l = 7
idx = 0
max_idx = len(p_keys)
while idx < max_idx:
    if len(p_keys[idx]) == l:
        length_arr[l] = idx
        l -= 1
    idx += 1


const = set("123456789")
def complement(s):
    return const.difference(s)


totalres = 0


def count(curr_set, idx, ways):
    if len(curr_set) == 9:
        global totalres
        totalres += ways
        return None
    elif idx >= max_idx:
        return None
    other_set = complement(curr_set)
    new_idx = max(idx, len(other_set))
    
    while new_idx < max_idx:
        temp_set = set(p_keys[new_idx])
        if len(curr_set.intersection(temp_set)) == 0:
            new_set = curr_set.union(temp_set)
            new_ways = ways * prime_d[p_keys[new_idx]]
            count(new_set, new_idx + 1, new_ways)
        
        new_idx += 1
    



for bdx in range(len(p_keys)):
    count(set(p_keys[bdx]), bdx + 1, prime_d[p_keys[bdx]])


print("Result = ", totalres)
print("Time on algorithm:", datetime.now() - startTime2)
print("Total time:", datetime.now() - startTime)
#total time: 10.3s


