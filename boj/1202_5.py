#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 19:52:47 2021

@author: hihyun
"""
from heapq import heappush,heappop
from collections import defaultdict
def solution(q_bag,q_germ):
    answer=0
    while q_bag:
        b=q_bag[0]
        if len(q_germ)==0:
            break
        v,w=q_germ.pop()
        if b>=w:
            answer+=v
            heappop(q_bag)
    print(answer*-1)
    
                    
                    

    
N,K=map(int,input().split(' '))
gem=[]
gem_h=[]
bag=[]
dic=defaultdict(list)
for i in range(N):
    M,V=map(int,input().split(' '))
    gem.append((-1*V,M))
gem.sort(key=lambda x : x[1])
print(gem)
for i in gem:
    heappush(gem_h,i)
for i in range(K):
    W=int(input())
    heappush(bag,W)
(solution(bag,gem_h))
