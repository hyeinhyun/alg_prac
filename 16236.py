#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 15:14:54 2020

@author: hihyun
"""
import collections
sys.setrecursionlimit(100000000)
import sys


def solution(s_map,shark_point):
    #처음에 먹을 수 있는 물고기를 찾아
    visit=[]
    q=collections.deque()
    q.append(shark_point)
    pre={str(shark_point):None}
    c={str(shark_point):0}
    cand={}
    toto=0
    pre_g=0
    for i in s_map:
        toto+=sum(i)
    if toto==0:
        return '',0,0
    flag=False
    for i in s_map:
        for j in i:
            if j<shark:
                flag=True
    if flag==False:
        return '',0,0
    while len(q)!=0:

        cur_x,cur_y=q.popleft()
        if pre[str((cur_x,cur_y))]!=None:
            c[str((cur_x,cur_y))]=c[str(pre[str((cur_x,cur_y))])]+1
            
        if len(cand.keys())!=0 and pre_g<c[str((cur_x,cur_y))]:
            break
            ###########
        #up해
        if cur_x>0:
            if (cur_x-1,cur_y) not in visit:
                #작아 --> 그럼 아무것도 append 하지마 (쟤가 마지막)
                if s_map[cur_x-1][cur_y]<shark and s_map[cur_x-1][cur_y]>0:
                    if str((cur_x-1,cur_y)) not in cand.keys():
                        cand[str((cur_x-1,cur_y))]=(c[str((cur_x,cur_y))]+1,s_map[cur_x-1][cur_y]) #초,값
                        visit.append((cur_x-1,cur_y))

                #같아 그냥 무브
                if s_map[cur_x-1][cur_y]==shark or s_map[cur_x-1][cur_y]==0:
                    q.append((cur_x-1,cur_y))
                    pre[str((cur_x-1,cur_y))]=(cur_x,cur_y)
                    visit.append((cur_x-1,cur_y))

        if cur_y>0:
            #left해
            if (cur_x,cur_y-1) not in visit:
                #작아 --> 그럼 아무것도 append 하지마 (쟤가 마지막)
                if s_map[cur_x][cur_y-1]<shark and s_map[cur_x][cur_y-1]>0:
                    if str((cur_x,cur_y-1)) not in cand.keys():
                        cand[str((cur_x,cur_y-1))]=(c[str((cur_x,cur_y))]+1,s_map[cur_x][cur_y-1]) #초,값
                        visit.append((cur_x,cur_y-1))

                #같아 그냥 무브
                if s_map[cur_x][cur_y-1]==shark or s_map[cur_x][cur_y-1]==0:
                    q.append((cur_x,cur_y-1))
                    pre[str((cur_x,cur_y-1))]=(cur_x,cur_y)
                    visit.append((cur_x,cur_y-1))

        if cur_y<num-1:
            #right해
            if (cur_x,cur_y+1) not in visit:
                #작아 --> 그럼 아무것도 append 하지마 (쟤가 마지막)
                if s_map[cur_x][cur_y+1]<shark and s_map[cur_x][cur_y+1]>0:
                    if str((cur_x,cur_y+1)) not in cand.keys():
                        cand[str((cur_x,cur_y+1))]=(c[str((cur_x,cur_y))]+1,s_map[cur_x][cur_y+1]) #초,값
                        visit.append((cur_x,cur_y+1))

                #같아 그냥 무브
                if s_map[cur_x][cur_y+1]==shark or s_map[cur_x][cur_y+1]==0:
                    q.append((cur_x,cur_y+1))
                    pre[str((cur_x,cur_y+1))]=(cur_x,cur_y)
                    visit.append((cur_x,cur_y+1))

        if cur_x<num-1:
            #down헤
            if (cur_x+1,cur_y) not in visit:
                #작아 --> 그럼 아무것도 append 하지마 (쟤가 마지막)
                if s_map[cur_x+1][cur_y]<shark and s_map[cur_x+1][cur_y]>0:
                    if str((cur_x+1,cur_y)) not in cand.keys():
                        cand[str((cur_x+1,cur_y))]=(c[str((cur_x,cur_y))]+1,s_map[cur_x+1][cur_y]) #초,값
                        visit.append((cur_x+1,cur_y))

                #같아 그냥 무브
                if s_map[cur_x+1][cur_y]==shark or s_map[cur_x+1][cur_y]==0:
                    q.append((cur_x+1,cur_y))
                    pre[str((cur_x+1,cur_y))]=(cur_x,cur_y)
                    visit.append((cur_x+1,cur_y))

        pre_g=c[str((cur_x,cur_y))]

    new_shark_point=''
    if len(cand.keys())!=0:
        new=[]
        for i in cand.keys():
            new_key=tuple(map(int,i[1:-1].split(',')))
            new.append(new_key)
        new_shark_point=str(sorted(new)[0])

    if new_shark_point=='':
        return new_shark_point,0,0
    return tuple(map(int,new_shark_point[1:-1].split(','))),cand[new_shark_point][0],cand[new_shark_point][1]


f = open("./input.txt", 'r')
num=int(input())

s_map=[]
shark=2#샤크의 몸집 크기
count=0
shark_point=''#현재 샤크위치
total_sec=0
for i in range(num):
    temp=list(map(int,(input().split(' '))))
    s_map.append(temp)
    for idx,j in enumerate(temp):
        if j==9:
            shark_point=(i,idx)
            s_map[i][idx]=0
#init
new_shark,time_sec,power=solution(s_map,shark_point)
count+=1
if new_shark!='':
    s_map[new_shark[0]][new_shark[1]]=0
while time_sec!=0:
    total_sec+=time_sec
    new_shark,time_sec,power=solution(s_map,new_shark)
    count+=1
    if count==shark:
        shark+=1
        count=0
    if new_shark!='':
        s_map[new_shark[0]][new_shark[1]]=0

print(total_sec)
    
