# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 12:50:51 2016

@author: Home
"""

import sys
sys.setrecursionlimit(10000)

from datetime import datetime
#startTime = datetime.now()
#print datetime.now() - startTime

import graph_module_v2 as gm

def solve1():
    f = open("p082_matrix.txt", 'r')
    matrix = [map(int, row.split(",")) for row in f]    
    f.close()
    
    d = {}
    m = max(len(matrix), len(matrix[0]))
    
    def place(a,b):
        return str(a) + "," + str(b)
    
    for a in range(m):
        for b in range(m):
            d[place(a,b)] = {}
    start = "s"
    eind = "e"
    n, k = len(matrix), len(matrix[0])
    
    d[start] = {}
    d[eind] = {}
    for row in range(n):
        d[start][place(row, 0)] = matrix[row][0]
        d[place(row, k-1)][eind] = 0
    
    for row in range(n-1):      #making the graph
        for col in range(k-1):
            d[place(row, col)][place(row, col+1)] = matrix[row][col+1]
            d[place(row, col)][place(row+1, col)] = matrix[row+1][col]
        d[place(row, k-1)][place(row+1, k-1)] = matrix[row+1][k-1]
    for col in range(k-1):
        d[place(n-1, col)][place(n-1, col+1)] = matrix[n-1][col+1] 
    for row in range(n-1, 0, -1):
        for col in range(k):
            d[place(row, col)][place(row-1, col)] = matrix[row-1][col]
    
    g = gm.graph(d)
    
    print "Result = " + str(g.dijkstra(g.trans_d[start], g.trans_d[eind], True))



def solve2():

    f = open("p082_matrix.txt", 'r')
    matrix = [map(int, row.split(",")) for row in f]
    for row in matrix:
        row.reverse()
    f.close()
    
    fulldic = {}
    for k1 in range(len(matrix)):
        temp = {}
        for k2 in range(len(matrix[0])):
            temp2 = {}
            temp2["up"] = -1
            temp2["right"] = -1
            temp2["down"] = -1
            temp[k2] = temp2
        fulldic[k1] = temp
    
    def minPath(row, col, last):
        cValue = matrix[row][col]
        if col == len(matrix[0])-1:
            return cValue
        
        upValue, rightValue, downValue = -1, -1, -1
                    
        if col != len(matrix[0])-1:
            if fulldic[row][col+1]["right"] != -1:
                rightValue = fulldic[row][col+1]["right"]
            else:
                rightValue = minPath(row, col+1, "right")
                fulldic[row][col+1]["right"] = rightValue
    
        if row != len(matrix)-1 and last != "up":
            if fulldic[row+1][col]["down"] != -1:
                downValue = fulldic[row+1][col]["down"]
            else:
                downValue = minPath(row+1, col, "down")
                fulldic[row+1][col]["down"] = downValue
    
        if row != 0  and last != "down":
            if fulldic[row-1][col]["up"] != -1:
                upValue = fulldic[row-1][col]["up"]
            else:
                upValue = minPath(row-1, col, "up")
                fulldic[row-1][col]["up"] = upValue
        
        min_value = min([v for v in [upValue, rightValue, downValue] if v != -1])
        resValue = min_value + cValue
        return resValue
    
    min_waard = minPath(0,0, "")
    
    for i in range(len(matrix)):
        waard = minPath(i,0, "")
        if waard < min_waard:
            min_waard = waard
        
    print "minimum route = " + str(min_waard)
    
print "\nSolution 1:"
startTime = datetime.now()
solve1()
print datetime.now() - startTime
#220ms

print "\nSolution 2:"
startTime = datetime.now()
solve2()
print datetime.now() - startTime
#time: 50ms

