# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 10:47:10 2017

@author: Home
"""

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
    #only classes with positive solutions for x
    #class 0 
    if i == 0:
        F, G = expand(2*m)
        x = (F + 5*G - 1)//5
        y = F + G
    
    #class 2
    if i == 2:
        F, G = expand(2*m + 1)
        x = (-F + 5*G - 1)//5
        y = F - G
    
    #class 5
    if i == 5:
        F, G = expand(2*m + 1)
        F, G = -F, -G
        x = (-4*F - 10*G -1)//5
        y = -2*F - 4*G
    
    return (x, y)

res_list = []
sol_count = 0
max_el = 0
todo = [0, 2, 5]
m = 0
for m in range(15):
    for i in todo:
        flag = False
        new_el = solution_class(i, m)[0]
        if new_el <= 0:
            continue
        if new_el > max_el:
            if sol_count > 15:
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

print("Result =", res_list[14])
print(datetime.now() - startTime)
print((timer()-start)*1000)
#time: 5.5ms

