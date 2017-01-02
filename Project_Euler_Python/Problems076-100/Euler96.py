# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 10:16:03 2016

@author: Home
"""

"""The solution is divided into 2 parts: the (always successful) 
backtracking implementation, and the (not always successful) logical
solver. The logical solver tries to fill as much squares as possible 
with logic, 
"""

import numpy as np
from datetime import datetime
startTime = datetime.now()

numbers = range(9)

#opening the file and reading the sudokus
res_all = []
counter = 0

f = open('p096_sudoku.txt', 'r')
for el in f:
    if counter == 0:
        sud_temp = np.array(np.zeros([9,9], dtype = int))
        counter = (counter+1)%10
        continue
    
    line = el.replace("\n", "")
    sud_temp[counter-1] = map(int, list(line))
    if counter == 9:
        res_all.append(sud_temp)
    
    counter = (counter+1)%10
f.close()

sqndic = {} #The squares from top to bottom from left to right 1-9
for x in numbers:
    top = x/3
    sqndic[x] = {}
    for y in numbers:
        left = y/3
        sqn = 3*top + left
        sqndic[x][y] = sqn


def solve_bt(sudoku, startx, starty, rowdic, coldic, sqdic, potDic):
    """This is the backtracking solution. 
    """
    x, y = startx, starty
    while x < 9 and sudoku[x, y] != 0:
        if y == 8:
            x += 1
            y = 0
        else:
            y += 1
    if x == 9:
        return True, sudoku
    
    for i in potDic[x][y]:
        if i in rowdic[x]:
            continue
        if i in coldic[y]:
            continue
        sqn = sqndic[x][y]
        if i in sqdic[sqn]:
            continue
        sudoku[x, y] = i
        rowdic[x].add(i)
        coldic[y].add(i)
        sqdic[sqn].add(i)
        
        flag, sol = solve_bt(sudoku, x, y, rowdic, coldic, sqdic, potDic)
        if flag:
            return True, sol
        rowdic[x].remove(i)
        coldic[y].remove(i)
        sqdic[sqn].remove(i)
    sudoku[x, y] = 0
    return False, []

values = range(1, 10)
def backtrack_solve(sud, potDic):
    """First a dictionary of sets is created to store row, column
    and square information. """
    rowdic, coldic, sqdic = {}, {}, {}
    for x in numbers:
        rowdic[x] = set()
        coldic[x] = set()
        sqdic[x]  = set()
        
    for row in numbers:
        for col in numbers:
            rowdic[row].add(sud[row, col])
            coldic[col].add(sud[row, col])
    
    for x in numbers:
        top  = (x/3)*3
        left = (x%3)*3
        for row in [top, top+1, top+2]:
            for col in [left, left+1, left+2]:
                sqdic[x].add(sud[row, col])
        
    for x in numbers:
        if 0 in rowdic[x]:
            rowdic[x].remove(0)
        if 0 in coldic[x]:
            coldic[x].remove(0)
        if 0 in sqdic[x]:
            sqdic[x].remove(0)
    
    flag, sol = solve_bt(sud, 0, 0, rowdic, coldic, sqdic, potDic)
    return sol  #given it is solveable, this will be the solution
                    

def check(sud, potDic, x, y, el):
    """This function checks if the potential number is uniquely 
    possible, in either the row, column or square"""

    if (potDic[10][x][el] == 1):                #unique in row
        return True
    if (potDic[11][y][el] == 1):                #unique in column
        return True
    if (potDic[12][sqndic[x][y]][el] == 1):     #unique in square
        return True
    return False


def decrement_dics(potDic, x, y, sqn, el):
    potDic[10][x][el] -= 1
    potDic[11][y][el] -= 1
    potDic[12][sqn][el] -= 1

def update_potdic(potDic, x, y, el):
    for pot_el in potDic[x][y]:
        decrement_dics(potDic, x, y, sqndic[x][y], pot_el)
    potDic[x][y] = set()
    
    for col in numbers:
        if el in potDic[x][col]:
            potDic[x][col].remove(el)
            decrement_dics(potDic, x, col, sqndic[x][col], el)
    
    for row in numbers:
        if el in potDic[row][y]:
            potDic[row][y].remove(el)
            decrement_dics(potDic, row, y, sqndic[row][y], el)
    
    square_n = sqndic[x][y]
    top  = x - x%3
    left = y - y%3
    for row in [top, top+1, top+2]:
        for col in [left, left+1, left+2]:
            if el in potDic[row][col]:
                potDic[row][col].remove(el)
                decrement_dics(potDic, row, col,square_n, el)
    return
    


def update_solve(sud, potDic, left, empty_squares):
    for idx, [x, y] in enumerate(empty_squares):
        if len(potDic[x][y]) == 1:
            el = potDic[x][y].pop()
            sud[x][y] = el
            update_potdic(potDic, x, y, el)
            
            left -= 1
            del empty_squares[idx]
            return left
        else:
            for el in potDic[x][y]:
                if check(sud, potDic, x, y, el):
                    sud[x][y] = el
                    update_potdic(potDic, x, y, el)
                    left -= 1
                    del empty_squares[idx]
                    return left
    return left

def potdic_gen(sudoku):
    """This generates the dictionary which contains the potential 
    elements for each square. potDic[10], potDic[11], potDic[12] store
    the potential element counts from the rows, columns and squares.
    """
    potDic = {}
    for a1 in numbers:
        tempDic = {}
        for b1 in numbers:
            if sudoku[a1][b1] != 0:
                tempDic[b1] = set()
                continue
            tempDic[b1] = set([1,2,3,4,5,6,7,8,9])
        potDic[a1] = tempDic
        
    for row in numbers:
        for col in numbers:
            if sudoku[row, col] != 0:
                el = sudoku[row, col]
                for col2 in numbers:
                    if col2 == col:
                        continue
                    if el in potDic[row][col2]:
                        potDic[row][col2].remove(el)
                for row2 in numbers:
                    if row2 == row:
                        continue
                    if el in potDic[row2][col]:
                        potDic[row2][col].remove(el)
                top = row - row%3
                left = col - col%3
                for row2 in [top, top+1, top+2]:
                    for col2 in [left, left+1, left+2]:
                        if row2 == row and col2 == col:
                            continue
                        if el in potDic[row2][col2]:
                            potDic[row2][col2].remove(el)
        
    potDic[10] = {}
    potDic[11] = {}
    potDic[12] = {}
    for x in numbers:
        potDic[10][x] = {}
        potDic[11][x] = {}
        potDic[12][x] = {}
        
        for x2 in values:
            potDic[10][x][x2] = 0
            potDic[11][x][x2] = 0
            potDic[12][x][x2] = 0
    
    for row in numbers:
        for col in numbers:
            for pot_el in potDic[row][col]:
                potDic[10][row][pot_el] += 1
                potDic[11][col][pot_el] += 1
                potDic[12][sqndic[row][col]][pot_el] += 1
    
    return potDic


def solve(sud):
    """Returns boolean and potDic. Fills an empty square if possible.
    If not, returns False"""
    left = sum([1 for row in sud for el in row if el == 0])
    empty_squares = [[x,y] for x in numbers for y in numbers if sud[x][y] == 0]
    empty_squares.reverse()
    
    potDic = potdic_gen(sud)
    
    teller = 0
    while left > 0 and teller < 9**2+10:
        left = update_solve(sud, potDic, left, empty_squares) 
        teller += 1

    return (left == 0), potDic
    
resSum = 0 
for sudoku in res_all:
    flag, potDic = solve(sudoku)    #in place solver
    if not flag:
        #it is now partially more solved so easier to backtrack
        sudoku = backtrack_solve(sudoku, potDic)
        
    resSum += int(""    .join(map(str, sudoku[0][:3])))


print "Result = " + str(resSum)
print datetime.now() - startTime
#time: 230ms


