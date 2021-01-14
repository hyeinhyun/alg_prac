#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 09:22:36 2021

@author: hihyun
"""

def check_bo(x,y,cur):
from collections import defaultdict

def check_t(x,y,cur):
    if 'b_l' in cur[str((x,y))] or 'b_r' in cur[str((x,y))] or 't_u' in cur[str((x,y))] or y==0:#보
        return True
    return False

def check_bo(x,y,cur):
    if 't_u' in cur[str((x,y))] or 't_u' in cur[str((x+1,y))] or ('b_r' in cur[str((x,y))] and 'b_l' in cur[str((x+1,y))]):
        return True
    return False

def solution(n, build_frame):
    answer = []
    cur=defaultdict(list)
    for x,y,t,f in build_frame:
        if f==1:
            if t==0:#기둥
                if check_t(x,y,cur):
                    cur[str((x,y))].append('t_d')
                    cur[str((x,y+1))].append('t_u')

            elif t==1:#보
                if check_bo(x,y,cur):
                    cur[str((x,y))].append('b_l')
                    cur[str((x+1,y))].append('b_r')  

        else:#delete
            if t==0:#기둥
                #일단 삭제
                cur[str((x,y+1))].remove('t_u')
                cur[str((x,y))].remove('t_d')
                flag=True              
                if flag:
                    if 't_d' in cur[str((x,y+1))]:
                        if not check_t(x,y+1,cur):
                            flag=False
                if flag:
                    if 'b_l' in cur[str((x,y+1))]:
                        if not check_bo(x,y+1,cur):
                            flag=False                
                if flag:
                    if 'b_l' in cur[str((x-1,y+1))]:
                        if not check_bo(x-1,y+1,cur):
                            flag=False

                if not flag:
                    cur[str((x,y+1))].append('t_u')
                    cur[str((x,y))].append('t_d')

            else:#보
                cur[str((x,y))].remove('b_l')
                cur[str((x+1,y))].remove('b_r')
                flag=True
                if flag:
                    if 't_d' in cur[str((x,y))]:
                        if not check_t(x,y,cur):
                            flag=False              
                if flag:
                    if 't_d' in cur[str((x+1,y))]:
                        if not check_t(x+1,y,cur):
                            flag=False
                if flag:
                    if 'b_l' in cur[str((x+1,y))]:
                        if not check_bo(x+1,y,cur):
                            flag=False                
                if flag:
                    if 'b_l' in cur[str((x-1,y))]:
                        if not check_bo(x-1,y,cur):
                            flag=False 
                if not flag:
                    cur[str((x,y))].append('b_l')
                    cur[str((x+1,y))].append('b_r')

    for i in range(n+1):
        for j in range(n+1):
            if 't_d' in cur[str((i,j))]:
                answer.append([i,j,0])
            if 'b_l' in cur[str((i,j))]:
                answer.append([i,j,1])
    return answer
print(solution(5,[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))