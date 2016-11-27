# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 13:47:45 2016

@author: Home
"""

from datetime import datetime
#startTime = datetime.now()
#print datetime.now() - startTime

import graph_module_v2 as gm

def solve1():
    f = open("p083_matrix.txt", 'r')
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
    d[start][place(0,0)] = matrix[0][0]
    d[place(n-1, k-1)][eind] = 0
    
    #graph construction
    #inner rectangle
    for ridx in range(1,n-1):
        for cidx in range(1, k-1):
            d[place(ridx, cidx)][place(ridx, cidx+1)] = matrix[ridx][cidx+1]
            d[place(ridx, cidx)][place(ridx+1, cidx)] = matrix[ridx+1][cidx]
            d[place(ridx, cidx)][place(ridx, cidx-1)] = matrix[ridx][cidx-1]
            d[place(ridx, cidx)][place(ridx-1, cidx)] = matrix[ridx-1][cidx]
    #top row
    for col in range(1, k-1):       
        d[place(0, col)][place(0, col-1)] = matrix[0][col-1]
        d[place(0, col)][place(0, col+1)] = matrix[0][col+1]
        d[place(0, col)][place(1, col)] = matrix[1][col]
    d[place(0, 0)][place(0,1)] = matrix[0][1]
    d[place(0, 0)][place(1,0)] = matrix[1][0]
    d[place(0, k-1)][place(0, k-2)] = matrix[0][k-2]
    d[place(0, k-1)][place(1, k-1)] = matrix[1][k-1]
    
    #bottom row
    for col in range(1, k-1):       
        d[place(n-1, col)][place(n-1, col-1)] = matrix[n-1][col-1]
        d[place(n-1, col)][place(n-1, col+1)] = matrix[n-1][col+1]
        d[place(n-1, col)][place(n-2, col)] = matrix[n-2][col]
    d[place(n-1, 0)][place(n-1,1)] = matrix[n-1][1]
    d[place(n-1, 0)][place(n-2,0)] = matrix[n-2][0]
    d[place(n-1, k-1)][place(0, k-2)] = matrix[0][k-2]
    d[place(n-1, k-1)][place(n-2, k-1)] = matrix[n-2][k-1]
    
    #left and right column
    for row in range(1,n-1):
        d[place(row, 0)][place(row, 1)] = matrix[row][1]
        d[place(row, 0)][place(row-1, 0)] = matrix[row-1][0]
        d[place(row, 0)][place(row+1, 0)] = matrix[row+1][0]
        d[place(row, k-1)][place(row, k-2)] = matrix[row][k-2]
        d[place(row, k-1)][place(row-1, 0)] = matrix[row-1][0]
        d[place(row, k-1)][place(row+1, 0)] = matrix[row+1][0]
    
    g = gm.graph(d)
    print "Result = " + str(g.dijkstra(g.trans_d[start], g.trans_d[eind], True))


def solve2():
    """old solution"""
    f = open("p083_matrix.txt", 'r')
    matrix_bron = [map(int, row.split(",")) for row in f]
    f.close()  
    
    def dijkstra(matrix, start, eind):
        width = len(matrix[0])
        height = len(matrix)
    
        oneindig = float("inf")
        undiscovered = []
        for a in range(width):
            for b in range(height):
                undiscovered.append([a, b])
        min_dist = [[oneindig for k in range(width)] for l in range(height)]
        
        min_dist[start[0]][start[1]] = matrix[start[0]][start[1]]
        
        def dis(x,y):
            return min_dist[x][y]
        
        while len(undiscovered) > 0:
            min_row, min_col = -1, -1
            min_d = float("inf")
            for [x,y] in undiscovered:
                if min_dist[x][y] < min_d:
                    min_d = min_dist[x][y]
                    min_row, min_col = x, y
            undiscovered.remove([min_row, min_col])
            
            row, col = min_row, min_col
            a = (row, col)
            #left
            dist_u = min_dist[row][col]
            if col != 0:
                alt = dist_u + matrix[row][col-1]
                if alt < min_dist[row][col-1]:
                    min_dist[row][col-1] = alt
            #up
            if row != 0:
                alt = dist_u + matrix[row-1][col]
                if alt < min_dist[row-1][col]:
                    min_dist[row-1][col] = alt
            #right
            if col != width-1:
                alt = dist_u + matrix[row][col+1]
                if alt < min_dist[row][col+1]:
                    min_dist[row][col+1] = alt
            #down
            if row != height-1:
                alt = dist_u + matrix[row+1][col]
                if alt < min_dist[row+1][col]:
                    min_dist[row+1][col] = alt
        return min_dist
        
    min_arr = dijkstra(matrix_bron, [0,0], [len(matrix_bron)-1, len(matrix_bron[0])-1])
    print "minimum route = " + str(min_arr[len(matrix_bron)-1][len(matrix_bron[0])-1])

print "\nSolution 1"            #new solution
startTime = datetime.now()
solve1()
print datetime.now() - startTime
#time: 250ms

print "\nSolution 2"            #old solution
startTime = datetime.now()
solve2()
print datetime.now() - startTime
#time: 2.3s

    