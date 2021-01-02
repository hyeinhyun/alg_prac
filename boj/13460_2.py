#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 15:42:41 2020

@author: hihyun
"""

import sys
sys.setrecursionlimit(10000000)

def move(g_map,cur,cur_b):
    print(cur)
    p_r,p_c=cur
    b_r,b_c=cur_b
    r=['','','','']
    r_b=['','','','']
    #up
    for i in range(p_r-1,0,-1):#자신 포함 x
        if g_map[i][p_c]=='#':
            break
        if g_map[i][p_c]=='.':
            r[0]=(i,p_c)
        if (i,p_c)==goal:
            r[0]=(i,p_c)
            break
    for i in range(b_r,0,-1):#자신 포함
        if g_map[i][b_c]=='#':
            break
        if g_map[i][b_c]=='.':
            r_b[0]=(i,b_c)
        if (i,b_c)==goal:
            r_b[0]=(i,b_c)
            break
    if r[0]==r_b[0]:
        if r[0]==goal:
            pass
        else:
            if p_r>b_r:
                r[0]=(r[0][0]+1,r[0][1])
            else:
                r_b[0]=(r_b[0][0]+1,r_b[0][1])
    #down
    for i in range(p_r+1,x):#자신 포함 x
        if g_map[i][p_c]=='#':
            break
        if g_map[i][p_c]=='.':
            r[1]=(i,p_c)
        if (i,p_c)==goal:
            r[1]=(i,p_c)
            break
    for i in range(b_r,x):#자신 포함
        if g_map[i][b_c]=='#':
            break
        if g_map[i][b_c]=='.':
            r_b[1]=(i,b_c)
        if (i,b_c)==goal:
            r_b[1]=(i,b_c)
            break
    if r[1]==r_b[1]:
        if r[1]==goal:
            pass
        else:
            if p_r>b_r:
                r_b[1]=(r_b[1][0]-1,r_b[1][1])
            else:
                r[1]=(r[1][0]-1,r[1][1])
    #left            
    for i in range(p_c-1,0,-1):#자신 포함 x
        if g_map[p_r][i]=='#':
            break
        if g_map[p_r][i]=='.':
            r[2]=(p_r,i)
        if (p_r,i)==goal:
            r[2]=(p_r,i)
            break
    for i in range(b_c,0,-1):#자신 포함
        if g_map[b_r][i]=='#':
            break
        if g_map[b_r][i]=='.':
            r_b[2]=(b_r,i)
        if (b_r,i)==goal:
            r_b[2]=(b_r,i)
            break
    if r[2]==r_b[2]:
        if r[2]==goal:
            pass
        else:
            if p_c>b_c:
                r[2]=(r[2][0],r[2][1]+1)
            else:
                r_b[2]=(r_b[2][0],r_b[2][1]+1)
            
    #right            
    for i in range(p_c+1,y):#자신 포함 x
        if g_map[p_r][i]=='#':
            break
        if g_map[p_r][i]=='.':
            r[3]=(p_r,i)
        if (p_r,i)==goal:
            r[3]=(p_r,i)
            break
    for i in range(b_c,y):#자신 포함
        if g_map[b_r][i]=='#':
            break
        if g_map[b_r][i]=='.':
            r_b[3]=(b_r,i)
        if (b_r,i)==goal:
            r_b[3]=(b_r,i)
            break
    if r[3]==r_b[3]:
        if r[3]==goal:
            pass
        else:
            if p_c>b_c:
                r_b[3]=(r_b[3][0],r_b[3][1]-1)
            else:
                r[3]=(r[3][0],r[3][1]-1)
    return r,r_b
        
def solution(s,e,g_map,B):
    q=[s]
    c={str(s):0}
    q_b=[B]
    v=[]
    pre={str(s):None}

    while len(q)!=0:

        cur=q.pop(0)
        cur_b=q_b.pop(0)

        if pre[str(cur)] !=None:
            c[str(cur)]=c[pre[str(cur)]]+1
        v.append(cur)

        if cur==goal:
            break

        r,r_b=move(g_map,cur,cur_b)
        for x,y in zip(r,r_b):
            if x=='':
                pass
            else:
                if x not in v:
                    q.append(x)
                    pre[str(x)]=str(cur)
                    q_b.append(y)
    if cur_b==goal:
        return -1
    if str(goal) in c.keys():
        if c[str(goal)]<=10:
            return c[str(goal)]
        else:
            return -1
    else:
        return -1

        



    

    
x,y=map(int,input().split(' '))
g_map=[]
R=''
B=''
goal=''
for i in range(x):
    g_map.append(list(str(input())))

for i in range(1,x-1):
    for j in range(1,y-1):
        #(i,j)
        if g_map[i][j]=='O':
            g_map[i][j]='.'
            goal=(i,j)
        if g_map[i][j]=='R':
            g_map[i][j]='.'
            R=(i,j)
        if g_map[i][j]=='B':
            g_map[i][j]='.'
            B=(i,j)       
            


print(solution(R,goal,g_map,B))



