#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 20:29:16 2020

@author: hihyun
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 22:34:35 2020

@author: hihyun
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 15:42:41 2020

@author: hihyun
"""

import sys
sys.setrecursionlimit(10000000)

def move(g_map,cur,cur_b):
    p_r,p_c=cur
    b_r,b_c=cur_b
    r=['','','','']
    r_b=['','','','']
    #up
    for i in range(p_r,0,-1):
        if (i,p_c)==goal:
            r[0]=(i,p_c)
            break
        if g_map[i][p_c]=='.':
            r[0]=(i,p_c)
        if g_map[i][p_c]=='#':
            break

        
    for i in range(b_r,0,-1):#자신 포함
        if (i,b_c)==goal:
            r_b[0]=(i,b_c)
            break
        if g_map[i][b_c]=='.':
            r_b[0]=(i,b_c)
        if g_map[i][b_c]=='#':
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
    for i in range(p_r,x):#자신 포함 x
        if (i,p_c)==goal:
            r[1]=(i,p_c)
            break
        if g_map[i][p_c]=='.':
            r[1]=(i,p_c)
        if g_map[i][p_c]=='#':
            break
  
        
    for i in range(b_r,x):#자신 포함
        if (i,b_c)==goal:
            r_b[1]=(i,b_c)
            break
        if g_map[i][b_c]=='.':
            r_b[1]=(i,b_c)
        if g_map[i][b_c]=='#':
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
    for i in range(p_c,0,-1):#자신 포함 x
        if (p_r,i)==goal:
            r[2]=(p_r,i)
            break
        if g_map[p_r][i]=='.':
            r[2]=(p_r,i)
        if g_map[p_r][i]=='#':
            break

        
    for i in range(b_c,0,-1):#자신 포함
        if (b_r,i)==goal:
            r_b[2]=(b_r,i)
            break
        if g_map[b_r][i]=='.':
            r_b[2]=(b_r,i)
        if g_map[b_r][i]=='#':
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
    for i in range(p_c,y):#자신 포함 x
        if (p_r,i)==goal:
            r[3]=(p_r,i)
            break

        if g_map[p_r][i]=='.':
            r[3]=(p_r,i)
        if g_map[p_r][i]=='#':
            break

        
    for i in range(b_c,y):#자신 포함
        if (b_r,i)==goal:
            r_b[3]=(b_r,i)
            break

        if g_map[b_r][i]=='.':
            r_b[3]=(b_r,i)
        if g_map[b_r][i]=='#':
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
    q=[(s,B)]
    c={str((s,B)):0}
    #q_b=[B]
    v=[(s,B)]
    pre={str((s,B)):None}
    temp_b=''
    while len(q)!=0:
        cur_li=q.pop(0)
        cur=cur_li[0]
        cur_b=cur_li[1]


        if pre[str((cur,cur_b))] !=None:
            c[str((cur,cur_b))]=c[pre[str((cur,cur_b))]]+1
        
        if cur==goal:
            temp_b=cur_b
            break
        if cur_b==goal:
            continue


        r,r_b=move(g_map,cur,cur_b)

        for x,y in zip(r,r_b):
            if x=='':
                pass
            if y==goal:
                pass
            else:
                if (x,y) not in v:
                    q.append((x,y))
                    pre[str((x,y))]=str((cur,cur_b))
                    v.append((x,y))
    if temp_b==goal:
        return -1
    new_c=[]
    for i in c.keys():
        cc='('+i[2:-2].split('), (')[0]+')'
        new_c.append(cc)
    min_val=100000
    if str(goal) in new_c:
        for i in c:
            cc='('+i[2:-2].split('), (')[0]+')'
            if cc==str(goal):
                if c[i]<=10:
                    if min_val>c[i]:
                        min_val=c[i]
                else:
                    return -1
        return min_val
    else:
        return -1

        
    

    
f = open("./input.txt", 'r')

x,y=map(int,f.readline().strip().split(' '))
g_map=[]
R=''
B=''
goal=''
for i in range(x):
    g_map.append(list(str(f.readline().strip())))

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


