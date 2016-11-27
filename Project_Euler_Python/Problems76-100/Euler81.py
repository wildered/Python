# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 20:44:16 2016

@author: Home
"""
           
from datetime import datetime
#startTime = datetime.now()
#print datetime.now() - startTime

import graph_module_v2 as gm

def solve1():
    """Graph based solution"""
    f = open("p081_matrix.txt", 'r')
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
    n, k = len(matrix), len(matrix[0])
    
    d[start] = {}
    d[start][place(0,0)] = matrix[0][0]
    
    for row in range(n-1):      #making the graph
        for col in range(k-1):
            d[place(row, col)][place(row, col+1)] = matrix[row][col+1]
            d[place(row, col)][place(row+1, col)] = matrix[row+1][col]
        d[place(row, k-1)][place(row+1, k-1)] = matrix[row+1][k-1]
    for col in range(k-1):
        d[place(n-1, col)][place(n-1, col+1)] = matrix[n-1][col+1] 
    
    g = gm.graph(d)
    
    print "Result = " + str(g.dijkstra(g.trans_d[start], g.trans_d[place(n-1, k-1)], True))

def solve2():
    """Dynamic programming"""
    f = open("p081_matrix.txt", 'r')
    matrix = [map(int, row.split(",")) for row in f]        
    f.close()
    
    n, k = len(matrix), len(matrix[0])
    
    for col in range(k-2, -1, -1):
        matrix[n-1][col] += matrix[n-1][col+1]
    
    for row in range(n-2, -1, -1):
        matrix[row][k-1] += matrix[row+1][k-1]
        for col in range(k-2, -1, -1):
            matrix[row][col] += min(matrix[row+1][col], matrix[row][col+1])
    print "Result = " + str(matrix[0][0])    
    
    
print "\nSolution 1:"             #graph based
startTime = datetime.now()
solve1()
print datetime.now() - startTime
#time: 0.2s

print "\nSolution 2:"             #dynamic progrmaming
startTime = datetime.now()
solve2()
print datetime.now() - startTime
#5ms (2ms excluding file reading and matrix construction)

