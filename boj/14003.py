#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 11:08:45 2021

@author: hihyun
"""

import sys
import bisect
N=int(input())
l=list(map(int, input().split(' ')))
result=[]
ans=[]#후보군들을 다 모아둠.
for idx,i in enumerate(l):
    if idx==0:
        result.append(i)
        ans.append((0,i))
    elif result[-1]<i:
        result.append(i)
        ans.append((len(result)-1,i))
    elif result[-1]==i:
        pass
    else:
        #자신의 위치를 찾아가야함.
        idx=bisect.bisect_left(result,i)
        result[idx]=i
        ans.append((idx,i))

print(len(result))
t=len(result)
s=[]
for idx,i in ans[::-1]:
    if idx==t-1:
        s.append(i)
        t-=1
print(' '.join(list(map(str,s[::-1]))))
