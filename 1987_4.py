#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 13:11:37 2020

@author: hihyun
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 17:02:12 2020

@author: hihyun
"""

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
max_val=0
# in 의 문제일 확률이 높음
def solution(cur,xx,m):
    global max_val
    if cur[0]-1>=0:
        if xx[ord(g[cur[0]-1][cur[1]])-65]==0:
            xx[ord(g[cur[0]-1][cur[1]])-65]=1
            solution((cur[0]-1,cur[1]),xx,m+1)
            xx[ord(g[cur[0]-1][cur[1]])-65]=0

    if cur[0]+1<r:
        if xx[ord(g[cur[0]+1][cur[1]])-65]==0:
            xx[ord(g[cur[0]+1][cur[1]])-65]=1
            solution((cur[0]+1,cur[1]),xx,m+1)
            xx[ord(g[cur[0]+1][cur[1]])-65]=0

                
    if cur[1]-1>=0:
        if xx[ord(g[cur[0]][cur[1]-1])-65]==0:
           xx[ord(g[cur[0]][cur[1]-1])-65]=1
           solution((cur[0],cur[1]-1),xx,m+1)
           xx[ord(g[cur[0]][cur[1]-1])-65]=0

                
    if cur[1]+1<c:
        if xx[ord(g[cur[0]][cur[1]+1])-65]==0:
            xx[ord(g[cur[0]][cur[1]+1])-65]=1
            solution((cur[0],cur[1]+1),xx,m+1)
            xx[ord(g[cur[0]][cur[1]+1])-65]=0

    if max_val<m:
        max_val=m
                
r,c=map(int,input().split(' '))
g=[]
for i in range(r):
    temp=(list(input()))
    g.append(temp)

x=[0]*26
x[ord(g[0][0])-65]=1
solution((0,0),x,1)
print(max_val)
#print(max(list(map(lambda x:(len(x)), v.values()))))

