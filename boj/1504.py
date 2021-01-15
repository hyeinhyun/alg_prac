#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 10:29:56 2021

@author: hihyun
"""
from heapq import heappush, heappop
import sys
INF = sys.maxsize

def dik(s,e,m):
    cur_i=s
    cur_w=0
    q=[(cur_w,cur_i)]
    v_w=[INF]*(len(m)+1)
    v_w[s]=0
    
    while q:
        if v_w[cur_i]<cur_w:#더 작은것이 있으면 패스
            continue
        for idx, i in enumerate(m[cur_i]):
            if cur_w+i<v_w[idx]:
                heappush(q,(cur_w+i,idx))
                v_w[idx]=cur_w+i
        cur_w,cur_i=heappop(q)

    return v_w[e]
"""
V,E=map(int,input().split(' '))
m=[[1001]*(V+1) for i in range(V+1)]
for i in range(E):
    s,e,w=map(int,input().split(' '))
    m[s][e]=w
    m[e][s]=w
A,B=map(int,input().split(' '))
print(min(dik(1,A,m)+dik(A,B,m)+dik(B,V,m),dik(1,B,m)+dik(B,A,m)+dik(A,V,m)))
"""
f=open('input.txt','r')
V,E=map(int,f.readline().strip().split(' '))
m=[[INF]*(V+1) for i in range(V+1)]
for i in range(E):
    s,e,w=map(int,f.readline().strip().split(' '))
    m[s][e]=w
    m[e][s]=w
A,B=map(int,f.readline().strip().split(' '))
result=min(dik(1,A,m)+dik(A,B,m)+dik(B,V,m),dik(1,B,m)+dik(B,A,m)+dik(A,V,m))

print(result if result<INF else -1)