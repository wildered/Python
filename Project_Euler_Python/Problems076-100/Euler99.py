# -*- coding: utf-8 -*-
"""
Created on Fri Jan 06 21:34:19 2017

@author: Home
"""

""" We compare a^p and b^q if the numbers are small enough. Else we 
compare a^(p/2) and b^(q/2) = much faster"""

from datetime import datetime
startTime = datetime.now()


def compare(base1, exp1, base2, exp2):
    if exp1 < 5 or exp2 < 5:
        return cmp(pow(base1, exp1), pow(base2, exp2))
    else:
        return compare(base1, exp1/2.0, base2, exp2/2.0)

f = open('p099_base_exp.txt', 'r')

res_arr = []

for placeholder in f:
    line = placeholder.replace("\n", "")
    [base, exp] = line.split(",")
    temp_arr = [int(base), int(exp)]
    res_arr.append(temp_arr)
    
res_out = res_arr[0]
[base_out, exp_out] = res_out
for el in res_arr:
    [base_new, exp_new] = el
    if compare(base_new, exp_new, base_out, exp_out) == 1:
        [base_out, exp_out] = el
        res_out = el


print "result = " + str(res_out)
print "line number = " + str(res_arr.index(res_out)+1)
print datetime.now() - startTime
#time: 10ms

