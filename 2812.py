#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 00:07:26 2020

@author: hihyun
"""

n,m=map(int,input().split(' '))
x_l=(list(map(int,input())))
num={}
for idx,i in enumerate(x_l):
    if i not in num.keys():
        num[i]=[idx]
    else:
        num[i].append(idx)
x=n-m
answer=['']*n

for i in sorted(num.keys(),reverse=True):
    while len(num[i])!=0:
        if x==0:
            break
        answer[num[i].pop(0)]=str(i)
        x-=1
    if x==0:
        break



r=''
for i in answer:
    r+=i
print(r)