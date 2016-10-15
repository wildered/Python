# -*- coding: utf-8 -*-
"""The puzzle is as follows:
You have 2 eggs and are at a tower with n floors. There is an unknown floor k,
such that for any floor < k it doesn't break, and for floor >= k it does break. 
If not broken, the egg can be reused. (Uniform distribution of k on {1, 2, ... n} is assumed)
Goal: find k.
In this script there will be some algorithms of which the computation time will be measured and 
the average number of throws necessary computed. n = 50.
"""

from datetime import datetime


def algo1(curr, n, eggs, skipped, last_safe, hidden_k, steps, step_size=1):
    if not skipped and curr == hidden_k:
        return steps+1
    if curr >= hidden_k:
        return algo1(last_safe, n, 1, False, last_safe, hidden_k, steps+1)
    else:
        return algo1(curr+1, n, 2, False, last_safe, hidden_k, steps+1)
        
def algo2(curr, n, eggs, skipped, last_safe, hidden_k, steps, step_size):
    if not skipped and curr == hidden_k:
        return steps+1
    if curr >= hidden_k:
        return algo2(last_safe+1, n, 1, False, last_safe, hidden_k, steps+1, step_size=1)
    else:
        return algo2(curr+step_size, n, 2, step_size != 1, curr, hidden_k, steps+1, step_size)
    
        
        
def time(algorithm, n, s):
    start = datetime.now()
    step_total = 0
    max_step = 0
    for k in range(1,n+1):
        steps_made = algorithm(1, n, 2, False, 0, k, 0, step_size = s)
        step_total += steps_made
        if steps_made > max_step:
            max_step = steps_made
    end_time = datetime.now()-start
    return end_time, (step_total, n), max_step
        

#print algo2(1, 50, 2, False, 0, 2, 0, 10)

if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(10000)

    n = 1000
    t1, s1, m1= time(algo1, n, 10)
    print "First simple algorithm took " + str(t1)
    print "And E(steps) = " + str(s1[0]/s1[1]) + " with maximum step size: " + str(m1 ) +  "\n" 
    
    t2, s2, m2 = time(algo2, n, 10)
    print "Second improved algorithm took " + str(t2)
    print "And E(steps) = " + str(s2[0]/s2[1]) + " with maximum step size: " + str(m2) + "\n" 
    
    print "Finding optimal step size"
    start = datetime.now()
#    res = min([time(algo2, n, stap) for stap in range(1,n)], key= lambda x: x[2])
    step_size = 2
    curr_val = time(algo2, n, step_size)[1][0]
    while True:
        step_size += 1
        temp_val = time(algo2, n, step_size)[1][0]
        if temp_val >= curr_val:
            step_size -= 1
            break
        curr_val = temp_val
    end_time = datetime.now()-start
    print "With n = " + str(n) + ", Optimum step size = " + str(step_size) + " and E(steps) = " + str(curr_val / n)
    print "Took "+ str(end_time)
    
    
    #Conclusion: Optimal step size for algorithm 2 is sqrt(n) rounded (?)
    
    
    
    