# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 17:12:47 2017

@author: Home
"""

#reusing code from 140

from eulerTools import nChoosek
from datetime import datetime
import copy
from timeit import default_timer as timer


startTime = datetime.now()
start = timer()

def expand(n):
    #expanding (a + bsqrt(c))^n into rational and irrational part
    #rational part
    a = 9
    b = 4
    c = 5
    rat_res = 0
    irrat_res = 0
    for k in range(0, n + 1, 2):
        rat_res += nChoosek(n, k) * a**(n-k) * b**k * c**(k//2)
    for k in range(1, n + 1, 2):
        irrat_res += nChoosek(n, k) * a**(n-k) * b**k * c**((k-1)//2)
    return rat_res, irrat_res


def solution_class(i, m):
    #only classes with positive solutions for x
    #class 0
    if i == 0:
        F, G = expand(2*m)
        x = (17*F + 35*G - 7)//5
        y = 7*F + 17*G
        
    #class 2
    if i == 2:
        F, G = expand(2*m + 1)
        x = (13*F + 25*G - 7)//5
        y = 5*F + 13*G
        
    #class 5
    if i == 5:
        F, G = expand(2*m)
        F, G = -F, -G
        x = (-7*F - 5*G - 7)//5
        y = -1*F - 7*G
    
    #class 7
    if i == 7:
        F, G = expand(2*m )
        F, G = -F, -G
        x = (-7*F + 5*G - 7)//5
        y = F - 7*G
        
    #class 8
    if i == 8:
        F, G = expand(2*m + 1)
        x = (8*F + 10*G - 7)//5
        y = 2*F + 8*G
        
    #class 11
    if i == 11:
        F, G = expand(2*m + 1)
        F, G = -F, -G
        x = (-8*F + 10*G - 7)//5
        y = 2*F + -8*G
    
    return (x, y)

res_list = []
sol_count = 0
max_el = 0
todo = [0, 2, 5, 7, 8, 11]
m = 0
for m in range(15):
    for i in todo:
        flag = False
        new_el = solution_class(i, m)[0]
        if new_el <= 0:
            continue
        if new_el > max_el:
            if sol_count > 30:
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

print("Result =", sum(res_list[:30]))
print(datetime.now() - startTime)
print((timer()-start)*1000)
#time: 15ms
