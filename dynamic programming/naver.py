#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 19:04:11 2020

@author: hihyun
"""

import sys   

def solution(x,visit,fevertime):
    for idx,i in enumerate(x):
        if i[0]==0:
            visit.append(i)
        else:
            visit.append(i)
            
            for i in range(10):
                solution(x[idx:],visit,i[0]+1*idx+0.5)







a=input().split('],[')
a[0]=a[0][2:]
a[-1]=a[-1][:-2]
x=[]
for i in (a):
    x.append(list(map(int,i.split(','))))
solution(x)