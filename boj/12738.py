#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 11:58:59 2021

@author: hihyun
"""

import sys
import bisect
N=int(input())
l=list(map(int, input().split(' ')))
result=[]
for idx,i in enumerate(l):
    if idx==0:
        result.append(i)
    elif result[-1]<i:
        result.append(i)
    elif result[-1]==i:
        pass
    else:
        #자신의 위치를 찾아가야함.
        idx=bisect.bisect_left(result,i)
        result[idx]=i

print(len(result))