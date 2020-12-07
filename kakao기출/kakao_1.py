#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 13:57:56 2020

@author: hihyun
"""
source='abdh'
target='bcif'
s_l=list(map(lambda x:ord(x),list(source)))
t_l=list(map(lambda x:ord(x),list(target)))
for i    count=0
    s_d=[]
    for i in range(len(list(source))-1):
        s_d=ord(list(source)[i])-ord(list(source)[i+1])
        t_d=ord(list(target)[i])-ord(list(target)[i+1])
        if s_d!=t_d:
            count+=1
    return count*2