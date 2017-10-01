# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 21:37:23 2017

@author: Home
"""

from eulerTools import sieve_for_primes_to
from datetime import datetime
from timeit import default_timer as timer
import random

def isPrime_oud(n, low_prime):
    if n%2 == 0:
        return False
    q = 3
    while q*q <= n:
        if n%q == 0:
            return False
        q += 2
    return True

def isPrime(n, low_prime):
    for k in range(4000):
        a = random.randint(2, n-2)
        if pow(a, n-1, n) != 1:
            return False
    return True
        


def check(n, low_prime):
    m = n*n
    if not isPrime(m + 1, low_prime):
        return False, 1
    if not isPrime(m + 3, low_prime):
        return False, 3
    if not isPrime(m + 7, low_prime):
        return False, 7
    if not isPrime(m + 9, low_prime):
        return False, 9
    if not isPrime(m + 13, low_prime):
        return False, 13
    if not isPrime(m + 27, low_prime):
        return False, 27
    return True


startTime = datetime.now()
start = timer()

high_prime = 19
primes = sieve_for_primes_to(high_prime + 1)
mod_classes = []
temp_mod_classes = []

additions = [1, 3, 7, 9, 13, 27]


for idx, prime in enumerate(primes):
    mod_list = []
    for k in range(prime):
        flag = True
        for add in additions:
            if (k*k + add)%prime == 0:
                flag = False
                break
        if flag:
            mod_list.append(k)
    mod_classes.append(mod_list)
    
    

def find_new(x, mod_x, y, mod_y):
    res = x
    while res%mod_y != y:
        res += mod_x
    return (res, mod_x * mod_y)

high = 150e6
res_list = []
def func(x, mod_x, prime_idx):
    if prime_idx == len(primes):
        while x < high:
            res_list.append(x)
            x += mod_x
        return
    mod_y = primes[prime_idx]
    for y in mod_classes[prime_idx]:
        new_x, new_mod_x = find_new(x, mod_x, y, mod_y)
        if new_x > high:
            continue
        func(new_x, new_mod_x, prime_idx + 1)
        
func(0, 1, 0)
res_list.sort()

next_high_prime = 150000000
next_primes = sieve_for_primes_to(next_high_prime)
next_primes = [el for el in next_primes if el > high_prime]

for idx, prime in enumerate(next_primes):
    new_res_list = []
    mod_list = set()
    for n in res_list:
        flag = True
        for add in additions:
            if (n*n + add != prime) and (n*n + add)%prime == 0:
                if n == 10:
                    print("what", prime)
                flag = False
                break
        if flag:
            new_res_list.append(n)
    res_list = new_res_list

print("Reached here")

p_sum = sum(res_list)
#p_sum = 0
#final_res_list = []
#for idx, n in enumerate(res_list):
#    val = check(n, next_high_prime)
#    if type(val) == tuple:
#        continue
#    p_sum += n
#    print("Found:", n, "idx =", idx, "partial sum =", p_sum)
#    final_res_list.append(n)            


print(len(res_list))
print("Result =", p_sum)
print(datetime.now() - startTime)
print((timer()-start)*1000)

#315410
#927070

#result: 676333270
