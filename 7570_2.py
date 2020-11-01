#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 22:18:57 2020

@author: hihyun
"""
def solution():
    for i in range(1,num+1):
        for j in range(1,num+1):
            if c[i-1]==sort_c[j-1]:
                T[i][j]=1+T[i-1][j-1]
            else:
                T[i][j]=max(T[i-1][j],T[i][j-1])
    
    return T[num][num]

num=int(input())
c=list(map(int,input().split()))
sort_c=sorted(c)

T=[[0]*(len(c)+1) for _ in range(len(c)+1)]
print(len(c)-solution())
