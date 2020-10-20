#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 16:50:58 2020

@author: hihyun
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 00:03:48 2020

@author: hihyun
"""

import copy
def solution(j,g_map_r): #i==cur g_map_r=cur_g
    global max_val
    g_map=copy.deepcopy(g_map_r)
    if j=='u':
        for k in range(x):
            temp=[]
            zeros=[]
            pre=[]
            pre_zeros=[]
            for n in range(x):
                i=g_map[n][k]
                if i!=0:
                    pre.append(i)
                else:
                    pre_zeros.append(0)
            pre+=pre_zeros
            print(pre)
            for kk in range(x):
                if kk+1<x:
                    if pre[kk]==pre[kk+1]:
                        pre[kk]*=2
                        pre[kk+1]=0
                        if pre[kk]>max_val:
                            max_val=pre[kk]
                if pre[kk]!=0:
                    temp.append(pre[kk])
                else:
                    zeros.append(0)
            temp+=zeros
            for idx,i in enumerate(temp):
                g_map[idx][k]=i
            

                        

    if j=='d':
        for k in range(x):
            temp=[]
            zeros=[]
            pre=[]
            pre_zeros=[]

            for n in range(x):
                i=g_map[n][k]
                if i!=0:
                    pre.append(i)
                else:
                    pre_zeros.append(0)
            pre+=pre_zeros
            for kk in range(x-1,-1,-1):
                if kk-1>=0:
                    if pre[kk]==pre[kk-1]:
                        pre[kk]*=2
                        pre[kk-1]=0
                        if pre[kk]>max_val:
                            max_val=pre[kk]
                if pre[kk]!=0:
                    temp.append(pre[kk])
                else:
                    zeros.append(0)
            temp+=zeros
            for idx,i in enumerate(temp[::-1]):
                g_map[idx][k]=i


    if j=='l':
        for k in range(x):
            temp=[]
            zeros=[]
            pre=[]
            pre_zeros=[]
            for i in g_map_r[:][k]:
                if i!=0:
                    pre.append(i)
                else:
                    pre_zeros.append(0)
            pre+=pre_zeros
            for kk in range(x):
                if kk+1<x:
                    if pre[kk]==pre[kk+1]:
                        pre[kk]*=2
                        pre[kk+1]=0
                        if pre[kk]>max_val:
                            max_val=pre[kk]

                if pre[kk]!=0:
                    temp.append(pre[kk])
                else:
                    zeros.append(0)
            temp+=zeros
            g_map[k][:]=temp

    if j=='r':
        for k in range(x):
            temp=[]
            zeros=[]
            pre=[]
            pre_zeros=[]
            for i in g_map_r[:][k]:
                if i!=0:
                    pre.append(i)
                else:
                    pre_zeros.append(0)
            pre+=pre_zeros
            for kk in range(x-1,-1,-1):
                if kk-1>=0:
                    if pre[kk]==pre[kk-1]:
                        pre[kk]*=2
                        pre[kk-1]=0
                        if pre[kk]>max_val:
                            max_val=pre[kk]
                if pre[kk]!=0:
                    temp.append(pre[kk])
                else:
                    zeros.append(0)
            temp+=zeros
            g_map[k][:]=temp[::-1]

    return g_map




def bfs(g_map):
    q=['u','d','l','r']
    g=[g_map,g_map,g_map,g_map]
    count=0
    while count<5 and len(q)!=0:
        for i in range(len(q)):
            cur=q.pop(0)#방향
            g_cur=g.pop(0)
            new_g=solution(cur,g_cur)
            print('==')
            print(new_g)
            if g_cur !=new_g:
                q.append('u')
                q.append('d')
                q.append('l')
                q.append('r')
                g.append(new_g)
                g.append(new_g)
                g.append(new_g)
                g.append(new_g)
        
        count+=1

    










f = open("./input.txt", 'r')

x=int(f.readline().strip())
g_map=[]
max_val=0
for i in range(x):
    temp=list(map(int,f.readline().strip().split()))
    g_map.append(temp)
    for j in temp:
        if max_val<j:
            max_val=j
 

#dir_li=list(product(dir_key,repeat=5))

        
bfs(g_map)
print(max_val)
