#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 20:28:23 2020
4
@author: hihyun
"""

n,m=map(int,input().split(' '))
g=[]
cand=[]
for i in range(n):
    temp=list(map(int,list(input())))
    for idx,j in enumerate(temp):
        if j==1:
            cand.append((i,idx))
    g.append(temp)
        
max_val=0
for i in range(n-1,-1,-1):
    for j in range(m-1,-1,-1):
        if g[i][j]==1:
            if i+1>=n or j+1>=m:
                if g[i][j]>max_val:
                    max_val=g[i][j]
                pass
            else:
                g[i][j]=min(g[i+1][j],g[i][j+1],g[i+1][j+1])+1
                if g[i][j]>max_val:
                    max_val=g[i][j]
print((max_val)**2)