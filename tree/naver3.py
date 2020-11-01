#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 23:40:02 2020

@author: hihyun
"""

from collections import defaultdict
class graph:
    def __init__(self):
        self.edges=defaultdict(list)
    def add(self,from_node,to_node):
        self.edges[from_node].append(to_node)
    def divide(self):
        self.leaf=[]
        for i in self.edges.keys():
            if len(self.edges[i])==1:
                self.leaf.append(i)
    
        
        


        
            
graph=graph()
for x in [[1, 4], [3, 2], [1, 6], [5, 3], [5, 1]]:
    graph.add(x[0],x[1])
    graph.add(x[1],x[0])


sorted(graph.edges)
graph.divide()
graph.leaf


for i in graph.leaf:
    
