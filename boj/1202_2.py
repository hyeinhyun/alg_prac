#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 10:07:39 2021

@author: hihyun
"""
import sys
sys.setrecursionlimit(300000)
from heapq import heappop,heappush

def heapify(q,i):
    cur_root=i
    left=i*2+1
    right=i*2+2
    n=len(q)
    flag=0
    if left<n and q[left][0]>=q[cur_root][0]:
        if q[left][0]>q[cur_root][0]:
            q[left],q[cur_root]=q[cur_root],q[left]
        else:#같다면
            if q[left][1]<q[cur_root][1]:#무게가 작다면,
                q[left],q[cur_root]=q[cur_root],q[left]
    elif right<n and q[right][0]>=q[cur_root][0]:
        if q[right][0]>q[cur_root][0]:
            q[right],q[cur_root]=q[cur_root],q[right]
        else:#같다면
            if q[right][1]<q[cur_root][1]:#무게가 작다면,
                q[right],q[cur_root]=q[cur_root],q[right]
    if flag !=0:
        heapify(q,flag)
    return q
def build_heap(q):
    n=len(q)
    for i in range(n//2-1,-1,-1):
        q=heapify(q,i)
    return q
class heap:
    def __init__(self,l):
        self.q=l
        self.n=len(l)
    def insert(self,e):
        self.q.append(e)
        build_heap(self.q)
    def is_empty(self):
        if len(self.q)==0:
            return True
    def pop(self):
        x=(self.q.pop(0))
        build_heap(self.q)
        return x

N,M=map(int,input().split(' '))
q_germ=heap([])
q_bag=[]
for i in range(N):
    d1,d2=(map(int,input().split(' ')))
    q_germ.insert([d2,d1])
for i in range(M):
    heappush(q_bag,int(input()))
answer=0
while q_bag:
    b=q_bag[0]
    if q_germ.is_empty():
        break
    v,w=q_germ.pop()
    if b>=w:
        answer+=v
        heappop(q_bag)
print(answer)