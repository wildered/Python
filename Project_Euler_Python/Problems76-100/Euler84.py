# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 17:04:08 2016

@author: Home
"""

from datetime import datetime
import random
ogen = 4
perms = ogen**2
p_jail = 1.0/(pow(ogen, 4))
cc_p = 1.0/16
ch_p = 1.0/16


def solve1():
    
    def p_func(n):
        return max(0, float(ogen - abs(n-(ogen+1)))/perms)
    
    p = [p_func(i) for i in range(2*ogen+1)]
    
    boord_l = 40    
    distribution = [[float(1)/boord_l, 0] for i in range(boord_l)]
    distribution[30][0] = 0
    distribution[10][0] += float(1)/boord_l
    
    def nextR(n):
        if n >= 36 or n <= 5:
            return 5
        elif 6 <= n <= 15:
            return 15
        elif 16 <= n <= 25:
            return 25
        else:
            return 35
    
    def nextU(n):
        if n >= 29 or n <= 12:
            return 12
        else:
            return 28
    
    def add(arr, slot, amount):
        frac_left = 1.0
        
        if slot == 30:
             arr[10][1] += amount
             return
        
        arr[10][1] += amount*p_jail     #triple double -> jail
        frac_left -= p_jail             #perhaps not entirely accurate
                                        #odd number will never be double        
        if slot in [2, 17, 33]:
            arr[0][1] += cc_p*amount            #go to go
            frac_left -= cc_p
            arr[10][1] += cc_p*amount           #go to jail
            frac_left -= cc_p
            arr[slot][1] += frac_left*amount
        elif slot in [7, 22, 36]:
            arr[0][1] += ch_p*amount            #go to go
            arr[10][1] += ch_p*amount           #go to jail
            arr[11][1] += ch_p*amount  
            arr[24][1] += ch_p*amount  
            arr[39][1] += ch_p*amount  
            arr[5][1] += ch_p*amount  
            arr[nextR(slot)][1] += 2*ch_p*amount  
            arr[nextU(slot)][1] += ch_p*amount  
            arr[(slot-3)%boord_l][1] += ch_p*amount  
            frac_left -= 9*ch_p
            arr[slot][1] += frac_left*amount
        else:
            arr[slot][1] += frac_left*amount
            
    for i in xrange(100):
#        h_s = 0.0
        #with Markov chain convergence rates this could probably be stopped ealier
        for idx in range(boord_l):
            cell = distribution[idx]
            for walk in range(2*1, 2*ogen+1):
                add(distribution, (idx+walk)%boord_l, cell[0]*p[walk])
        
        for i in range(boord_l):
#            if abs(distribution[i][1] - distribution[i][0]) > h_s:
#                h_s = abs(distribution[i][1] - distribution[i][0])
            distribution[i][0], distribution[i][1] = distribution[i][1], 0
        
    def conv(n):
        return "0"*(2-len(str(n))) + str(n)
    
    lst = [[distribution[i][0], i] for i in range(len(distribution))]
    lst.sort(key= lambda x: -x[0])
    print "result = " + "".join([conv(idx) for [v, idx] in lst[:3]])
    
    
def solve2():
    boord = ["GO", "A1", "CC", "A2", "T1", "R", "B1", "CH", "B2", "B3", "jail", "C1", "U", "C2", "C3", "R", "D1", "CC", "D2", "D3", "FP", 
    "E1", "CH", "E2", "E3", "R", "F1", "F2", "U",
             "F3", "goJail", "G1", "G2", "CC", "G3", "R", "CH", "H1", "T2", "H2"]
    
    C_chest = ["togo", "JAIL", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    random.shuffle(C_chest)
    Chance = ["togo", "JAIL", "C1", "E3", "H2", "R1","nextR", "nextR", "nextU", "back3", "", "", "", "", "", ""]
    random.shuffle(Chance)
    
    boord_lengte = len(boord)
    #jail idx = 
    global chest_idx, chance_idx
    
    chest_idx = 0
    chance_idx = 0
    
    chest_idx = -1
    def C_chestPop():
        global chest_idx
        chest_idx = (chest_idx+1)%len(C_chest)
        return C_chest[chest_idx]
    
    chance_idx = -1
    def ChancePop():
        global chance_idx
        chance_idx = (chance_idx+1)%len(Chance)
        return Chance[chance_idx]
    
    def action(place):
        plaats = boord[place]
        if plaats == "goJail":
            return 10
        if plaats == "CC":
            kaart = C_chestPop()
            if kaart == "togo":
                return 0
            if kaart == "JAIL":
                return 10
        if plaats == "CH":
            kaart = ChancePop()
            if kaart == "togo":
                return 0
            if kaart == "JAIL":
                return 10
            if kaart == "C1":
                return 11
            if kaart == "E3":
                return 24
            if kaart == "H2":
                return 39
            if kaart == "R1":
                return 5
            if kaart == "nextR":
                i = place
                while boord[i] != "R":
                    i = (i+1)%len(boord)
                return i
            if kaart == "nextU":
                j = place
                while boord[j] != "R":
                    j = (j+1)%len(boord)
                return j
            if kaart == "back3":
                return action(place-3)
            
        return place
                
    def step(place):
        counter = 0
        while counter < 3:
            a = random.randint(1, ogen)
            b = random.randint(1, ogen)
            place = (place+a+b)%boord_lengte
            place = action(place)
            if a != b:
                break
            counter += 1
        
        if counter == 3:
            place = 10
            
        return place
        
    freq = [0 for i in range(len(boord))]
    
    plek = 0
    for i in range(100000):
        plek = step(plek)
        freq[plek] += 1
        
    #backupF = copy.deepcopy(freq)
    def conv(n):
        return "0"*(2-len(str(n))) + str(n)
    
    lst = [[-freq[idx], idx] for idx in range(len(freq))]
    lst.sort()
#    print lst[:3]
    
    print "result = " + "".join([conv(idx) for [v, idx] in lst[:3]])

"""Although accuracy is still dependent on number of steps done, 
   this algorithm is completely deterministic, allowing for a lower
   lower bound to be chosen (100 (20 is enough in this case) vs
   10000 for solution 2, and is non-deterministic)."""
   
print "\nSolution 1: "
startTime = datetime.now()
solve1()       
print datetime.now() - startTime
#time: 34ms


"""Not 100% reliable.
   Old solution."""
   
print "\nSolution 2: "
startTime = datetime.now()
solve2()       
print datetime.now() - startTime
#time: 510ms

"""Special note: at current monte-carlo simulation length, the
old solution (solution 2) gives various answer, most of which wrong,
whilst the new solution (solution 1) gives the correct one (with chance
1 as it is deterministic)
"""


