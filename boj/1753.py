#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 10:18:04 2020

@author: hihyun
"""
from collections import defaultdict
import heapq
import sys
def solution(s):
    r=[10000000]*(v+1)
    r[s]=0
    q=[]
    heapq.heappush(q,[0,s])#(weight,v)
    while q:
        cur_w,cur_v=heapq.heappop(q)
        for i_v,i_w in g_map[cur_v]:
                if cur_w+i_w<r[i_v]:
                    r[i_v]=cur_w+i_w
                    heapq.heappush(q,[r[i_v],i_v])
    return r
#t=open('./input.txt')
#v,e=map(int,t.readline().strip().split(' '))
v,e=map(int,sys.stdin.readline().split(' '))
#s=int(t.readline().strip())
s=int(sys.stdin.readline())
g_map=defaultdict(list)
for i in range(e):
    #s_p,e_p,w=map(int,t.readline().strip().split(' '))
    s_p,e_p,w=map(int,sys.stdin.readline().split(' '))
    g_map[s_p].append((e_p,w))
r=solution(s)
for i in r[1:]:
    if i==10000000:
        print('INF')
    else:
        print(i)
        
        
from heapq import heappop,heappush
q=[]
heappush(q,5)
heappush(q,4)
heappush(q,3)
heappush(q,2)