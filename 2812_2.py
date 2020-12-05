#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 17:44:57 2020

@author: hihyun
"""

n,m=map(int,input().split(' '))
x_l=(list(map(int,input())))
#자릿수 : n-m
before=0
max_val=0
s=''
temp_s=[]
cur_p=n-m
for idx,i in enumerate(x_l):
    tt=min((n-m),len(x_l)-idx)

    if tt!=cur_p:
        s+=str(temp_s.pop(0))
        cur_p=tt
    while True:
        if len(temp_s)==0:
            temp_s.append(i)
            break
        if i>temp_s[-1]:
            temp_s.pop()
        else:
            temp_s.append(i)
            break
if len(list(s))!=n-m:
    s+=str(temp_s.pop(0))
    print(s)
else:
    print(s)