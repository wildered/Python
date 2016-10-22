# -*- coding: utf-8 -*-
from datetime import datetime as dt
q = dt.now()
suits = ['C', 'D', 'H', 'S']

def value(deck):
    nrs = [el[0] for el in deck]
    #royalflush
    for i in xrange(len(suits)):
        if [10,suits[i]] in deck and [11,suits[i]] in deck and \
        [12,suits[i]] in deck and [13,suits[i]] in deck and \
        [14,suits[i]] in deck:
            return 10, nrs
    
    #straight
    if min(deck)[0] <= 10:
        low = min(deck)[0]    
        
        if low in nrs and low+1 in nrs and low+2 in nrs and \
        low+3 in nrs and low+4 in nrs :
            if len(set([el[1] for el in deck])) == 1:
                return 9, nrs
            
    for getal in nrs:
        counter = 0
        for i in xrange(len(nrs)):
            if nrs[i] == getal:
                counter += 1
        if counter == 4:
            return 8, 4*[getal]
        if counter == 3:
            others = [x for x in nrs if x != getal]
            if others == [others[0]]*2:
                temp = 3*[getal]
                temp.extend(2*[others[0]])
                return 7, temp
             
    if len(set([el[1] for el in deck])) == 1:
        return 6, nrs
    
    if min(deck)[0] <= 10:
        low = min(deck)[0]
        
        if low in nrs and low+1 in nrs and low+2 in nrs and \
        low+3 in nrs and low+4 in nrs :
            return 5, nrs
    
    for getal in nrs:
        counter = 0
        for i in xrange(len(nrs)):
            if nrs[i] == getal:
                counter += 1
        if counter == 3:
            return 4, 3*[getal]
        if counter == 2:
            others = [x for x in nrs if x != getal]
            if len(set(others)) == 2:
                others.sort()
                res = 2*[getal]
                temp = [2*others[1]]
                res.extend(temp)
                return 3, res
            
            return 2, 2*[getal]
    
    return 1, max(nrs)
                        
def winner(deck1, deck2):
    if value(deck1) > value(deck2):
        return 1
        
    if value(deck1) < value(deck2):
        return 2  
    a1, b1 = value(deck1)
    a2, b2 = value(deck2)
    while len(b1) != 0:
        if max(b1) > max(b2):
            return 1
        if max(b1) < max(b2):
            return 2
        b1.remove(max(b1))
        b2.remove(max(b2))
        
translate = {}
for j in xrange(2, 11):
    translate[str(j)] = j
translate['T'] = 10
translate['J'] = 11
translate['Q'] = 12
translate['K'] = 13
translate['A'] = 14

def trans(words):
    words = words.split()
    p1cards = []
    p2cards = []
    p1cards.extend(words[0:5])
    p2cards.extend(words[5::])
    for idx in xrange(5):
        old1 = p1cards[idx]
        old2 = p2cards[idx]
        new1 = [translate[old1[0]], old1[1]]
        new2 = [translate[old2[0]], old2[1]]
        p1cards[idx] = new1
        p2cards[idx] = new2
    return p1cards, p2cards

lijst = file("p054_poker.txt", 'r')

counter = 0
for line in lijst:
    words = line.replace("\n", "")
    p1cards, p2cards = trans(words)
    if winner(p1cards, p2cards) == 1:
        counter += 1

print counter
print dt.now()-q
#time 50ms

lijst.close()




