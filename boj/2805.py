#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 10:48:29 2021

@author: hihyun
"""
def solution(H,tree,min_v,max_v):
    while max_v-1>min_v:
        mid_v=(min_v+max_v)//2
        t=0
        for i in tree:
            if i-mid_v>=0:
                t+=(i-mid_v)
        if t>=H:
            min_v=mid_v
        else:
            max_v=mid_v
    return min_v
            
    
N,H=map(int,input().split(' '))
tree=list(map(int,input().split(' ')))
min_v=1
max_v=max(tree)
print(solution(H,tree,min_v,max_v))
