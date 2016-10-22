# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 23:49:24 2016

@author: Home
"""

#manual labour doen
from datetime import datetime
startTime = datetime.now()

lijst = file("p059_cipher.txt", 'r')

line = lijst.read()
numbers = line.split(',')

def decode(key):
    i = 0
    res = ""
    for n in numbers:
        newC = chr(int(n)^ord(key[i]))
        res += newC
        i = (i+1)%len(key)
        
    print res
    return res

a = 103
b = 111
c = 100

key = chr(a) + chr(b) + chr(c)
res = decode(key)
        
print "done"

lijst.close()
print datetime.now() - startTime
#time 4ms...


