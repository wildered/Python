# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 19:53:47 2017

@author: Home
"""

from datetime import datetime
startTime = datetime.now()

def check_f(s):
    temp = set(str(s)[:9])
    return (len(temp) == 9 and '0' not in temp)

def check_t(s):
    temp = set(str(s)[-9:])
    return (len(temp) == 9 and '0' not in temp) 


F_a, F_b = 1, 1
K_a, K_b = 1, 1
counter = 2

cut_off_p = 20
cut_off = 10**cut_off_p

while True:
    counter += 1
    l = len(str(F_b))
    F_a, F_b = F_b, (F_a + F_b)%(10**10)
    K_a, K_b = K_b, K_a + K_b
    if K_a > cut_off:
        K_b = K_b/(10**(len(str(K_a)) - cut_off_p))
        K_a = K_a/(10**(len(str(K_a)) - cut_off_p))
    if check_t(F_b) and check_f(K_b):
        break

print "result = " + str(counter)
print datetime.now() - startTime
#time: 0.95s


