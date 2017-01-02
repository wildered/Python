# -*- coding: utf-8 -*-

from datetime import datetime
startTime = datetime.now()

n = 1000
res = 0
cut = 10**10
for i in range(1,n+1):
    res = (res + i**i)%cut

print res%cut
print datetime.now() - startTime
#time 0.1s
