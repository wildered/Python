# -*- coding: utf-8 -*-

from datetime import datetime
startTime = datetime.now()

res = []
def func(lst, done):
    temp = lst[::]
    for el in done:
        temp.remove(el)
    if len(temp) == 1:
        return temp
    else:
        res = []
        for n in temp:
            temp2 = done[::]
            temp2.append(n)
            for k in func(lst, temp2):
                res.append(str(n)+str(k))
    return res
        
i = 0
res = []
while True:
    res.extend(func([0,1,2,3,4,5,6,7,8,9], [i])) #set generated are sorted but missing first digit (i)
    if len(res) >= 1000000:
        break
    i += 1

print "result =",
print str(i) + str(res[999999])

print datetime.now()-startTime

#computation time on system: 9.1s 
