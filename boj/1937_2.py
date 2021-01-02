#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 14:39:40 2020

@author: hihyun
"""

def find(cur):
    cx,cy=cur
    c=[]
    #up
    if cx-1>=0:
        if g[cx-1][cy]>g[cx][cy]:
            c.append((cx-1,cy))
    #down
    if cx+1<num:
        if g[cx+1][cy]>g[cx][cy]:
            c.append((cx+1,cy))
    #left
    if cy-1>=0:
        if g[cx][cy-1]>g[cx][cy]:
            c.append((cx,cy-1))
    #right
    if cy+1<num:
        if g[cx][cy+1]>g[cx][cy]:
            c.append((cx,cy+1))
    return c
    
def dfs(cur):
    if memo[str(cur)]!=-1:
        return memo[str(cur)]
        
    else:
        child=find(cur)
        max_val=0
        for i in child:
            max_val=max(max_val,dfs(i))

        
        memo[str(cur)]=max_val+1
        return memo[str(cur)]


f = open("./input.txt", 'r')
num=int(f.readline().strip())
#num=int(input())
g=[]
memo={}
for idxi,i in enumerate(range(num)):
    temp=list(map(int,f.readline().strip().split(' ')))
    #temp=list(map(int,input().split(' ')))
    g.append(temp)
    for idxj,j in enumerate(temp):
        memo[str((idxi,idxj))]=-1

for i in range(num):
    for j in range(num):
        dfs((i,j))
"""
i=str((0,0))

while True:
    cur=tuple(map(int,i[1:-1].split(',')))
    dfs(cur)
    i=''
    for k in memo.keys():
        if memo[k]==-1:
            i=k
            break
    if i=='':
        break
"""
print(max(list(memo.values())))

