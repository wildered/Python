# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 00:03:01 2016

@author: Home
"""

class node:
    
    def __init__(self, name):
        self.name = name
        self.edges = []
        self.checked = 0
        self.out = []
        
    def add_edge(self, edge_new):
        self.edges.append(edge_new)
        self.out.append(edge_new.get_other())
        
    def remove_edge(self, edge_old):
        self.edges.remove(edge_old)
        self.out.remove(edge_old.nodes.get_other(self))
        
    def connected(self):
        return self.out
        
    def __str__(self):
        return "Node " + str(self.name)
        
    def __lt__(self, other):
        return (self.dist < other.dist)
        

#from heapq import *
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


class edge:
    
    def __init__(self, node1, node2, d):
        self.a = node1
        self.b = node2
        self.distance = d
    
    def get_other(self):
        return self.b
    


class graph:
    
    def __init__(self, d_dic):
        
        self.nodes = []
        self.trans_d = {}
        
        for node_name in d_dic:
            new_n = node(node_name)
            self.nodes.append(new_n)
            self.trans_d[node_name] = new_n
        
        for node1 in self.nodes:
            
            for node2_name in d_dic[node1.name]:
                node2 = self.trans_d[node2_name]
                connection = edge(node1, node2, d_dic[node1.name][node2.name])
                node1.add_edge(connection)
    

    def dijkstra(self, start, goal="", only_dist = False):

        global pq, entry_finder, REMOVED, counter
        pq = []                         # list of entries arranged in a heap
        entry_finder = {}               # mapping of tasks to entries
        REMOVED = '<removed-task>'      # placeholder for a removed task
        counter = itertools.count()     # unique sequence count
        
        for point in self.nodes:
            point.dist = float('inf')
            point.prev = ""
            add_task(point, point.dist)
        
        start.dist = 0
        add_task(start, 0)
        
        left = len(self.nodes)
        while left > 0:
            
            
            point = pop_task()
            if point == goal:
                break
            left -= 1
            
            for line in point.edges:
                alt = point.dist + line.distance
                if alt < line.get_other().dist:
                    other_node = line.get_other()
                    other_node.dist = alt
                    other_node.prev = point
                    add_task(other_node, alt)
                    
                
        if goal != "":
            if only_dist:
                return goal.dist
            path_length = goal.dist
            path = []
            curr = goal
            while curr != "":
                path.append(curr)
                curr = curr.prev
            path.reverse()
            return path_length, path
            
            
            