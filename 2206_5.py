#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 23:21:24 2020

@author: hihyun
"""
import sys
from collections import deque
def solution(g):
    N=len(g)
    M=len(g[0])
    q=deque([(0,0,1)])
    visit=[[[0]*M for i in range(N)],[[0]*M for i in range(N)]]
    count=[[0]*M for i in range(N)]
    count[0][0]=1
    visit[0][0][0]=1
    #visit=[str((0,0,1))]
    #count={str((0,0,1)):1}
    #live={str((0,0)):1}
    mv_x=[-1,1,0,0]
    mv_y=[0,0,-1,1]
    answer=-1
    while q:
        cur=q.popleft()
        cur_x=cur[0]
        cur_y=cur[1]
        cur_l=cur[2]
        if cur_x==N-1 and cur_y==M-1:
            answer=count[N-1][M-1]
            break
        for i in range(4):
            mx=mv_x[i]
            my=mv_y[i]
            if cur_x+mx>=0 and cur_x+mx<N and cur_y+my>=0 and cur_y+my<M:
                step=(cur_x+mx,cur_y+my)
                if cur_l==1:
                    if g[step[0]][step[1]]==0:
                        if visit[1][step[0]][step[1]]==0:
                            step=step+(1,)
                            q.append(step)
                            visit[1][step[0]][step[1]]=1
                            count[step[0]][step[1]]=count[cur_x][cur_y]+1
                            #live[str(step)]=1
                    else:
                        if visit[0][step[0]][step[1]]==0:
                            step=step+(0,)
                            q.append(step)
                            visit[0][step[0]][step[1]]=1
                            count[step[0]][step[1]]=count[cur_x][cur_y]+1
                            #live[str(step)]=0
                else:
                    if g[step[0]][step[1]]==0:
                        if visit[0][step[0]][step[1]]==0:
                            step=step+(0,)
                            visit[0][step[0]][step[1]]=1
                            q.append(step)
                            count[step[0]][step[1]]=count[cur_x][cur_y]+1
                            #live[str(step)]=0
    return answer 
        
t=open('./input.txt')
n,m=map(int,t.readline().strip().split(' '))
g=[]
for i in range(n):
    g.append(list(map(int,list(t.readline().strip()))))
print(solution(g))
visit=[[[0]*6 for i in range(6)],[[0]*6 for i in range(6)]]
visit[0][1][1]=1
visit[1][1][1]=1
visit
