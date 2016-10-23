# -*- coding: utf-8 -*-
"""
This is a solution to the following problem:
We want to find a hidden point in Z^2 (thus integergrid)
We have the following data: m points in space and for each their taxicab (L^1-norm)
to the hidden point. The goal is to give the point if it's unique, or conclude whether
none exist or more than 1 exist.
"""

from datetime import datetime
q = datetime.now()

N = 3
arr = []
arr.append([999999,0,1000])
arr.append([999900, 950, 451])
arr.append([987654, 123, 13222])

def intersect(line1, line2):
    xleft1, xright1, c1, b1 = line1
    xleft2, xright2, c2, b2 = line2
    
    other = []
    if xleft1 > xright2 or xright1 < xleft2:
        return "empty", other
    if xleft1 == xright2:
        if c1*xleft1 + b1 == c2*xright2 + b2:
            return "point", [xleft1, c1*xleft1 + b1]
        else:
            return "empty", other
    if xleft2 == xright1:
        if c2*xleft2 + b2 == c1*xright1 + b1:
            return "point", [xleft2, c2*xleft2 + b2]
        else:
            return "empty", other
    if c1 == c2:
        if b1 != b2:
            return "empty", other
        else:
            return "line", [max(xleft1, xleft2), min(xright1, xright2), c1, b1]
    else:
        new_l = max(xleft1, xleft2)
        new_r = min(xright1, xright2)
        if (b1-b2)%(c2-c1) == 0:
            xpoint = (b1-b2)/(c2-c1)
            if new_l <= xpoint <= new_r:
                return "point", [xpoint, xpoint*c1 + b1]
        return "empty", other
        

idx = 0
current = arr[idx]
a,b, r=  current
idx += 1

lines = []
#upperleft line
#format [leftx, rightx, (y=)cx, +d]
lines.append([a-r, a, 1, b-a+r])
#lowerleft
lines.append([a-r, a, -1, b+a-r])
#lowerright
lines.append([a, a+r, 1, b-a-r])
#upper right
lines.append([a, a+r, -1, b+a+r])

points = []

while idx < len(arr):
    new_points = []
    new_lines = []
    invest = arr[idx]
    ta, tb, tr = invest
    idx += 1
    inv_lines = []
    inv_lines.append([ta-tr, ta, 1, tb-ta+tr])
    inv_lines.append([ta-tr, ta, -1, tb+ta-tr])
    inv_lines.append([ta, ta+tr, 1, tb-ta-tr])
    inv_lines.append([ta, ta+tr, -1, tb+ta+tr])
    
    for line in lines:
        for line2 in inv_lines:
            dec, res = intersect(line, line2)
            if dec == "empty":
                continue
            elif dec == "point":
                if res not in new_points:
                    new_points.append(res)
            else:
                if res not in new_lines:
                    new_lines.append(res)
    
    for point in points:
        if abs((point[0]-ta) + abs(point[1]-tb)) == tr:
            if point not in new_points:
                new_points.append(point)
            
    lines = new_lines
    points = new_points
        
    
if (len(lines) >= 1) or (len(points) >= 2):
    print "uncertain"
elif len(points) == 1:
    print str(points[0][0]) + " " + str(points[0][1])
else:
    print "impossible"

print datetime.now()-q


