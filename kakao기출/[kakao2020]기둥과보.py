#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 21:51:19 2021

@author: hihyun
"""

from collections import defaultdict

def check_bo(x,y,cur):
    flag=False
    if 't_u' in cur[str((x,y))] or 't_u' in cur[str((x+1,y))]:
        flag=True
 
    elif 'b_r' in cur[str((x,y))] and 'b_l' in cur[str((x+1,y))]:
        flag=True
    return flag
    
def solution(n, build_frame):
    answer = []
    cur=defaultdict(list)
    for x,y,t,f in build_frame:
        if f==1:
            if t==0:#기둥
                if y==0:
                    cur[str((x,y))].append('t_d')
                    cur[str((x,y+1))].append('t_u')
                else:
                    if 'b_l' in cur[str((x,y))] or 'b_r' in cur[str((x,y))]:#보
                        cur[str((x,y))].append('t_d')
                        cur[str((x,y+1))].append('t_u')
                    elif 't_u' in cur[str((x,y))]:
                        cur[str((x,y))].append('t_d')
                        cur[str((x,y+1))].append('t_u')                        
            elif t==1:#보
                if 't_u' in cur[str((x,y))] or 't_u' in cur[str((x+1,y))]:
                        cur[str((x,y))].append('b_l')
                        cur[str((x+1,y))].append('b_r')  
                elif 'b_r' in cur[str((x,y))] and 'b_l' in cur[str((x+1,y))]:
                        cur[str((x,y))].append('b_l')
                        cur[str((x+1,y))].append('b_r')  
        else:#delete
            if t==0:#기둥
                if cur[str((x,y+1))]==['t_u']:#위에 아무것도 없음
                    cur[str((x,y+1))].remove(['t_u'])
                    cur[str((x,y))].remove(['t_d'])
                else:
                    if 't_d' not in cur[str((x,y+1))]:
                        if 'b_l' in cur[str((x,y+1))] and 'b_r' in cur[str((x,y+1))]:
                            flag=False
                            if check_bo(x,y+1,cur) and check_bo(x-1,y+1,cur):
                                flag=True
                            if flag:
                                cur[str((x,y+1))].remove('t_u')
                                
                                cur[str((x,y))].remove('t_d')                               
                        elif 'b_l' in cur[str((x,y+1))]:
                            flag=False
                            if check_bo(x,y+1,cur):
                                flag=True

                            if flag:
                                cur[str((x,y+1))].remove('t_u')
                                cur[str((x,y))].remove('t_d') 
                        elif 'b_r' in cur[str((x,y+1)),cur]:
                            flag=False
                            if check_bo(x-1,y+1):
                                flag=True
                            if flag:
                                cur[str((x,y+1))].remove('t_u')
                                cur[str((x,y))].remove('t_d') 
            else:#보
                if 't_u' not in cur[str((x,y))] and 't_u' not in cur[str((x,y+1))]:
                    if 'b_l' in cur[str((x,y+1))] and 'b_r' in cur[str((x,y))]:
                        flag=False
                        if check_bo(x-1,y+1,cur) and check_bo(x,y+1,cur):
                            flag=True
                  
                        if flag:
                            cur[str((x,y))].remove('b_l')
                            cur[str((x,y+1))].remove('b_r')
                    elif 'b_l' in cur[str((x,y+1))]:
                        flag=False
                        if check_bo(x,y+1,cur):
                            flag=True
                        if flag:
                            cur[str((x,y))].remove('b_l')
                            cur[str((x,y+1))].remove('b_r')
                    elif 'b_r' in cur[str((x,y))]:
                        flag=False
                        if check_bo(x-1,y+1,cur):
                            flag=True
                            if flag:
                                cur[str((x,y))].remove('b_l')
                                cur[str((x,y+1))].remove('b_r')                       
    for i in range(n+1):
        for j in range(n+1):
            if 't_d' in cur[str((i,j))]:
                answer.append([i,j,0])
            if 'b_l' in cur[str((i,j))]:
                answer.append([i,j,1])
    return answer
print(solution(5,[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))