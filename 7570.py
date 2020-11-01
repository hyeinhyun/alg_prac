#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 21:54:52 2020

@author: hihyun
"""

num=int(input())
c=list(map(int,input().split()))

count=0
while sorted(c)!=c and len(c)>3:
    c.remove(min(c))
    c.remove(max(c))
    count+=1
if len(c)==0 or len(c)>3:
    print(count*2)
else:
    print(count*2+1)
