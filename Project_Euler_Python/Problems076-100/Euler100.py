# -*- coding: utf-8 -*-
"""
Created on Thu Jan 05 12:28:28 2017

@author: Home
"""

"""See math appendix"""

from timeit import default_timer as timer
start = timer()

x, y = 1, 1
threshold = 2*10**12 - 1

while x <= threshold:
    x, y = 3*x + 4*y, 2*x + 3*y

print "Result = " + str((y+1)/2)
print timer()-start
#time: 40μs



