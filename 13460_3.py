#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 14:25:52 2020

@author: hihyun
"""

import sys


def move(g_map,cur,cur_b):
    p_r,p_c=cur
    b_r,b_c=cur_b
    r=['','','','']
    r_b=['','','','']
    #up
    for i in range(p_r-1,0,-1):#자신 포함 x
        if g_map[i][p_c]=='.':
            r[0]=(i,p_c)
    for i in range(b_r,0,-1):#자신 포함
        if g_map[i][b_c]=='.':
            r_b[0]=(i,b_c)
    if r[0]==r_b[0]:
        if r>r_b:
            r[0]=(r[0][0]+1,r[0][1])
        else:
            r_b[0]=(r_b[0][0]+1,r_b[0][1])
    #down
    for i in range(p_r+1,x):#자신 포함 x
        if g_map[i][p_c]=='.':
            r[1]=(i,p_c)
    for i in range(b_r,x):#자신 포함
        if g_map[i][b_c]=='.':
            r_b[1]=(i,b_c)
    if r[1]==r_b[1]:
        if r>r_b:
            r_b[1]=(r_b[1][0]-1,r_b[1][1])
        else:
            r[1]=(r[1][0]-1,r[1][1])
    #left            
    for i in range(p_c-1,0,-1):#자신 포함 x
        if g_map[p_r][i]=='.':
            r[2]=(p_r,i)
    for i in range(b_c,0,-1):#자신 포함
        if g_map[b_r][i]=='.':
            r_b[2]=(b_r,i)
    if r[2]==r_b[2]:
        if r>r_b:
            r[2]=(r[2][0],r[2][1]+1)
        else:
            r_b[2]=(r_b[2][0],r_b[2][1]+1)
            
    #right            
    for i in range(p_c+1,y):#자신 포함 x
        if g_map[p_r][i]=='.':
            r[3]=(p_r,i)
    for i in range(b_c,y):#자신 포함
        if g_map[b_r][i]=='.':
            r_b[3]=(b_r,i)
    if r[3]==r_b[3]:
        if r>r_b:
            r_b[2]=(r_b[2][0],r_b[2][1]-1)
        else:
            r[2]=(r[2][0],r[2][1]-1)
    return r,r_b
    

def solution(g_map,R,goal,B):#bfs
    visit=[]
    que=[R]
    b_que=[B]
    pre={R:None}
    c={}
    while len(que)!=0:
        cur=que.pop(0)
        cur_b=b_que.pop(0)
        if cur==goal:
            break
        move(g_map,cur,cur_b)
    
    



x,y=map(int,sys.stdin.readline().split(' '))
g_map=[]
R=''
B=''
goal=''
for i in range(x):
    g_map.append(list(str(sys.stdin.readline())))

for i in range(1,x-1):
    for j in range(1,y-1):
        #(i,j)
        if g_map[i][j]=='O':
            g_map=[i][j]='.'
            goal=(i,j)
        if g_map[i][j]=='R':
            g_map=[i][j]='.'
            R=(i,j)
        if g_map[i][j]=='B':
            g_map=[i][j]='.'
            B=(i,j)         
            