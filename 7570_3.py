#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 01:44:16 2020

@author: hihyun
"""


        

num=int(input())
c=list(map(int,input().split()))
list_c={}
for idx,i in enumerate(c):
    list_c[i]=idx
    
dp=[1]*len(c)

for i in range(1,len(c)):
    if list_c[i]<list_c[i+1]:
        dp[i]=dp[i-1]+1
print(len(c)-max(dp))
