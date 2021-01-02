#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 11:02:33 2020

@author: hihyun
"""

num=int(input())
l=[]
l+=list(map(int,input().split(' ')))

sum(l)
l=sorted(l)
c=0
count=0
for cur in l:
    if c+1<cur:
        break
    else:
        c+=cur

print(c+1)