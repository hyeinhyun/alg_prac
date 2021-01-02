#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 08:15:28 2021

@author: hihyun
"""

#다익스트라 구현
from heapq import heappush,heappop
import sys
def solution(s,d,X):
    x=X[s-1]
    q=[]
    v=[0]*len(x)

    for idx,i in enumerate(x):
        heappush(q,(i,idx))
    while q:
        cur_w,cur_s=heappop(q)
        if v[cur_s]==0:
            if cur_s==d-1:
                return cur_w
            for idx,i in enumerate(X[cur_s]):
                if x[idx]>cur_w+X[cur_s][idx]:
                    x[idx]=cur_w+X[cur_s][idx]
                    heappush(q,(cur_w+X[cur_s][idx],idx))
            
            v[cur_s]=1
    

N=int(input())
M=int(input())
X=[[987654321 for i in range(N)]for j in range(N)]
for i in range(M):
    i,j,w=map(int,input().split(' '))
    if X[i-1][j-1]>w:
        X[i-1][j-1]=w
s,d=map(int,input().split(' '))
print(solution(s,d,X))
