#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 19:29:34 2020

@author: hihyun
"""
def solution(pos):
    q=[pos]
    v=[[0]*m for i in range(n)]
    v[pos[0]][pos[1]]=1
    c={str(pos):1}
    pre={str(pos):None}
    cand_c={}
    cand=set()
    r=[-1,1,0,0]
    col=[0,0,-1,1]
    while len(q)!=0:
        cur=q.pop(0)
        if pre[str(cur)] is not None:
            c[str(cur)]=c[str(pre[str(cur)])]+1
        for i in range(4):
            if cur[0]+r[i]>=0 and cur[0]+r[i]<n and cur[1]+col[i]>=0 and cur[1]+col[i]<m:
                if g[cur[0]+r[i]][cur[1]+col[i]]==1:
                    cand.add((cur[0]+r[i],cur[1]+col[i]))
                    if str((cur[0]+r[i],cur[1]+col[i])) not in cand_c.keys():
                        cand_c[str((cur[0]+r[i],cur[1]+col[i]))]=c[str(cur)]
                    else:
                        cand_c[str((cur[0]+r[i],cur[1]+col[i]))]=min(c[str(cur)],cand_c[str((cur[0]+r[i],cur[1]+col[i]))])
                else:
                    if v[cur[0]+r[i]][cur[1]+col[i]]==0:
                        q.append((cur[0]+r[i],cur[1]+col[i]))
                        v[cur[0]+r[i]][cur[1]+col[i]]=1
                        pre[str((cur[0]+r[i],cur[1]+col[i]))]=cur
    return cand_c,cand,c
t=open('./input.txt')
n,m=map(int,t.readline().strip().split(' '))
g=[]
for i in range(n):
    g.append(list(map(int,list(t.readline().strip()))))
a,b,c=solution((0,0))
x,y,z=solution((n-1,m-1))
ss=b&y
min_val=1000000
if str((n-1,m-1)) in c.keys():
    min_val=c[str((n-1,m-1))]

for i in ss:
    min_val=min(x[str(i)]+a[str(i)]+1,min_val)
if min_val==1000000:
    print(-1)
else:
    print(min_val)