# -*- coding: utf-8 -*-
"""
Created on Thu Dec 01 14:34:20 2016

@author: Home
"""

"""
The algorithm works as follows: Assume for any cuboid <= M-1 it has 
been calculated. Only those with at least one side M remain to count.
Using a pythagorean triplet generating algorithm, we find all triples 
(a, b, c) containing M, with a, b <= 2M. If we have sides s1, s2, s3 
for the cuboid, and a = M = s1 (wlog), then b = s2 + s3 ("fold out the
cuboid" for the shortest path) and we can calculate the amount of 
integer sides (with s2 >= s3 as we're barring rotation) can be 
calculated in O(1). Continue until given value exceeded.
"""

from fractions import gcd
from math import sqrt, ceil

from datetime import datetime
startTime = datetime.now()
#print datetime.now() - startTime

sq_set = set()

sq_idx = 1
l = pow(sq_idx, 2)

def sq_check(n):
    """This functions checks if a number is square. A set of squares
    is maintained throughout, and if a number higher than the highest
    square is checked, squares are added to ensure correct answer
    O(1)?"""
    global sq_idx, sq_set, l
    if n >= l:
        k = pow(sq_idx, 2)
        while n >= k:
            sq_set.add(k)
            sq_idx += 1
            k = pow(sq_idx, 2)
        l = pow(sq_idx, 2)
    return n in sq_set

d = {}

def d_add(key, el):
    """Function to add to dictionary and create entry if needed"""
    global d
    if key in d:
        d[key].append(el)   
    else:
        d[key] = [el]   #number can have multiple triplets

def calc(M, p):
    """amount/2, floored because (k,k) counted once, and (m,k)
    with m > k counted once"""
    if p <= 1 or p > 2*M:
        return 0
    if p > M:
        p = 2*(M+1)-p
    return p/2
    

def find_old(M):
    """As the pyth. tripl. algorithm generates primitive triplets,
    we have to find the other side in the non-primitive. O(n)? """
    global d
    res = 0
    for key in d:
        if M%key == 0:
            for b in d[key]:
                q = b*M/key
                res += calc(M, q)
    return res

def find_new1(M):
    """Use the algorithm if nm = M. Lower and upper bounds for n, m 
    can be deduced mathematically. O(sqrt(M)log(M))?"""
    if M%2 == 0:
        return 0
    global d
    res = 0
    n = int(ceil(sqrt((sqrt(5)-2)*M)))
    if n%2 == 0:
        n += 1
    eind = int(sqrt((2+sqrt(5))*M))
    if eind%2 == 0:
        eind -= 1
    n_hoog = min(sqrt(M+1)-1, eind)
    while n <= n_hoog:
        if M%n == 0:
            m = M/n
            if gcd(m, n) == 1:
                new_prim_b = (pow(m, 2) - pow(n, 2))/2
                d_add(M, new_prim_b)
                res += calc(M, new_prim_b)
                
        n += 2
    return res

def find_new2(M):
    """Use the algorithm if (m^2-n^2)/2 = M. Lower and upper bounds 
    for n, m can be deduced mathematically. O(sqrt(M)log(M))?"""
    res = 0
    n = 1
    eind_n = sqrt((sqrt(5)-1)*M)
    while n <= eind_n:
        m2 = 2*M+pow(n,2)
        if sq_check(m2):
            m = int(sqrt(m2))
            if gcd(m, n) == 1:
                new_primitive_b = n*m
                d_add(M, new_primitive_b)
                res += calc(M, new_primitive_b)
        n += 1
    return res
        
M = 1
res = 0
hoog = 1000000
while res <= hoog:
    res += find_old(M)
    res += find_new1(M)
    res += find_new2(M)
    
    M += 1
M -= 1      #Compensation
    
print M
    
print datetime.now() - startTime
#time 65ms

