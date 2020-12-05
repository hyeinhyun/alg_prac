#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 16:13:58 2020

@author: hihyun
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 17:53:59 2020

@author: hihyun
"""
"""
def solution(g):
    q=[(0,0)]
    v=[]
    pre={str((0,0)):None}
    count={str((0,0)):1}
    while len(q)!=0:
        cur=q.pop(0)
        v.append(g[cur[0]][cur[1]])
        if pre[str(cur)] !=None:
            count[str(cur)]=count[pre[str(cur)]]+1
        if cur[0]-1>=0:
            if g[cur[0]-1][cur[1]] not in v:
                q.append((cur[0]-1,cur[1]))
                pre[str((cur[0]-1,cur[1]))]=str(cur)
        if cur[0]+1<r:
            if g[cur[0]+1][cur[1]] not in v:
                q.append((cur[0]+1,cur[1]))
                pre[str((cur[0]+1,cur[1]))]=str(cur)

        if cur[1]-1>=0:
            if g[cur[0]][cur[1]-1] not in v:
                q.append((cur[0],cur[1]-1))
                pre[str((cur[0],cur[1]-1))]=str(cur)

        if cur[1]+1<c:
            if g[cur[0]][cur[1]+1] not in v:
                q.append((cur[0],cur[1]+1))
                pre[str((cur[0],cur[1]+1))]=str(cur)
    print(count)
    return max(count.values())
"""
import collections
max_val=0
# in 의 문제일 확률이 높음
def solution(cur):
    global max_val
    if cur[0]-1>=0:
        if v[str(cur)][g[cur[0]-1][cur[1]]]==False:
            v[str((cur[0]-1,cur[1]))]=v[str(cur)].copy()
            v[str((cur[0]-1,cur[1]))][g[cur[0]-1][cur[1]]]=True
            solution((cur[0]-1,cur[1]))
    if cur[0]+1<r:
        if v[str(cur)][g[cur[0]+1][cur[1]]]==False:
            v[str((cur[0]+1,cur[1]))]=v[str(cur)].copy()
            v[str((cur[0]+1,cur[1]))][g[cur[0]+1][cur[1]]]=True
            solution((cur[0]+1,cur[1]))

    if cur[1]-1>=0:
        if v[str(cur)][g[cur[0]][cur[1]-1]]==False:
            v[str((cur[0],cur[1]-1))]=v[str(cur)].copy()
            v[str((cur[0],cur[1]-1))][g[cur[0]][cur[1]-1]]=True
            solution((cur[0],cur[1]-1))

    if cur[1]+1<c:
        if v[str(cur)][g[cur[0]][cur[1]+1]]==False:
            v[str((cur[0],cur[1]+1))]=v[str(cur)].copy()
            v[str((cur[0],cur[1]+1))][g[cur[0]][cur[1]+1]]=True
            solution((cur[0],cur[1]+1))
    if max_val<len(v[str(cur)]):
        max_val=len(v[str(cur)])

r,c=map(int,input().split(' '))
g=[]
x=collections.defaultdict(bool)
flag=True
for i in range(r):
    temp=(list(input()))
    g.append(temp)
    


xx=x.copy()
xx[g[0][0]]=True
v={str((0,0)):xx}
solution((0,0))
print(max_val)
#print(max(list(map(lambda x:(len(x)), v.values()))))

