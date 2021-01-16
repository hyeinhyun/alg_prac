#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 20:50:08 2021

@author: hihyun
"""
def solution(N,K):
    g=[]
    for i in range(1,K+1):
        temp=[]
        for j in range(N+1):
            if i==1:
                temp.append(1)
            else:
                temp.append(sum(g[i-2][:j+1]))
        g.append(temp)
    return g[-1][-1]
    

            
N,K=map(int,input().split(' '))
print(solution(N,K)%1000000000)
