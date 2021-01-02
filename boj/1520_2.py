#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 12:10:45 2020

@author: hihyun
"""

import sys
sys.setrecursionlimit(1000000)

def solution(p,s,e):
    if s==e:
        r[str((0,0))]=1
        return 1
    else:
        total=0
        if e[0]-1>=0:
            if p[e[0]-1][e[1]]>p[e[0]][e[1]]:
                if r[str((e[0]-1,e[1]))]==-1:
                    total+=solution(p,s,(e[0]-1,e[1]))
                else:
                    total+=r[str((e[0]-1,e[1]))]                    
        if e[0]+1<m:
            if p[e[0]+1][e[1]]>p[e[0]][e[1]]:
                if r[str((e[0]+1,e[1]))]==-1:
                    total+=solution(p,s,(e[0]+1,e[1]))
                else:
                    total+=r[str((e[0]+1,e[1]))]

        if e[1]-1>=0:
            if p[e[0]][e[1]-1]>p[e[0]][e[1]]:
                if r[str((e[0],e[1]-1))]==-1:
                    total+=solution(p,s,(e[0],e[1]-1))
                else:
                    total+=r[str((e[0],e[1]-1))]

        if e[1]+1<n:
            if p[e[0]][e[1]+1]>p[e[0]][e[1]]:
                if r[str((e[0],e[1]+1))]==-1:
                    total+=solution(p,s,(e[0],e[1]+1))
                else:
                    total+=r[str((e[0],e[1]+1))]
        r[str(e)]=total

        return total
    

    
    



m,n=map(int,sys.stdin.readline().split(' '))
p=[]
r={}
for i in range(m):
    p.append(list(map(int,sys.stdin.readline().split(' '))))
for i in range(m):
    for j in range(n):
        r[str((i,j))]=-1

print(solution(p,(0,0),(m-1,n-1)))
