#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 12:39:47 2020

@author: hihyun
"""

from heapq import heappop,heappush
x=int(input())
q=[]
for i in range(x):
    num=int(input())
    if num==0:
        try:
            print(heappop(q))
        except:
            print(0)
    else:
        heappush(q,num)