# -*- coding: utf-8 -*-

from datetime import datetime
startTime = datetime.now()

from math import log

term1 = 1
term2 = 1
newterm = 1+1
i = 2
#while len(str(term2)) < 1000:
while log(term2, 10) < 999:
    i += 1
    term1, term2 = term2, term1+term2

print "place =",
print i
print datetime.now()-startTime

#on system: 29ms










