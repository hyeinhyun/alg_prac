#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 19:02:41 2020

@author: hihyun
"""
from collections import defaultdict
class graph:
    def __init__(self):
        self.graph=defaultdict(list)
    def add(self,node1,node2):
        self.graph[node1].append(node2)
    def show(self):
        print(self.graph)
    def __len__(self):
        return len(self.graph.keys())

g1=graph()
g1.add("r","s")
g1.add("r","v")
g1.add("s","r")
g1.add("s","w")
g1.add("w","s")
g1.add("w","t")
g1.add("w","x")

g1.add("t","w")
g1.add("t","x")
g1.add("t","u")

g1.add("x","t")
g1.add("x","u")
g1.add("x","y")

g1.add("u","x")
g1.add("u","y")
g1.add("u","t")

g1.add("y","u")
g1.add("y","x")
g1.add("v","r")

g1.show()
len(g1)


class queue:
    def __init__(self):
        self.queue=[]
    def enqueue(self,v):
        self.queue.append(v)
    def dequeue(self):
        a=self.queue[0]
        self.queue=self.queue[1:]
        return a

q1=queue()
q1.enqueue(1)
print(q1.queue)
q1.enqueue(2)
q1.enqueue(3)
q1.enqueue(4)
q1.dequeue()



###BFS 
def BFS(G,sp):
    #visit list
    visit={}
    length={}
    for i in G.graph.keys():
        visit[i]=-1
        length[i]=-1
    #queue
    q1=queue()
    visit[sp]=1
    length[sp]=0
    q1.enqueue(sp)
    while(len(q1.queue)!=0):
        point=q1.dequeue()
        print(point)
        adj_e=G.graph[point]
        for i in adj_e:
            if visit[i]==-1:
                q1.enqueue(i)
                visit[i]=1
                length[i]=length[point]+1
    return length
BFS(g1,"s")  



####DFS
def DFS(G,sp,visit):
    visit[sp]=1
    for i in G.graph[sp]:
        if visit[i]==-1:#unvisit
            print(i)
            DFS(G,i,visit)
    
visit={}
for j in g1.graph.keys():
    visit[j]=-1      
DFS(g1,"s",visit)  
   
