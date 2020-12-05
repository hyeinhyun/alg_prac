#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 18:10:10 2020

@author: hihyun
"""
from heapq import heappop,heappush
def solution(n, times):
    answer = 0
    #end가 최저인 친구를 
    q=[]
    for i in times:
        heappush(q,(0,i))
    while True:
        et,val=heappop(q)
        if n==1:
            answer=et+val
            break
        heappush(q,(et+val,val))

        n-=1

    return answer
print(solution(6,[7,10]))