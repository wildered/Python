# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 21:27:40 2017

@author: Home
"""

#generate n^a numbers in order and checks these for required property.
#time: 18ms

import itertools
import heapq
from datetime import datetime
from timeit import default_timer as timer

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


startTime = datetime.now()
start = timer()

max_el = 10
add_task((10, 10))
idx = 0

while idx < 29:
    curr_power, n = pop_task()
    
    if n == sum([int(c) for c in str(curr_power)]):
        idx += 1
    
    if curr_power == max_el:
        max_el += 1
        add_task((max_el, max_el))
    
    add_task((curr_power * n, n))

print("Result =", curr_power)
print(datetime.now() - startTime)
print((timer()-start)*1000)
#time: 18ms

