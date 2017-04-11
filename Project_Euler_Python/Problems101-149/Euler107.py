# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 17:27:36 2016

@author: Home
"""
"""Kruskal's algorithm. """

from datetime import datetime
startTime = datetime.now()

arcs_t = {}
cloud_g = {}
old = 0

f = open('p107_network.txt', 'r')
idx = 0

for l in range(1,1000+1):
    arcs_t[l] = []

for placeholder in f:
    cloud_g[idx] = idx
    line = placeholder.replace("\n", "")
    weights = line.split(",")
    for k in range(len(weights)):
        if weights[k] != '-':
            weights[k] = int(weights[k])
    temp = []
    for bdx in range(idx+1, len(weights)):
        if weights[bdx] != '-':
            arcs_t[weights[bdx]].append([idx, bdx])
            old += weights[bdx]
    idx += 1
    
f.close()

dic_keys = list(arcs_t.keys())

for key_l in dic_keys:
    if arcs_t[key_l] == []:
        del arcs_t[key_l]

lengtes = list(arcs_t.keys())
lengtes.sort()


def Kruskal(info, arcs, cloud):
    resSum = 0
    count = len(cloud)-1
    walk = 0
    while count > 0:
        while(arcs[info[walk]]) == []:
            walk += 1
        length = info[walk]
        pair = arcs[length][0]
        a, b = pair
        if cloud[a] != cloud[b]:
            old_b = cloud[b]
            new_b = cloud[a]
            for i in range(len(cloud)):
                if cloud[i] == old_b:
                    cloud[i] = new_b
            
            resSum += length
            count -= 1
        del arcs[info[walk]][0]
        
        if arcs[info[walk]] == []:
            del arcs[info[walk]]
            del info[walk]

    return resSum

res = Kruskal(lengtes, arcs_t, cloud_g)

print("amount saved = " + str(old-res))
print(datetime.now() - startTime)


