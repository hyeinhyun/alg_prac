#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 00:39:30 2020

@author: hihyun
"""

num=int(input())
pos=[]

neg=[]
zero=0
one=0
for k in range(num):
    i=int(input())
    if i<0 and i!=0:
        neg.append(i)
    elif i==1:
        one+=1
    elif i==0:
        zero+=1
    else:
        pos.append(i)

pos_val=0
neg_val=0
pos=sorted(pos,reverse=True)
neg=sorted(neg)

for i in range(len(neg)//2):
    neg_val+=neg[i*2]*neg[i*2+1]
for i in range(len(pos)//2):
    pos_val+=pos[i*2]*pos[i*2+1]

if len(neg)%2!=0:
    if zero!=0:
        pass
    else:
        neg_val+=neg[-1]
if len(pos)%2!=0:
    pos_val+=pos[-1]
print(pos_val+neg_val+one)