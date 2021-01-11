#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 08:55:10 2021

@author: hihyun
"""
from collections import defaultdict,deque
def land(cur,island,count,N,total_land,gmap):
    q=deque([])
    q.append(cur)
    visit=[cur]
    X=[0,0,-1,1]
    Y=[-1,1,0,0]
    while q:
        c_x,c_y=q.popleft()
        for i in range(4):
            n_x=c_x+X[i]
            n_y=c_y+Y[i]
            if n_x>=0 and n_x<N and n_y>=0 and n_y<N:
                if gmap[n_x][n_y]==1:
                    if (n_x,n_y) not in visit:
                        visit.append((n_x,n_y))
                        island.remove((n_x,n_y))
                        q.append((n_x,n_y))
    total_land[count]=visit
    return island
def distance(N,gmap,cur,key,total_land):
    q=deque([])
    q.append((cur[0],cur[1],0))#say sth
    visit=[[10000000]*N for i in range(N)]
    visit[cur[0]][cur[1]]=1
    cur_li=total_land[key]
    count=[]

    X=[0,0,-1,1]
    Y=[-1,1,0,0]
    while q:
        c_x,c_y,w=q.popleft()#w=-1 현재 1
        for i in range(4):
            n_x=c_x+X[i]
            n_y=c_y+Y[i]
            if n_x>=0 and n_x<N and n_y>=0 and n_y<N:
                if gmap[n_x][n_y]==1:
                    if visit[n_x][n_y]==10000000:
                        if w==0:#현재 visit 안함
                            visit[n_x][n_y]=0
                            q.append((n_x,n_y,0))
                        else:
                            if (n_x,n_y) not in cur_li:
                                count.append(w)
                else:#0
                    if w+1<visit[n_x][n_y]:
                        q.append((n_x,n_y,w+1))
                        visit[n_x][n_y]=w+1
    return min(count)

def solution(gmap,island):
    total_land=defaultdict(list)
    count=0
    while island:
        cur=island.pop(0)
        island=land(cur,island,count,N,total_land,gmap)
        count+=1
    min_val=100000
    for i in total_land.keys():
        
        min_val=min(min_val,distance(N,gmap,total_land[i][0],i,total_land))


    return min_val

f=open('./input.txt','r')
N=int(f.readline().strip())
gmap=[]
island=[]

for i in range(N):
    temp=list(map(int,list(f.readline().strip().split(' '))))
    gmap.append(temp)
    for idx,j in enumerate(temp):
        if j==1:
            island.append((i,idx))
print(solution(gmap,island))
"""           
N=int(input())
gmap=[]
island=[]

for i in range(N):
    temp=list(map(int,input().split('')))
    gmap.append(temp)
    for idx,j in enumerate(temp):
        if j==1:
            island.append((i,idx))
"""