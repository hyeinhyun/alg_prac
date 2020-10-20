#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 00:03:48 2020

@author: hihyun
"""

from itertools import permutations,product
import copy
def solution(dirs): 
    if dirs=='u':
        for k in range((x+1)//2):
            for kk in range(x):
                if k*2+1<x:
                        print(k*2+1,kk)
                        if g_map[k*2][kk]==g_map[k*2+1][kk]:
                            g_map[k*2][kk]*=2
                            g_map[k*2+1][kk]=0

    if dirs=='d':
        for k in range((x-1)//2,0,-1):
            for kk in range(x):
                if k*2-1>=0:
                        if g_map[k*2][kk]==g_map[k*2-1][kk]:
                            g_map[k*2][kk]*=2
                            g_map[k*2-1][kk]=0


    if dirs=='l':
        for k in range((x+1)//2):
            for kk in range(x):
                if k*2+1<x:
                        if g_map[k][k*2]==g_map[kk][k*2+1]:
                            g_map[kk][k*2]*=2
                            g_map[kk][k*2+1]=0

    if dirs=='r':
        for k in range((x-1)//2,0,-1):
            for kk in range(x):
                if k*2-1>=0:
                        if g_map[k][k*2]==g_map[kk][k*2-1]:
                            g_map[kk][k*2]*=2
                            g_map[kk][k*2-1]=0

def dfs(cnt):
    global g_map, max_val
    if cnt == 5:
        for i in range(x):
            for j in range(x):
                max_val = max(max_val, g_map[i][j])
        return

    temp_a = copy.deepcopy(g_map)
    for i in range(4):
        solution(dir_key[i])
        dfs(cnt + 1)
        g_map = copy.deepcopy(temp_a)















f = open("./input.txt", 'r')

x=int(f.readline().strip())
g_map=[]

for i in range(x):
    temp=list(map(int,f.readline().strip().split(' ')))
    g_map.append(temp)

 
dir_key=['u','d','l','r']

dfs(0)
        
print(max_val)