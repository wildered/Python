# -*- coding: utf-8 -*-
"""
Created on Sat Dec 03 12:00:07 2016

@author: Home
"""
"""
This solution works by finding the minimum value for an array
looking at only the non-1 elements, and adding these when using
the result.
"""
from math import log

from datetime import datetime
startTime = datetime.now()
fulldic = {}

max_n = 12000+100

def enter_dic(key, value):
    if key in fulldic:
        if value < fulldic[key]:
            fulldic[key] = value
    else:
        fulldic[key] = value

class r:
    
    def __init__(self, l):
        self.arr = l*[2]
        self.length = l
        self.prod = 2**l
        self.sum = 2*l
        
    def slow_prod(self):
        arr = self.arr
        res = 1
        for el in arr:
            res *= el
        return res
        
    def slow_sum(self):
        return sum(self.arr)
            
    def reset_arr(self, idx):
        stat = self.arr[idx]
        for i in range(idx+1, self.length):
            self.sum -= self.arr[i]
            self.sum += stat
            self.prod /= self.arr[i]
            self.prod *= stat
            self.arr[i] = stat
        
        
    def inc(self, idx):
        arr = self.arr
        self.prod = self.prod/arr[idx]*(arr[idx]+1)
        arr[idx] += 1
        self.sum += 1
        
    def __str__(self):
        res = ""
        res += "Arr = " + str(self.arr) + "\n"
        res += "Sum = " + str(self.sum) + "\n"
        res += "Prod = " + str(self.prod) + "\n"
        res += "Real sum = " + str(self.slow_sum()) + "\n"
        res += "Real prod = " + str(self.slow_prod()) 
        return res
        
    def defame(self, idx):
        if idx == self.length-1:
            temp_prod = self.prod
            while temp_prod < max_n:
                k = temp_prod - self.sum + self.length
                enter_dic(k, temp_prod)
                
                self.inc(idx)
                temp_prod = self.prod
        else:
            self.reset_arr(idx)
            temp_prod = self.prod
            while temp_prod < max_n:
                self.defame(idx+1)
                self.inc(idx)
                self.reset_arr(idx)
                temp_prod = self.prod
               
l = int(log(max_n, 2))

while l > 0:
    v = r(l)
    v.defame(0)
    l -= 1

del fulldic[1]

resSet = set([fulldic[key] for key in fulldic if key <= 12000])

print "result = " + str(sum(resSet))
print datetime.now() - startTime
#time: 0.24s


