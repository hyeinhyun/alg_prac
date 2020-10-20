#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 21:57:51 2020

@author: hihyun
"""

def oreum(num_list):
    x=len(num_list)
    num_o=[1]*x
    prev=[0]*x
    
    for i in range(x):
        if i==0:

        for j in range(0,i):#전 기준점
            if num_list[j]<num_list[i]:
                if num_o[i]<num_o[j]+1:
                    num_o[i]=num_o[j]+1
                    prev[i]=j
                    
                else:
                    pass
    max_val=0
    max_idx=0
    for idx,i in enumerate(num_o):
        if i>max_val:
            max_val=i
            max_idx=idx
    return max_val,max_idx,num_o
num=int(input())
num_list=list(map(int,input().split()))
max_val,max_idx,num_o=oreum(num_list)
print(max_val)
for i in 
