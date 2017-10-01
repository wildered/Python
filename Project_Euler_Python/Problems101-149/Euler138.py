# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 23:26:05 2017

@author: Home
"""

#reusing code from problem 137

from eulerTools import nChoosek
from datetime import datetime
import copy
from timeit import default_timer as timer


startTime = datetime.now()
start = timer()

def expand(n):
    #expanding (9 + 4sqrt(5))^n into rational and irrational part
    #rational part
    rat_res = 0
    irrat_res = 0
    for k in range(0, n + 1, 2):
        rat_res += nChoosek(n, k) * 9**(n-k) * 4**k * 5**(k//2)
    for k in range(1, n + 1, 2):
        irrat_res += nChoosek(n, k) * 9**(n-k) * 4**k * 5**((k-1)//2)
    return rat_res, irrat_res


def solution_class(i, m):
    #only classes with positive solutions for L
    #class 1
    if i == 1:
        F, G = expand(2*m + 1)
        F, G = -F, -G
        x = -F - 2*G
        y = (2*F + 5*G - 2)//5
    
    #class 3
    if i == 3:
        F, G = expand(2*m)
        F, G = -F, -G
        x = -F - 2*G
        y = (2*F + 5*G + 2)//5
    
    return (x, y)

res_list = []
sol_count = 0
max_el = 0
todo = [1, 3]
m = 0
for m in range(15):
    for i in todo:
        flag = False
        new_el = solution_class(i, m)[0]
        if new_el <= 1:
            continue
        if new_el > max_el:
            if sol_count > 12:
                flag = True
                new_todo = copy.copy(todo)
                new_todo.remove(i)
            else:
                max_el = new_el
        res_list.append(new_el)
        sol_count += 1
    if flag:
        todo = new_todo
    
res_list.sort()
#
print("Result =", sum(res_list[:12]))
print(datetime.now() - startTime)
print((timer()-start)*1000)
#time: 12ms
