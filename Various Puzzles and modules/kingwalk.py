# -*- coding: utf-8 -*-
"""
This is a solution to a puzzle which goes as follows:
Let there be an N x N chessboard, and a single king on (x0, y0). In how many ways
can the king move to (x1, y1) in the minimum number of moves possible? (remember that the
king can move omnidirectional but only 1 square)
"""

from datetime import datetime
def solve(startx, starty, endx, endy, N):
    """First the problem is translated into one where x-difference exceeds (or equals)
    y-difference. Then we iterate over the x coordinates and sum the amount of paths possible
    to connected squares from a square and assign it that value."""
    startx, starty, endx, endy = startx-1, starty-1, endx-1, endy-1
    if startx > endx:
        endx, startx = startx, endx
    if starty>  endy:
        endy, starty = starty, endy
    if (endy-starty) > (endx-startx):
        startx, starty = starty, startx
        endx, endy = endy, endx
    
    if (endx - startx) == (endy-starty):
        return 1
        
    a = endx-startx
    b = endy-starty
    
    d = {}
    d[starty] = 1
    min_i = starty
    max_i = starty
    n = a
    
    for i in range(a):
        d_new = {}
        
        for k in range(max(0, min_i-1, endy-(n-i+1)), min(N-1, max_i +1, endy+(n-i+1))+1):
            res = 0
            for other in [-1, 0, 1]:
                if k+other in d:
                    res += d[k+other]
            d_new[k] = res%5318008
        min_i = max(0, min_i-1, endy-(n-i+1))
        max_i = min(N-1, max_i +1, endy+(n-i+1))
        d = d_new
    
    return d[endy]%5318008
    
n = 3770
sx, sy, ex, ey = 2993, 524, 2598, 1656
#expected: 5086736

q = datetime.now()
print solve(sx, sy, ex, ey, n)
print datetime.now()-q
