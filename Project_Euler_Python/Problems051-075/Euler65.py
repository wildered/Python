# -*- coding: utf-8 -*-

from datetime import datetime
startTime = datetime.now()

def numGen(idx):
    if idx == 0:
        return 2
    else:
        if (idx-2)%3 == 0:
            return (idx+1)/3*2
        else:
            return 1

def stap(n, max_n):
    if n == max_n:
        return (1,numGen(n+1))
    a,b = stap(n+1, max_n)
    return (b, numGen(n+1)*b+a)
    
def numberAt(pos):
    if pos == 0:
        return (numGen(0), 1)
    pos -= 1
    a,b = stap(0, pos)
    return (a+numGen(0)*b,b)

a, b = numberAt(99)
print str(a) + " / " +  str(b)
res = 0
for c in str(a):
    res += int(c)
    
print "digital sum = " + str(res)

print datetime.now() - startTime
#time <1ms


