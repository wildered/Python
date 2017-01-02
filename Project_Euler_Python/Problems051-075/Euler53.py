# -*- coding: utf-8 -*-
from math import *
from eulerTools import *

from datetime import datetime
startTime = datetime.now()

counter = 0
for i in range(1, 100+1):
    for k in range(0, i+1):
        if nChoosek(i, k) > 1000000:
            counter += 1
            
print counter
print datetime.now() - startTime
#time 25ms
