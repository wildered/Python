# -*- coding: utf-8 -*-

from datetime import datetime
startTime = datetime.now()

f = open("p022_names.txt", 'r')
fullread = f.read()
f.close()

def score(name):
    temp = 0
    name = name.lower()
    for letter in name:
        temp += ord(letter)
    temp += len(name)*(-ord("a") + 1) #saves computing time doing it outside the loop
    return temp



names = []
for name in eval(fullread):
    names.append(name)
    
names.sort()

sumscore = 0
for place, name in enumerate(names):
    sumscore += (place+1)*score(name)


print sumscore

print datetime.now()-startTime

#creator system: 40ms





