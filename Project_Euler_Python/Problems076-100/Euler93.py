# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 22:25:07 2016

@author: Home
"""

# -*- coding: utf-8 -*-
from datetime import datetime
startTime = datetime.now()

import copy
possibles = ["+", "-", "*", "/"]

def perm(lst):
    """permutes items in a list"""
    res = []
    if len(lst) == 1:
        return [lst]
    for dig in lst:
        temp = copy.copy(lst)
        temp.remove(dig)
        
        for partial in perm(temp):
            partial.append(dig)
            res.append(partial)
    return res
        

"""There are several equivalent combinations. e.g: a - (b - c)
= a - b + c. In order to reduce these (by a factor ~6)
we use sets and store the operations. Also use of large values 
to prevent number-dependent equivalencies."""
a, b, c, d = 3.0, 17.0, 113.0, 2537.0
perms_ch = perm(["a", "b", "c", "d"])
tempSet = set()
combinations = []
for op1 in possibles:
    for op2 in possibles:
        for op3 in possibles:
            for lst in perms_ch:           
                """Althought the elegance of this questionable, it
                was the fastest of all implementations I made, and 
                supringly the shortest. Keep in mind that
                order 1, 3, 2 <=> 2, 3, 1"""
                
                [a_ch, b_ch, c_ch, d_ch] = lst
                data = [a_ch, op1, b_ch, op2, c_ch, op3, d_ch]
                exec( "f1 = lambda a, b, c, d: " \
                    + "(( {} {} {} ) {} {} ) {} {}".format(*data) )
                exec( "f2 = lambda a, b, c, d: " \
                    + "( {} {} {} ) {} ( {} {} {})".format(*data) )
                exec( "f3 = lambda a, b, c, d: " \
                    + "( {} {} ( {} {} {} )) {} {}".format(*data) )
                exec( "f4 = lambda a, b, c, d: " \
                    + "{} {} (( {} {} {} ) {} {} )".format(*data) )
                exec( "f5 = lambda a, b, c, d: " \
                    + "{} {} ( {} {} ( {} {} {} ))".format(*data) )
                for f in [f1, f2, f3, f4, f5]:
                    val = f(a, b, c, d)
                    if  val not in tempSet:
                        tempSet.add(val)
                        combinations.append(f)
                        

def expr(digits):
    """Tries all combinations and returns an ordered set"""
    resSet = set()
    [a,b,c,d] = digits
    for f in combinations:
        try:                        #division by zero
            resSet.add(f(a,b,c,d))
        except:
            pass
    return resSet


def cons(arr):
    """Looks for a longer consequtive sequence"""
    global high
    if high not in arr:
        return 0
    idx = 0
    while (idx+1) in arr:
        idx += 1
    return idx


high = 0
stored = None

for a in range(0,6+1):
    at = float(a)
    for b in range(a+1, 7+1):
        for c in range(b+1, 8+1):
            for d in range(c+1, 9+1):
                digits = [float(a), float(b), float(c), float(d)]
                count = cons(expr(digits))
                if count > high:
                    high = count
                    stored = [a,b,c,d]
                    
                    
print "result = " + "".join(map(str, stored))        
print datetime.now() - startTime
#time: 0.31s

