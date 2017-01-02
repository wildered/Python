# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 22:21:01 2016

@author: Home
"""

"""
This is a graph-based approach. The graph consists of directed edges (a,b) if b comes later in the password than a. 
The goal is to find a path through the graph such that for every edge (a,b): there exists a (directed) (sub)path from 
a to b. Note that (a,b) is not necessarily used, as numbers can be inbetween.
The solution for the problem is the found path.
"""

from datetime import datetime
startTime = datetime.now()
#print datetime.now() - startTime

f = open("p079_keylog.txt", 'r')

bron = [line.replace("\n", "") for line in f]

d = {} #graph building
nodes = [str(i) for i in range(10)]
for i in nodes:
    d[i] = set()

for el in bron:
    for i in range(2):
        d[el[i]].add(el[i+1])

f.close()

#counters for improved performance
outcount = {}
incount = {}
for i in nodes:
    outcount[i] = len(d[i])
    incount[i] = 0

for i in nodes:
    for k in nodes:
        incount[i] += (i in d[k])

over = sum([outcount[i] + incount[i] for i in nodes])/2    

start2 = min(nodes, key= lambda x: incount[x]) #could be done with a custom cmp, but it's at most 2-layered. 
start = max([node for node in nodes if incount[node] == incount[start2]], key = lambda x : outcount[x])
s = start

curr = start
new_node = start

while over > 0:
    if len([el for el in d[new_node] if el != new_node]) != 0: #in case an outgoing vector exists
        new_node2 = min([el for el in d[new_node] if el != new_node], key = lambda x: incount[x])
        new_node = max([el for el in d[new_node] if el != new_node and incount[el] == incount[new_node2]], key = lambda x: outcount[x])
    elif len(d[new_node]) != 0: #loop back to current
        new_node = new_node
    else: #if no outgoing vectors, choose new continuing starting point
        new_node2 = min(nodes, key= lambda x: incount[x])
        start = max([node for node in nodes if incount[node] == incount[new_node2]], key = lambda x : outcount[x])
    
    if incount[new_node] + outcount[new_node] == 0:
        break
    for old in s:
        if new_node in d[old]:
            d[old].remove(new_node)
            incount[new_node] -= 1
            outcount[old] -= 1
            over -= 1
    s += new_node
    
print "Result = " + str(s)

print datetime.now() - startTime
#time 1ms


