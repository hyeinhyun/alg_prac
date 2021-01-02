#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 20:38:53 2020

@author: hihyun
"""
import sys

def solution(f1,f2,root_val,f1_su,f2_su,root_dict):
    root_val[f1_su]+=root_val[f2_su]
    root_dict[f2_su]=f1_su
    return root_val[f1_su]

def find_su(f,root_dict):
    while root_dict[f]!=f:
        f=root_dict[f]
    return root_dict[f]


q=int(input())
for i in range(q):
    net=int(input())
    root_val={}
    root_dict={}
    for j in range(net):
        f1,f2=input().split()
        if f1 not in root_val.keys():
            root_val[f1]=1
            root_dict[f1]=f1
            
        if f2 not in root_val.keys():
            root_val[f2]=1
            root_dict[f2]=f2
        f1_su=find_su(f1,root_dict)
        f2_su=find_su(f2,root_dict)
        print(solution(f1,f2,root_val,f1_su,f2_su,root_dict))
        #print('\n')
