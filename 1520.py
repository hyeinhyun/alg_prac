#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 00:18:21 2020

@author: hihyun
"""
import sys

def solution(p,r):
    q=[(0,0)]
    while len(q)!=0:
        cur=q.pop(0)
        if cur[0]-1>=0:
            if p[cur[0]-1][cur[1]]<p[cur[0]][cur[1]]:
                q.append((cur[0]-1,cur[1]))
                r[str((cur[0]-1,cur[1]))]+=1
        if cur[0]+1<m:
            if p[cur[0]+1][cur[1]]<p[cur[0]][cur[1]]:
                q.append((cur[0]+1,cur[1]))
                r[str((cur[0]+1,cur[1]))]+=1

        if cur[1]-1>=0:
            if p[cur[0]][cur[1]-1]<p[cur[0]][cur[1]]:
                q.append((cur[0],cur[1]-1))
                r[str((cur[0],cur[1]-1))]+=1

        if cur[1]+1<n:
            if p[cur[0]][cur[1]+1]<p[cur[0]][cur[1]]:
                q.append((cur[0],cur[1]+1))
                r[str((cur[0],cur[1]+1))]+=1
    
    



m,n=map(int,input().split(' '))
p=[]
r={}
for i in range(m):
    p.append(list(map(int,sys.stdin.readline().split(' '))))
for i in range(m):
    for j in range(n):
        r[str((i,j))]=0
r[str((0,0))]=1
print(solution(p,r))
