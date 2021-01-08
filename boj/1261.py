#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 12:03:03 2021

@author: hihyun
"""
from collections import deque
import sys
def solution(maps):
    N,M=len(maps),len(maps[0])
    q=deque([])
    q.append((0,0))
    v=[[100000]*M for i in range(N)]
    v[0][0]=0
    X=[0,0,-1,1]
    Y=[1,-1,0,0]
    while q:
        cur_x,cur_y=q.popleft()
        wall=v[cur_x][cur_y]
        for i in range(4):
            n_x=X[i]+cur_x
            n_y=Y[i]+cur_y
            if n_x>=0 and n_x<N and n_y>=0 and n_y<M:
                if maps[n_x][n_y]==1:
                    if v[n_x][n_y]>wall+1:
                        v[n_x][n_y]=wall+1
                        q.append((n_x,n_y))
                else:
                    if v[n_x][n_y]>wall:
                        v[n_x][n_y]=wall
                        q.append((n_x,n_y))
    return v[N-1][M-1]
        
"""  
f=open('./input.txt','r')
M,N=map(int,f.readline().strip().split(' '))
maps=[]
for i in range(N):
    maps.append(list(map(int,list(f.readline().strip()))))
print(solution(maps))
"""
M,N=map(int,sys.stdin.readline().strip().split(' '))
maps=[]
for i in range(N):
    maps.append(list(map(int,list(sys.stdin.readline().strip()))))
print(solution(maps))