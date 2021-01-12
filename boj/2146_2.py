#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 11:14:05 2021

@author: hihyun
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 08:55:10 2021

@author: hihyun
"""
from collections import defaultdict,deque
def land(cur,island,count,N,total_land,gmap):#land의 상태를 구함
    q=deque([])
    q.append(cur)
    visit=[cur]
    X=[0,0,-1,1]
    Y=[-1,1,0,0]
    cand=[]
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
def distance(N,gmap,cur,island):#각 섬에서 영역을 넓히며 다른 섬까지의 count (w값으로 카운트)
    q=deque([])
    q.append((cur[0],cur[1],0))
    visit=[[10000000]*N for i in range(N)]
    #visit=[cur]
    visit[cur[0]][cur[1]]=1
    terr=[]
    #cur_li=total_land[key]
    cand=[]
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
                        if w==0:#현재 같은섬에서 있음
                            visit[n_x][n_y]=0
                            terr.append((n_x,n_y))
                            q.append((n_x,n_y,0))
                            island.remove((n_x,n_y))
                        else:#다른섬일때
                            cand.append((n_x,n_y,w))
                else:#0일때 계속 카운트
                    if w+1<visit[n_x][n_y]:
                        q.append((n_x,n_y,w+1))
                        visit[n_x][n_y]=w+1
    min_val=100000
    for x,y,w in cand:
        if (x,y) not in terr:
            min_val=min(min_val,w)
    return island,min_val

def solution(gmap,island):
    min_val=100000

    while island:
        cur=island.pop(0)
        island,val=distance(N,gmap,cur,island)
        min_val=min(val,min_val)


    return min_val

f=open('./input.txt','r')
N=int(f.readline().strip())
gmap=[]#map
island=[]#값 1인 좌표

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