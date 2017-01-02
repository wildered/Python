# -*- coding: utf-8 -*-

from datetime import datetime
startTime = datetime.now()

max_size = 100
max_n = 99

nArray = [1 for i in range(max_size+1)]
over = [walk for walk in range(2,max_n+1)]

#print nArray
oldArr = nArray
for n in over:
    idx = n
    while idx < max_size+1:
        nArray[idx] = nArray[idx] + nArray[idx-n]
        idx += 1


print "100 can be made in " + str(nArray[100]) + " ways"

print datetime.now() - startTime
#time: 2ms

