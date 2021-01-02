#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 23:56:14 2020

@author: hihyun
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 19:29:34 2020

@author: hihyun
"""
def solution(pos):
    q=[pos]
    v=[[0]*m for i in range(n)]
    v[pos[0]][pos[1]]=1
    c={str(pos):1,str((n-1,m-1)):1000000}
    pre={str(pos):None}
    wall={str(pos):0}

    r=[-1,1,0,0]
    col=[0,0,-1,1]
    while len(q)!=0:
        cur=q.pop(0)
        if pre[str(cur)] is not None:
                c[str(cur)]=c[str(pre[str(cur)])]+1
        for i in range(4):
            if cur[0]+r[i]>=0 and cur[0]+r[i]<n and cur[1]+col[i]>=0 and cur[1]+col[i]<m:
                if g[cur[0]+r[i]][cur[1]+col[i]]==1:
                    if v[cur[0]+r[i]][cur[1]+col[i]]==0:
                        if wall[str(cur)]==0:
                            q.append((cur[0]+r[i],cur[1]+col[i]))
                            pre[str((cur[0]+r[i],cur[1]+col[i]))]=cur
                            wall[str((cur[0]+r[i],cur[1]+col[i]))]=1

                else:#g[][]==0
                    if v[cur[0]+r[i]][cur[1]+col[i]]==0:
                        q.append((cur[0]+r[i],cur[1]+col[i]))
                        v[cur[0]+r[i]][cur[1]+col[i]]=1
                        pre[str((cur[0]+r[i],cur[1]+col[i]))]=cur
                        wall[str((cur[0]+r[i],cur[1]+col[i]))]=wall[str(cur)]
            print(wall)
    return c[str((n-1,m-1))]
t=open('./input.txt')
n,m=map(int,t.readline().strip().split(' '))
g=[]
for i in range(n):
    g.append(list(map(int,list(t.readline().strip()))))

min_val=solution((0,0))

if min_val==1000000:
    print(-1)
else:
    print(min_val)