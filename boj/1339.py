#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 00:21:23 2020

@author: hihyun
"""
alpha=[0]*26
num=int(input())
answer=0
for i in range(num):
    temp=list(input())[::-1]
    for idx,x in enumerate(temp):
        alpha[ord(x)-65]+=10**idx
for idx,i in enumerate(sorted(alpha,reverse=True)):
    if i!=0:
        answer+=(9-idx)*i
    if i==0:
        break

print(answer)