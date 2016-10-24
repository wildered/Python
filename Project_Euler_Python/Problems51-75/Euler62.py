# -*- coding: utf-8 -*-

from datetime import datetime
startTime = datetime.now()

cubes = [i*i*i for i in range(1,10000)]

cubeDic = {}
for number in cubes:
    tempDic = {}
    for c in str(number):
        tempDic[c] = 0
    for c in str(number):
        tempDic[c] += 1
    cubeDic[number] = tempDic

#print "At step 2"
for getal in cubeDic:
#    print getal
    mark = cubeDic[getal]
    counter = 0
    
    for other in cubeDic:
        if cubeDic[other] == cubeDic[getal]:
            counter += 1
    if counter == 5:
        verz = []
        res = "The 5 are: "
        for other in cubeDic:
            if cubeDic[other] == cubeDic[getal]:
                verz.append(other)
        verz.sort()
        
        for opl in verz:
            res += str(opl) + " , "
            
        print res[:-3]
        print "Minimal =",
        print(min(verz))
#        print "Oplossing = " + str(getal)
        break

print datetime.now() - startTime
print "done"
#time 400ms

