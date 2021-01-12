#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 11:12:56 2021

@author: hihyun
"""
"""
from heapq import heappush,heappop
def check(val,stones, k):
    ck = 0
    for i in stones:
        if i - val <= 0:
            ck += 1
        else:
            ck = 0
        if ck >= k:
            return False
    return True

def solution(stones, k):
    s=sorted(list(set(stones)))
    q=[]
    for i in (stones):
        heappush(q,i)
    answer=0
    for i in s:
        if not check(i,stones,k):
            answer=i
            break

    return answer
print(solution([1, 2, 1, 3, 4, 5],3 ))
"""
def check(val,stones, k):
    ck = 0
    for i in stones:
        if i - val <= 0:
            ck += 1
        else:
            ck = 0
        if ck >= k:
            return True
    return False

def solution(stones, k):
    min_v,max_v=1,200000000
    while max_v-1>min_v:
        print(max_v,min_v)
        mid_v=(min_v+max_v)//2
        if check(mid_v,stones,k):
            max_v=mid_v
        else:
            min_v=mid_v


    return max_v
print(solution([1, 2, 1, 3, 4, 5],3 ))
