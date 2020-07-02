#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 22:02:04 2020

@author: hihyun
"""

import sys

def DFS(graph,S,visit):
    cur=S
    visit.append(cur)
    for i in range(M):

        if graph[cur-1][i]==1:
            if i+1 not in visit:
                DFS(graph,i+1,visit)
        if len(visit)==M:
            break
    return visit

def BFS(graph,S):
    visit=[S]
    queue=[S-1]
    while len(queue)!=0:
        cur=queue.pop(0)
        for i in range(M):
            if graph[cur][i]==1:
                if i+1 not in visit:
                    visit.append(i+1)
                    queue.append(i)
    print(" ".join(map(str,visit)))
    


M,N,S=map(int,sys.stdin.readline().split())
graph=[[0 for i in range (M)] for j in range(M)]
for k in range(N):
    i,j=map(int,sys.stdin.readline().split())
    graph[i-1][j-1]=1
    graph[j-1][i-1]=1
print(" ".join(map(str,DFS(graph,S,[]))))

BFS(graph,S)

