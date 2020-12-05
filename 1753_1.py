#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 15:54:01 2020

@author: hihyun
"""

from collections import defaultdict
import heapq
def solution(s):
    r=[100]*(v+1)
    r[s]=0
    q=[]
    visit=[]
    heapq.heappush(q,[0,s])#(weight,v)
    while q:
        cur=heapq.heappop(q)
        while True:
            if cur[1] in visit:
                cur=heapq.heappop(q)
            else:
                break
        visit.append(cur[1])
        for i in g_map[cur[1]]:
            if i[0] not in visit:
                if cur[0]+i[1]<r[i[0]]:
                    r[i[0]]=cur[0]+i[1]
                    heapq.heappush(q,[r[i[0]],i[0]])
    return r
t=open('./input.txt')
v,e=map(int,t.readline().strip().split(' '))
#v,e=map(int,input().strip().split(' '))
s=int(t.readline().strip())
#s=int(input())
g_map=defaultdict(list)
for i in range(e):
    s_p,e_p,w=map(int,t.readline().strip().split(' '))
    #s_p,e_p,w=map(int,input().split(' '))
    g_map[s_p].append((e_p,w))
r=solution(s)
for i in r[1:]:
    if i==100:
        print('INF')
    else:
        print(i)