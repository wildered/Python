# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 14:41:01 2016

@author: Home
"""

"""Simple modulo math"""

from math import log

from datetime import datetime
startTime = datetime.now()

def pow_mod(base, power):
    mod_c = 10**10
    if power < log(mod_c, base):
        return base**power
    if power%2 == 0:
        return (pow_mod(base, power/2)**2)%mod_c
    return (base*pow_mod(base, (power-1)/2)**2)%mod_c

ans = pow_mod(2, 7830457)
print "Result = " + str((28433*ans + 1)%(10**10))
for i in xrange(1000):
    pow_mod(2, 7830457)

print datetime.now() - startTime
#time: <1ms
