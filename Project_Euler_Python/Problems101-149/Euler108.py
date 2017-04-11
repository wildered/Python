# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 18:40:32 2017

@author: Home
"""
#See 110

from math import log, ceil
from eulerTools import isPrime

from datetime import datetime
startTime = datetime.now()
from timeit import default_timer as timer
start = timer()

cutoff = int(1e3)
highest_prime_idx = int(ceil(log(cutoff, 3)))
cutoff = cutoff*2 - 1

primes = [2]
list_l = 1
k = 3
while list_l < highest_prime_idx:
    if isPrime(k):
        primes.append(k)
        list_l += 1
    k += 2
    
import heapq
import itertools

#code taken from Python heapq documentation page
pq = []                         # list of entries arranged in a heap
entry_finder = {}               # mapping of tasks to entries
REMOVED = '<removed-task>'      # placeholder for a removed task
counter = itertools.count()     # unique sequence count
def add_task(task, priority=0):
    'Add a new task or update the priority of an existing task'
    if task in entry_finder:
        remove_task(task)
    count = next(counter)
    entry = [priority, count, task]
    entry_finder[task] = entry
    heapq.heappush(pq, entry)

def remove_task(task):
    'Mark an existing task as REMOVED.  Raise KeyError if not found.'
    entry = entry_finder.pop(task)
    entry[-1] = REMOVED

def pop_task():
    'Remove and return the lowest priority task. Raise KeyError if empty.'
    while pq:
        priority, count, task = heapq.heappop(pq)
        if task is not REMOVED:
            del entry_finder[task]
            return task
    raise KeyError('pop from an empty priority queue')

from copy import copy
curr_arr = [0]*highest_prime_idx
curr_value = 1
curr_n = 1
add_task((tuple(curr_arr), curr_n, curr_value), curr_n)
while True:
    new_arr, new_n, new_value = pop_task()
    if new_value > cutoff:
        break
    if new_value < curr_value:
        continue
    curr_arr = list(new_arr)
    curr_value = new_value
    curr_n = new_n
    idx = 0
    while idx < highest_prime_idx:
        if curr_arr[idx-1] <= curr_arr[idx] and idx != 0:
            if curr_arr[idx] == 0:
                break
            idx += 1
            continue
        arr = copy(curr_arr)
        arr[idx] += 1
        n = curr_n * primes[idx]
        value = (curr_value)/(2*arr[idx]-1)*(2*arr[idx] + 1)
        add_task((tuple(arr), n, value), n)
        idx += 1

print("Smallest n = " + str(new_n))
print(datetime.now() - startTime)
print((timer()-start)*1000)
#time: 0.7ms
    
