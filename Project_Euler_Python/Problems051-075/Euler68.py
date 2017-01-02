# -*- coding: utf-8 -*-

import copy
circle = [0 for i in range(10)]

from datetime import datetime
startTime = datetime.now()    

def fill(vorm, place):
    res = []
    over = [i for i in range(1, len(vorm)+1) if i not in vorm]
    if place == 5:
        for el in over:
            temp = copy.copy(vorm)
            temp[5] = el
            res.append(temp)
        return res
        
    if len([a for a in vorm if a != 0]) == 6:
        return vorm
        
    for n in over:
        temp = copy.copy(vorm)
        temp[place] = n
        res.extend(fill(temp, place+1))
    return res

def complete(vorm):
    vorm = copy.copy(vorm)
    total = vorm[0] + vorm[1] + vorm[2]
    over = [i for i in range(1, len(vorm)+1) if i not in vorm]
    n7 = total - vorm[2] - vorm[3]
    if n7 in over:
        vorm[6] = n7
        over.remove(n7)
        n8 = total - vorm[3] - vorm[4]
        if n8 in over:
            vorm[7] = n8
            over.remove(n8)
            n9 = total - vorm[4] - vorm[5]
            if n9 in over:
                vorm[8] = n9
                over.remove(n9)
                n10 = total - vorm[5] - vorm[1]
                if n10 in over:
                    vorm[9] = n10
                    return vorm
    
    return []        

def kenmerk(sol):
    res = ""
    res += str(sol[0]) + str(sol[1]) + str(sol[2])
    res += str(sol[6]) + str(sol[2]) + str(sol[3])
    res += str(sol[7]) + str(sol[3]) + str(sol[4])
    res += str(sol[8]) + str(sol[4]) + str(sol[5])
    res += str(sol[9]) + str(sol[5]) + str(sol[1])
    return int(res)
    
tempOut = []
out = []
for i in range(6, 6+1): #one with 6 is possible and therefore the maximum starts with 6
    vorm = copy.copy(circle)
    vorm[0] = i
    res = fill(vorm, 1)
    for potential_sol in res:
        full_sol = complete(potential_sol)
        if full_sol != []:
            if min(set([full_sol[0], full_sol[6], full_sol[7], full_sol[8], full_sol[9]])) == 6:
#                print set([full_sol[0], full_sol[6], full_sol[7], full_sol[8], full_sol[9]])
#                print full_sol
                tempOut.append(full_sol)
                n = kenmerk(full_sol)
                if len(str(n)) == 16:
                    out.append(n)

    

print "maximum = " + str(max(out))
print datetime.now() - startTime
#time 0.1s
