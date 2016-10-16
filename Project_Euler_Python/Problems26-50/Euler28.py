# -*- coding: utf-8 -*-

from datetime import datetime

start = datetime.now()
value = 1
res = 1

for extra in range(2,1001,2):   #width of sides excluding corners
    for i in range(4):          #4 numbers in square to add, each "extra" apart
        value += extra
        res += value

print res
print datetime.now()-start
