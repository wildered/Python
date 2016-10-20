# -*- coding: utf-8 -*-

from datetime import datetime
q = datetime.now()

goal = 200
subs = [1, 2, 5, 10, 20, 50, 100, 200]
possible = [1] + [0]*goal

for sub in subs:
    for i in range(sub, goal+1):
        possible[i] += possible[i-sub]

print "res =", possible[goal]
print datetime.now()-q

#14ms
