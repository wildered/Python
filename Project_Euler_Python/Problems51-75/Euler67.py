# -*- coding: utf-8 -*-

bestand = open("p067_triangle.txt", 'r')

from datetime import datetime
startTime = datetime.now()
pyramid = []
for line in bestand:
    pyramid.append([int(c) for c in line.split()])

bestand.close()

counter = 0.
global fulldic

fulldic = {}
for k in range(len(pyramid)):
    tempdic = {}
    for i in range(k+1):
        tempdic[i] = 0
    fulldic[k] = tempdic
    
res = []

def maxPath(layer, place):
    global counter, fulldic, res
    counter += 1
    res.append(counter)
    node = pyramid[layer][place]
    if layer == len(pyramid)-1:
        return [node], node
    currentPath = [node]
    
    if fulldic[layer+1][place] == 0:
        leftPath, leftValue = maxPath(layer+1, place)
        fulldic[layer+1][place] = leftPath, leftValue
    else:
        leftPath, leftValue = fulldic[layer+1][place]
    if fulldic[layer+1][place+1] == 0:
        rightPath, rightValue = maxPath(layer+1, place+1)
        fulldic[layer+1][place+1] = rightPath, rightValue
    else:
        rightPath, rightValue = fulldic[layer+1][place+1]

    if leftValue >= rightValue:
        currentPath.extend(leftPath)
        resValue = leftValue + node
        return currentPath, resValue
    else:
        currentPath.extend(rightPath)
        resValue = rightValue + node
        return currentPath, resValue

maxPath, maxValue = maxPath(0, 0)

print "maximum route gives: " + str(maxValue)
print "answer made with " + str(counter) + " calls to the function"
print datetime.now() - startTime
#time 50ms






