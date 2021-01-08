#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 09:13:13 2021

@author: hihyun
"""
from collections import deque
import sys
def solution(sp : list ,tomato : list,v : list):
    N,M=len(tomato),len(tomato[0])
    q=sp
    X=[0,0,1,-1]
    Y=[1,-1,0,0]
    while q:
        c_x,c_y=q.popleft()
        for i in range(4):
            n_x=c_x+X[i]
            n_y=c_y+Y[i]
            if n_x>=0 and n_x<N and n_y>=0 and n_y<M:
                if tomato[n_x][n_y]==0:
                    if v[n_x][n_y]>v[c_x][c_y]+1:
                        q.append((n_x,n_y))
                        tomato[n_x][n_y]=1
                        v[n_x][n_y]=v[c_x][c_y]+1

    return -1 if sum(list(map(lambda x : x.count(0),(*tomato))))!=0 else max(map(max,v))
"""        
N,M=(map(int,input().split(' ')))
tomato=[]
sp=[]
v=[[10000]*N for i in range(M)]
for i in range(M):
    r=list(map(int,input().split(' ')))
    tomato.append(r)
    for idx,j in enumerate(r):
        if j==1:
            sp.append((i,idx))
            v[i][idx]=0
        elif j==-1:
            v[i][idx]=0
print(solution(sp,tomato,v))
"""
f=open('./input.txt','r')
N,M=(map(int,f.readline().strip().split(' ')))
tomato=[]
sp=deque([])
v=[[10000]*N for i in range(M)]
for i in range(M):
    r=list(map(int,f.readline().strip().split(' ')))
    tomato.append(r)
    for idx,j in enumerate(r):
        if j==1:
            sp.append((i,idx))
            v[i][idx]=0


print(solution(sp,tomato,v))
print(list(map(list,*tomato)))
