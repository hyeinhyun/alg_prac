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


from heapq import heappush,heappop
import sys
sys.setrecursionlimit(100000)
a=[]
num=int(input())
answer=0
for i in range(num):
    heappush(a,int(input()))
if num<2:
    print(heappop(a) if a else 0)
else:
    answer=heappop(a)+heappop(a)
    for i in range(num-2):
            answer+=answer+(heappop(a) if a else 0)
    print(answer)