#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 20:27:18 2020

@author: hihyun
"""

from collections import defaultdict
import sys
In = sys.stdin.readline

def find_root(a):
    if root[a]==a:
        return a
    else:
        return find_root(root[a])
def int36(x):
    return int(x, 36)
    
n=int(In())
for i in range(n):
    m=int(In())
    root=defaultdict(str)
    fam=defaultdict(int)
    for j in range(m):
        x,y=input().split(' ')
        x=int36(x)
        y=int36(y)
        if root[x]=='' or root[y]=='':
            if root[x]=='':
                root[x]=x
                fam[x]=1
            if root[y]=='':
                root[y]=y
                fam[y]=1

        root_x=find_root(x)
        root_y=find_root(y)
        if root_x==root_y:
            print(fam[root_x])
        else:
            if fam[root_x]>fam[root_y]:
                root[root_y]=root_x
                fam[root_x]+=fam[root_y]
                print(fam[root_x])
            else:
                root[root_x]=root_y
                fam[root_y]+=fam[root_x]
                print(fam[root_y])            
int36('AAAAA')  
int36('aaaaa')  
