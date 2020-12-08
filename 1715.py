#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 14:48:57 2020

@author: hihyun
"""

from heapq import heappush,heappop

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
            print(a)

            answer+=answer+(heappop(a) if a else 0)
            print(answer)
    print(answer)
