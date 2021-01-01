#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 13:23:05 2020

@author: hihyun
"""
from heapq import heappush,heappop
def solution(N,arr):
    q1=[]
    for i in arr:
        heappush(q1,(i,i))#1이 곱해졋다고 가정
    count=0
    while count<N:
        val1=heappop(q1)
        print(q1)
        for x in arr:#2,3,5,7
            if val1[1]>=x:
                heappush(q1,(x*val1[0],x))
        count+=1
    return val1[0]
        
#print(solution(19,[2,3,5,7]))
L,N=map(int,input().split(' '))
arr=list(map(int,input().split(' ')))
print(solution(N,arr))