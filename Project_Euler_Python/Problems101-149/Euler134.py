# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 11:16:16 2017

@author: Home
"""

from eulerTools import sieve_for_primes_to
from datetime import datetime


def solution_finder(p1, p2):
    q = pow(10, len(str(p1)), p2)
    a, b = p2, q
    prev_x = 0
    x = 1
    while b != 1:
        floor_div = a//b
        x, prev_x =  prev_x - x*floor_div, x
        a, b = b, a - floor_div*b
    res_coeff = x * -p1//b
    res_coeff = res_coeff - res_coeff//p2 * p2
    res = res_coeff*pow(10, len(str(p1))) + p1
    return res


startTime = datetime.now()
p_list = sieve_for_primes_to(1000011)
p_list = p_list[2:]
res = 0

for idx in range(len(p_list) - 1):
    res += solution_finder(p_list[idx], p_list[idx+1])

print("Result =", res)    
print(datetime.now() - startTime)
#time: 0.50s
