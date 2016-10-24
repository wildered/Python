# -*- coding: utf-8 -*-

from datetime import datetime
startTime = datetime.now()
counter = 0
for power in range(1, 1000):
    for base in range(1, 20):
        number = base**power
        if len(str(number)) == power:
            counter += 1

print "answer: " + str(counter)
print datetime.now() - startTime
#time 500ms

