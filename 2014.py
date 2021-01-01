#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 13:23:05 2020

@author: hihyun
"""
from heapq import heappush,heappop
def solution(N,arr):
    q1=arr
    q2=arr.copy()
    count=0
    val1=0
    while count!=N+1:
        val1=heappop(q1)

        for x in q2:#2,3,5,7
            if x<=val1:
                print(x*val1)
                heappush(q1,x*val1)
        count+=1
    return val1
        
#print(solution(19,[2,3,5,7]))
L,N=map(int,input().split(' '))
arr=list(map(int,input().split(' ')))
print(solution(N,arr))