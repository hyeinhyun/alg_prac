#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 21:08:21 2020

@author: hihyun
"""

f=open('./input.txt','r')
N,K=map(int,f.readline().split(' '))
j={}
bag=[]
for i in range(N):
    x,y=(map(int,f.readline().split(' ')))
    j[x]=y
for i in range(K):
    bag.append(int(f.readline()))
new_j={}
for i in sorted(j.items()):
    new_j[i]=j[i]

bag=sorted(bag,reverse=True)
total=0

'''
for i in bag:
    max_val=0
    max_key=-1
    for k in new_j.keys():
        if k>i:
            break
        else:
            if max_val<new_j[k]:
                max_val=new_j[k]
                max_key=k
    total+=max_val
    new_j[max_key]=-1
print(total)
'''