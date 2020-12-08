#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 20:15:40 2020

@author: hihyun
"""

import sys
from collections import deque
def solution(g):
    N=len(g)
    M=len(g[0])
    q=deque([(0,0)])
    visit=[[0]*M for i in range(N)]
    count={str((0,0)):1}
    live={str((0,0)):1}
    mv_x=[-1,1,0,0]
    mv_y=[0,0,-1,1]
    answer=-1
    while q:
        cur=q.popleft()
        cur_x=cur[0]
        cur_y=cur[1]
        visit[cur_x][cur_y]=1
        if cur==(N-1,M-1):
            answer=count[str(cur)]
            break
        for i in range(4):
            mx=mv_x[i]
            my=mv_y[i]
            if cur_x+mx>=0 and cur_x+mx<N and cur_y+my>=0 and cur_y+my<M:
                step=(cur_x+mx,cur_y+my)
                if live[str(cur)]==1:
                    if g[cur_x+mx][cur_y+my]==0:
                        if visit[step[0]][step[1]]==0:
                            visit[step[0]][step[1]]=1
                            q.append(step)
                            count[str(step)]=count[str(cur)]+1
                            live[str(step)]=1
                    else:
                        if visit[step[0]][step[1]]==0:
                            visit[step[0]][step[1]]=1
                            q.append(step)
                            count[str(step)]=count[str(cur)]+1
                            live[str(step)]=0
                else:
                    if g[cur_x+mx][cur_y+my]==0:
                        if visit[step[0]][step[1]]==0:
                            visit[step[0]][step[1]]=1
                            q.append(step)
                            count[str(step)]=count[str(cur)]+1
                            live[str(step)]=0
    return answer 
        
#t=open('./input.txt')
n,m=map(int,input().split(' '))
g=[]
for i in range(n):
    g.append(list(map(int,list(input().strip()))))
print(solution(g))