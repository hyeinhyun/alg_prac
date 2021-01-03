#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 18:43:51 2021

@author: hihyun
"""
from heapq import heappush,heappop
def solution(card):
    init=0
    answer=0
    while card:
        x=heappop(card)
        if init!=0:
            heappush(card,init+x)
            answer+=init+x
            init=0
        else:
            init=x
    return answer-sum(card)
            


N=int(input())
card=[]
for i in range(N):
    heappush(card,int(input()))
print(solution(card))