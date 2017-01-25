# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 21:07:48 2017

@author: Home
"""

"""
The solution is structured as follows:
Firstly we sort the set and check the 2nd property. By sorting it
we only have to check if the first thus smallest n elements is 
larger than the last thus largest n-1 elements. Now any other 
combination follows trivially, and this greatly reduces the amount 
of combinations to check. The second property is checked by finding
the sum of every subset (using decimal int -> binary int). Clearly
we only have to check half and if the sum%2 == 0, if half it is a 
subset sum. """


from datetime import datetime
startTime = datetime.now()

verz_all = []

f = open('p105_sets.txt', 'r')

for placeholder in f:
    words = placeholder.replace("\n", "").split(",")
    numbers = [int(word) for word in words]
    numbers.sort()
    verz_all.append(numbers)

f.close()

d = {}
def binGen(n):
    if n in d:
        return d[n]
        
    res = []
    for i in xrange(2**(len(verz))):
        res.append(str(bin(i))[2:])
    d[n] = res
    
    return res


def subsetCheck(verz):
    stored = []
    kaarten = binGen(len(verz) - 1) 
    for conf in kaarten:
        temp = 0
        for idx in xrange(1, len(conf) + 1):
            if conf[-idx] == '1':
                temp += verz[-idx]
        stored.append(temp)
    
    if len(verz)%2 == 0 and len(verz)/2 in stored:
        return False
    return (len(set(stored)) == len(stored))

def check(verz):
    eind = (len(verz) + 1)/2 + 1
    for i in xrange(2, eind):
        if sum(verz[:i]) <= sum(verz[-(i-1):]):
            return False
    return subsetCheck(verz)

resSum = 0
for verz in verz_all:
    if check(verz):
        resSum += sum(verz)
        
print "resulting sum = " + str(resSum)
print datetime.now() - startTime
#time: 160ms
