#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 11:30:49 2020

@author: hihyun
"""
from collections import defaultdict,deque
import copy
import sys
def bfs(g):
    p={1:[1]}
    q=deque([1])
    while len(q)!=0:#log(N)
        cur=q.popleft()

        for i in g[cur]:
            q.append(i)
            p[i]=copy.deepcopy(p[cur])
            p[i].append(i)
    return p
    
f=open('./input.txt','r')
num=int(f.readline().strip())
#num=int(input())
g=defaultdict(list)
for i in range(num-1):
    temp=sorted(list(map(int,f.readline().strip().split(' '))))
    g[temp[0]].append(temp[1])
g[num-1]=[]
p=bfs(g)

N=int(f.readline().strip())
#N=int(sys.stdin.readline())
for i in range(N):
    temp=sorted(list(map(int,f.readline().strip().split(' '))))
    #x,y=map(int,sys.stdin.readline().split(' '))
    x=p[temp[0]]
    y=p[temp[1]][:len(x)]
    print(x)
    print(y)
    for x1,y1 in zip(x[::-1],y[::-1]):
        if x1==y1:
            print(x1)
            break
