#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 00:55:30 2020

@author: hihyun
"""
from heapq import heappush,heappop

def solution(N):
    if N==1:
        return 2
    else:
        
        q=[]
        i=2
        while i!=N:
            heappush(q,(i*(i+1),i+2))
            v,n=heappop(q)
            heappush(q,(v*n,n+1))
            i+=1
        return heappop(q)[0]
print(solution(9))
        