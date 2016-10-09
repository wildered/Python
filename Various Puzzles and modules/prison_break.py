# -*- coding: utf-8 -*-

"""This script solves the following problem:
Let there be n guards in a n x m square, where for 1 <= i <= n:
x_i, y_i, r_i denote the location and sight radius of guard i. The algorithm solves if there is a 
route possible from (0,0) to (n,m) without being seen by guards.
Uses graph module
"""

import graph_module as g
from math import sqrt
from datetime import datetime
startTime = datetime.now()

def solve(width, height, guard_count, guards):
    counter = 0
    gs = []
    left = []
    right = []
    upper = []
    lower = []
    t_dic = {}
    for guard in guards:
        [x,y, r] = guard
        node = g.node(counter)
        node.att = [x,y, r]
        t_dic[counter] = node
        gs.append(node)
        if x-r <= 0:
            left.append(node)
        if x+r >= width:
            right.append(node)
        if y-r <= 0:
            lower.append(node)
        if y+r >= height:
            upper.append(node)
        counter += 1
        
    for g1 in gs:
        for g2 in gs:
            if g1 == g2:
                continue
            [x1,y1 ,r1] = g1.att
            [x2,y2, r2] = g2.att
            if (r1+r2) >= sqrt((x2-x1)**2 + (y2-y1)**2):
                new_e = g.edge(g1, g2, 1)
                g1.add_edge(new_e)
    
    #find from left to lower or right, after that from lower to upper
    Q = [guart_t for guart_t in left]
    done = []
    while len(Q) > 0:
        el = Q.pop()
        if (el in right) or (el in lower):
            return "Escape NOT possible"
        done.append(el)
        for other in el.connected():
            if (other not in Q) and (other not in done):
                Q.append(other)
    Q = [guart_t for guart_t in lower]
    done = []
    while len(Q) > 0:
        el = Q.pop()
        if (el in upper):
            return "Escape NOT possible"
        done.append(el)
        for other in el.connected():
            if (other not in Q) and (other not in done):
                Q.append(other)
            
    return "Escape possible"

if __name__ == "__main__":
    #example case:
    width = 5
    height = 5
    guard_count = 3
    guard_properties = []
    guard_properties.append([3,1,2])    #[x,y, r]
    guard_properties.append([3,5,1])
    guard_properties.append([1,4,1])
    
    #expected output: escape possible
    print "(Expected: possible)"
    print solve(width, height, guard_count, guard_properties)
    print
    
    width = 5
    height = 5
    guard_count = 3
    guard_properties = []
    guard_properties.append([3,1,2])    #[x,y, r]
    guard_properties.append([3,4,1])
    guard_properties.append([1,4,1])
    
    #expected output: escape possible
    print "(Expected: NOT possible)"
    print solve(width, height, guard_count, guard_properties)
    print
    
    print datetime.now() - startTime

    #simple case computation time: 30μs
