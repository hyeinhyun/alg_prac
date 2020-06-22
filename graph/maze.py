#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 19:22:48 2020

@author: hihyun
"""
#뭐가 문제인가!!!!!!!!!!!!!
import sys

def solution(maze,sp,ep):
    dist=[[-1 for a in range(M)] for b in range(N)]
    visit=[]
    dist[sp[0]][sp[1]]=0
    visit.append(sp)
    aV=[]
    while len(visit)!=0:
        cur_point=visit.pop(0)
        aV.append(cur_point)

        print(aV)
        i=cur_point[0]
        j=cur_point[1]
        
        ##up
        if (i-1)>=0 and dist[i-1][j]<0 and maze[i-1][j]==1 and (i-1,j) not in aV:
            visit.append((i-1,j))
            dist[i-1][j]=dist[i][j]+1
        ##down
        if (i+1<N) and dist[i+1][j]<0 and maze[i+1][j]==1 and (i+1,j) not in aV:
            visit.append((i+1,j))
            dist[i+1][j]=dist[i][j]+1

        ##left
        if (j-1)>=0 and dist[i][j-1]<0 and maze[i][j-1]==1 and (i,j-1) not in aV:
            visit.append((i,j-1))
            dist[i][j-1]=dist[i][j]+1

        ##right
        if (j+1<M) and dist[i][j+1]<0 and maze[i][j+1]==1 and (i,j+1) not in aV:
            visit.append((j,j+1))
            dist[i][j+1]=dist[i][j]+1

    
    return dist[ep[0]][ep[1]]
    
    

    
N,M=map(int,sys.stdin.readline().split())
sp=(0,0)
ep=(N-1,M-1)
maze=[]
for i in range(N):
    maze.append(list(map(int,str(sys.stdin.readline())[:-1])))
print(solution(maze,sp,ep))