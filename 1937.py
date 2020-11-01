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
    
def bfs(cur):
    if memo[str(cur)]!=-1:
        return memo[str(cur)]
        
    else:    
        q=[cur]
        c={str(cur):1}
        pre={str(cur):None}
        while len(q)!=0:
            cp=q.pop(0)
            if pre[str(cp)] is not None:
                c[str(cp)]=c[str(pre[str(cp)])]+1
            child=find(cp)
            for i in child:
                if memo[str(i)]!=-1:
                    print('touch')
                    c[str(i)]=c[str(cp)]+memo[str(i)]
                else:
                    q.append(i)
                    pre[str(i)]=cp
        memo[str(cur)]=max(list(c.values()))
        return memo[str(cur)]


#f = open("./input.txt", 'r')
#num=int(f.readline().strip())
num=int(input())
g=[]
memo={}
for idxi,i in enumerate(range(num)):
    #temp=list(map(int,f.readline().strip().split(' ')))
    temp=list(map(int,input().split(' ')))
    g.append(temp)
    for idxj,j in enumerate(temp):
        memo[str((idxi,idxj))]=-1
for i in memo.keys():
        print(i)
        if all([-1<i for i in memo.values()]):
            break
        else:
            cur=tuple(map(int,i[1:-1].split(',')))
            bfs(cur)
print(max(list(memo.values())))

