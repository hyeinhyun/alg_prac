#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 20:28:23 2020
4
@author: hihyun
"""
def check(cand,c):
    x=cand[0]
    y=cand[1]
    for i in range(c):
        if x+i>=n:
            return False
        if y+c-1>=m:
            return False
        if g[x+i][y+c-1]==0:
            return False
        if y+i>=m:
            return False
        if x+c-1>=n:
            return False
        if g[x+c-1][y+i]==0:
            return False
    return True

n,m=map(int,input().split(' '))
g=[]
cand=[]
for i in range(n):
    temp=list(map(int,list(input())))
    for idx,j in enumerate(temp):
        if j==1:
            cand.append((i,idx))
    g.append(temp)
        

count=1
while len(cand)!=0:
    count+=1
    temp=[]
    for i in cand:
        if check(i,count):
            temp.append(i)
    cand=temp
print((count-1)**2)