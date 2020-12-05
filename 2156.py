#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 16:36:45 2020

@author: hihyun
"""
def solution(g):
    for i in range(1,len(g)):
        print(i)
        if i==1:
            answer[1]=g[1]
        if i==2:
            answer[2]=g[1]+g[2]
        else:
            answer[i]=max(g[i]+answer[i-2],g[i]+g[i-1]+answer[i-3],answer[i-1])
        print(answer)
    return max(answer)
num=int(input())
g=[0]
for i in range(num):
    g.append(int(input()))
if len(g)==2:
    print(g[1])
else:
    answer=[0]*(len(g))
    print(solution(g))


