#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 21:15:06 2020

@author: hihyun
"""
from heapq import heappop,heappush
import sys
from collections import defaultdict
sys.setrecursionlimit(300000)

N,M=map(int,input().split(' '))
q_germ=[]
q_bag=[]
d_germ=defaultdict(list)
for i in range(N):
    d1,d2=(map(int,input().split(' ')))
    heappush(q_germ,-1*d2)
    heappush(d_germ[-1*d2],-1*d1)
for j in range(M):
    b1=int(input())
    heappush(q_bag,-1*b1)
answer=0
while q_bag:
    cur_bag=heappop(q_bag)
    while q_germ:
        cur_germ=heappop(q_germ)
        cur_w=heappop(d_germ[cur_germ])

        if cur_w>=cur_bag:
            if q_bag:
                if cur_w>=q_bag[0]:
                    heappop(q_bag)
                    heappush(q_bag,cur_bag)
            answer+=cur_germ*-1
            break


print(answer)
"""
from heapq import heappop,heappush
import sys
sys.setrecursionlimit(300000)

N,M=map(int,input().split(' '))
q_germ=[]
q_bag=[]
for i in range(N):
    d1,d2=(map(int,input().split(' ')))
    heappush(q_germ,[-1*d2,-1*d1])
for j in range(M):
    b1=int(input())
    heappush(q_bag,-1*b1)
answer=0
while q_bag:
    cur_bag=heappop(q_bag)
    while q_germ:
        cur_germ=heappop(q_germ)
        if cur_germ[1]>=cur_bag:
            if cur_germ[1]>=q_bag[0]:
                heappop(q_bag)
            heappush(q_bag,cur_bag)
            answer+=cur_germ[0]*-1
            break
print(answer)
"""