#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 19:52:47 2021

@author: hihyun
"""
from heapq import heappush,heappop
from collections import defaultdict
def solution(bag,gem):
    answer=0
    while bag:
        q=[]
        b=heappop(bag)
        while gem:
            m,v=heappop(gem)
            if b>=m:
                heappush(q,(-1*v,m))
            else:
                break
        if q:
            answer+=heappop(q)[0]*(-1)

        else:
            break
        
    return answer
    
                    
                    

    
N,K=map(int,input().split(' '))
gem=[]
bag=[]
dic=defaultdict(list)
for i in range(N):
    M,V=map(int,input().split(' '))
    heappush(gem,(M,V))
for i in range(K):
    W=int(input())
    heappush(bag,W)
print(solution(bag,gem))
