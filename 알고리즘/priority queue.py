#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 09:32:11 2021

@author: hihyun
"""
def heapify(q,i):
    n=len(q)
    cur_root=i
    cur_val=q[cur_root]
    left=i*2+1
    right=i*2+2
    flag=0
    if left<n and q[cur_root]>q[left]:#루트보다 더작을때
        q[cur_root],q[left]=q[left],q[cur_root]
        flag=left
    elif right<n and q[cur_root]>q[right]:
        q[cur_root],q[right]=q[right],q[cur_root]
        flag=right
    if cur_val!=q[cur_root]:
        heapify(q,flag)
    return q
        
def build_heap(q):
    n=len(q)
    for i in range(n//2-1,-1,-1):
        q=heapify(q,i)
    return q
    

class pq:
    def __init__(self,list):
        self.q=list
        self.length=len(self.q)
    def insert(self,element):
        self.q.append(element)
        self.q=build_heap(self.q)
        print(self.q)
    def pop(self):
        print(self.q.pop(0))
        self.q=build_heap(self.q)
        
h1=pq([])
h1.insert(10)
h1.insert(9)
h1.insert(11)
h1.insert(12)
h1.insert(13)
h1.insert(14)
h1.insert(15)
h1.insert(16)
h1.insert(8)
h1.pop()
