# -*- coding: utf-8 -*-
from datetime import datetime

start = datetime.now()
         
res = set([pow(a,b) for a in range(2, 101) for b in range(2, 101)])
         
print len(res)
print datetime.now()-start
#computation time: 15ms

