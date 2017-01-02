# -*- coding: utf-8 -*-

from datetime import datetime
startTime = datetime.now()

m_out = 0
v_out = 0

for n in range(1, 1000):
    ares = []
    bres = []
    res = 10
    while res%n != 0:
        ares.append(res%n)
        res = 10*(res%n)
        if (res%n) in ares:
            val = len(ares)-ares.index(res%n)
            break
        
    if res%n == 0:
        continue
    if val >= m_out:
        m_out = val
        v_out = n

print "result =",
print v_out
print datetime.now() - startTime
#Measured computation time: 300ms


