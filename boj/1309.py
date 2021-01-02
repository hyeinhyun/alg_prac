#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 19:59:29 2020

@author: hihyun
"""

num=int(input())
g=[0]*num*2
total=[0]*num
for i in range(num*2,0,-1):
    if i==num*2 or i==num*2-1:
        g[i-1]=1
        total[(i+1)//2]=2
    else:
        s=0
        g[i-1]=total[i+2//2]+1
        if i%2==0:
            g[i-1]+=g[i+1]
    total+=g[i-1]

print((total+1)%9901)

