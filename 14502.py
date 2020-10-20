#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 21:42:13 2020

@author: hihyun
"""
from itertools import combinations
import copy


    
def solution(test2,two_list):
    value=len(zero_list)-3
    for i in two_list:
        visit=[]
        q=[i]
        while len(q)!=0:
            cur=q.pop(0)
            r,c=cur
            visit.append(cur)
            if r>0:
                if test2[r-1][c]==0:
                    q.append((r-1,c))
                    test2[r-1][c]=2
                    value-=1
            if r<x-1:
                if test2[r+1][c]==0:
                    q.append((r+1,c))
                    test2[r+1][c]=2
                    value-=1
            if c>0:
                if test2[r][c-1]==0:
                    q.append((r,c-1))
                    test2[r][c-1]=2
                    value-=1

            if c<y-1:
                if test2[r][c+1]==0:
                    q.append((r,c+1))
                    test2[r][c+1]=2
                    value-=1
    return value
    
x,y=map(int,input().split(' '))
test=[]
zero_list=[]
two_list=[]
for i in range(x):
    temp=list(map(int,input().split(' ')))
    for idx,j in enumerate(temp):
        if j==0:
            zero_list.append((i,idx))
        if j==2:
            two_list.append((i,idx))
    test.append(temp)
zero_comb=list(combinations(zero_list,3))

max_val=0
for z in zero_comb:
    a,b,c=z
    test2=copy.deepcopy(test)
    test2[a[0]][a[1]]=1
    test2[b[0]][b[1]]=1
    test2[c[0]][c[1]]=1
    res=solution(test2,two_list)
    if max_val<res:
        max_val=res
print(max_val)