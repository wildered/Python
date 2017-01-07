# -*- coding: utf-8 -*-
"""
Created on Sat Jan 07 12:35:37 2017

@author: Home
"""

"""Basic linear algebra. From The problem we can assume that a unique
OP for k < n. As a result, we have that OP(k, k+1) will always be
incorrect for k < n. (The system of equations with k+1 
would be unsolvable). Instead of creating a new matrix for every k,
we make a 11 by 10 matrix and reduce the upper left submatrix_{jxj} to
echelon form for i = 1..10 . After each iteration, we can read the 
first j coefficients in the right-most column and use these to 
calculate the FIT. """

import numpy as np

from timeit import default_timer as timer
start = timer()

max_n = 10
def func(n):
    return 1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8 - n**9 + n**10

mat = np.zeros([max_n, max_n + 1], dtype = long)
for i in range(1, max_n + 1):
    temp_arr = [i**k for k in range(max_n)] + [func(i)]
    mat[i-1] = temp_arr
    
FIT_sum = 0
for submatrix_length in range(max_n):
    pivotcol, pivotrow = submatrix_length, submatrix_length
    for pivot_idx in range(pivotcol):
        mat[pivotrow] = mat[pivotrow] - mat[pivotrow, pivot_idx]/mat[pivot_idx, pivot_idx]*mat[pivot_idx]
        
    mat[pivotrow] = mat[pivotrow]/mat[pivotrow, pivotcol]
    for pivot_bdx in range(pivotrow):
        mat[pivot_bdx] = mat[pivot_bdx] - mat[pivot_bdx, pivotcol]/mat[pivotrow, pivotcol] * mat[pivotrow]
    
    n = submatrix_length + 1
    FIT_sum += sum([mat[k, 10]*(n+1)**k for k in range(n)])
        
print "Result = " + str(FIT_sum)
print timer()-start
#time: 0.5ms
