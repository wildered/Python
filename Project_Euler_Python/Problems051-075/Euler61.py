# -*- coding: utf-8 -*-

import copy
from datetime import datetime
startTime = datetime.now()

Tris = []
Sqs = []
Pents = []
Hexs  = []
Heps = []
Octs = []

def func(form, lijst):
    n = 1-1
    while True:
        n += 1
        bij = eval(form)
        if bij < 1000:
            continue
        if bij >= 10000:
            break
        lijst.append(bij)
        

func("n*(n+1)/2", Tris)
func("n*n", Sqs)
func("n*(3*n-1)/2", Pents)
func("n*(2*n-1)", Hexs)
func("n*(5*n-3)/2", Heps)
func("n*(3*n-2)", Octs)

def findFollow(cijfer, lijst):
    res = [el for el in lijst if str(el)[:2] == str(cijfer)[2:]]
    return res
    
def findCycle(currentList, remainingLists):
    #if no lists remain the current is the output (full path)
    if remainingLists == []:
        return currentList
    #res is the final output of the function
    res = []
    #here we take a look at a specific path to extend
    for current in currentList:
        #currentu nmber in order to obtain last 2 digits
        nr = current[-1]
        #we take the path for each of the other lists
        for otherList in remainingLists:
            uit = []
            for newWay in findFollow(nr, otherList):
                newPath = copy.copy(current)
                newPath.append(newWay)
                uit.append(newPath)                
                
            overigLists = copy.copy(remainingLists)
            overigLists.remove(otherList)
            tijdelijk = findCycle(uit, overigLists)
            res.extend(tijdelijk)
            
    return res
                
for number in Tris:
    remaining = [Sqs, Pents, Hexs, Heps, Octs]
    current = [[number]]    
    answer = findCycle(current, remaining)
    for sol in answer:
        if len(sol) == 6:
            if str(sol[0])[:2] == str(sol[5])[2:]:
                print sol
                print "Result = " + str(sum(sol))
                stored = sol
                break

print datetime.now() - startTime
#time 140ms
