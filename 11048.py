#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 23:20:32 2020

@author: hihyun
"""


def solution(order):
    g_b[n-1][m-1]=g[n-1][m-1]
    for i in order:
        x=i[0]
        y=i[1]
        if x-1>=0:
            g_b[x-1][y]=max(g_b[x-1][y],g[x-1][y]+g_b[x][y])
        if y-1>=0:
            g_b[x][y-1]=max(g_b[x][y-1],g[x][y-1]+g_b[x][y])
        if x-1>=0 and y-1>=0:
            g_b[x-1][y-1]=max(g_b[x-1][y-1],g[x-1][y-1]+g_b[x][y])        


n,m=map(int,input().split(' '))
g=[]
for i in range(n):
    g.append(list(map(int,input().split(' '))))
g_b=[[0]*m for i in range(n)]

order=[]
for i in range(m):
    for j in range(i+1):
        if i-j<n:
            order.append((i-j,j))

for i in range(m,m+n):
    for j in range(m):
        if i-j<n:
            order.append((i-j,j))
order=order[::-1]

solution(order)
print(g_b[0][0])
