#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 13:53:59 2020

@author: hihyun
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 11:30:49 2020

@author: hihyun
"""
from collections import defaultdict,deque
import copy
import sys
def bfs(g):
    d={1:0}
    p={1:None}
    q=deque([1])
    while len(q)!=0:#log(N)
        cur=q.popleft()
        for i in g[cur]:
            q.append(i)
            d[i]=d[cur]+1
            p[i]=cur
    return p,d
    
f=open('./input.txt','r')
num=int(f.readline().strip())

g=defaultdict(list)
for i in range(num-1):
    temp=sorted(list(map(int,f.readline().strip().split(' '))))
    g[temp[0]].append(temp[1])
p,d=bfs(g)

N=int(f.readline().strip())
#N=int(sys.stdin.readline())
for i in range(N):
    temp=sorted(list(map(int,f.readline().strip().split(' '))))
    #x,y=map(int,sys.stdin.readline().split(' '))
    x=d[temp[0]]
    y=d[temp[1]]
    diff=y-x
    x1=temp[0]
    y1=temp[1]
    
    for i in range(diff):
        y1=p[y1]
    if y1==x1:
        continue

    for i in range((x)):
        if p[x1]==p[y1]:
            print(temp[0])
            break
        x1=p[x1]
        y1=p[y1]