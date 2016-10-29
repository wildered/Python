# -*- coding: utf-8 -*-

from datetime import datetime
startTime = datetime.now()

from eulerTools import gcd


a_close = 0
b_close = 1
diff_close = (3*b_close-7*a_close, 7*b_close)
for b in range(1000000, 0, -1):
    if b%7 == 0:
        continue
    a = int(float(3*b)/7)
    if diff_close[0]*b*7 < diff_close[1]:
        break
    if (3*b-7*a)*diff_close[1] < 7*b*diff_close[0]:
        a_close = a
        b_close = b
        diff_close = (3*b-7*a, 7*b)

commonF = gcd(a_close, b_close)

print "Left fraction = " + str(a_close/commonF) + " / " + str(b_close/commonF)
    
print datetime.now() - startTime
#time 0.2s

