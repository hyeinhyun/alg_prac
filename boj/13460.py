#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 14:11:17 2020

@author: hihyun
"""
import sys

def solution(s,e,g_node):
    q=[s]
    v=[]
    c={s:0}
    pre={s:None}
    while len(q)!=0:
        cur=q.pop(0)
        if pre[cur] !=None:
            c[cur]=c[pre[cur]]+1
        v.append(q)
        if cur==e:
            break
        else:
            q+=g_node[cur]
            for i in g_node[cur]:
                pre[i]=cur
    return c,pre
    
answer=0
x,y=map(int,sys.stdin.readline().split(' '))
g_map=[]
g_node={}
R=''
B=''
goal=''
for i in range(x):
    g_map.append(list(str(sys.stdin.readline())))

for i in range(1,x-1):
    for j in range(1,y-1):
        #(i,j)
        if g_map[i][j]=='.':
            if g_map[i-1][j]=='#' or g_map[i+1][j]=='#':
                if g_map[i][j-1]=='#' or g_map[i][j+1]=='#':
                    g_node[str((i,j))]=[]
        if g_map[i][j]=='O':
            g_node[str((i,j))]=[]
            goal=str((i,j)) 
        if g_map[i][j]=='R':
            g_node[str((i,j))]=[]  
            R=str((i,j))
        if g_map[i][j]=='B':
            g_node[str((i,j))]=[]  
            B=str((i,j))            
            
for i in g_node.keys():# 나중에 반으로 나눠도 됨
    r,c=map(int,i[1:-1].split(','))
    for k in range(r,x-1):
        if g_map[k][c]=='#':
            break
        if str((k,c)) != i and str((k,c)) in g_node.keys():
            g_node[i].append(str((k,c)))
            g_node[str((k,c))].append(i)
            break
    for k in range(c,y-1):
        if g_map[r][k]=='#':
            break
        if str((r,k)) != i and str((r,k)) in g_node.keys():
            g_node[i].append(str((r,k)))
            g_node[str((r,k))].append(i)
            break
c,pre=solution(R,goal,g_node)
if c[goal]>10:
    answer=-1
else:
    answer=c[goal]
    root=[]
    prev=goal
    while prev!=R:
        if len(root)>10:
            break
        cur=pre[prev]
       
        cx,cy=map(int,prev[1:-1].split(','))
        ccx,ccy=map(int,cur[1:-1].split(','))
        if ccx-cx>0:#up
            root.append('u')
        if ccx-cx<0:#down
            root.append('d')
        if ccy-cy>0:#left
            root.append('l')
        if ccy-cy<0:#right
            root.append('r')
        prev=cur
    root=root[::-1]
    if len(root)<=10:
        for i in root:
            if cur==goal:
                answer=-1
                break
            cur=B
            if i=='u':
                for j in g_node[cur]:
                    if j==R:
                        pass
                    if list(map(int,cur[1:-1].split(',')))[0]-list(map(int,j[1:-1].split(',')))[0]>0:
                        cur=j
                    else:
                        break
            if i=='d':
                for j in g_node[cur]:
                    if j==R:
                        pass
                    if list(map(int,cur[1:-1].split(',')))[0]-list(map(int,j[1:-1].split(',')))[0]<0:
                        cur=j
                    else:
                        break
            if i=='l':
                for j in g_node[cur]:
                    if j==R:
                        pass
                    if list(map(int,cur[1:-1].split(',')))[1]-list(map(int,j[1:-1].split(',')))[1]>0:
                        cur=j
                    else:
                        break
            if i=='r':
                for j in g_node[cur]:
                    if j==R:
                        pass
                    if list(map(int,cur[1:-1].split(',')))[1]-list(map(int,j[1:-1].split(',')))[1]<0:
                        cur=j
                    else:
                        break
            
print(answer)


