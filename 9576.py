#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 17:06:26 2020

@author: hihyun
"""

tc=int(input())
for i in range(tc):
    lim,num=map(int,input().split(' '))
    book_confirm=[0]*lim
    std=[]
    for j in range(num):
        x,y=map(int,input().split(' '))
        std.append((x,y))
    std.sort(key=lambda x:x[0],reverse=True)
    std.sort(key=lambda x:x[1])
    for j1,j2 in std:
        for e in range(j1-1,j2):
            if book_confirm[e]==0:
                book_confirm[e]=1
                break

print(sum(book_confirm))
a=[[3,6],[2,6]]
a.sort(key=lambda x:x[0])
a.sort(key=lambda x:x[1])
