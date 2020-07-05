#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 20:39:48 2020

@author: hihyun
"""
import sys
def solution(name_set,set_list):
    temp=[]
    for idx,s in enumerate(set_list):
        if len(s&name_set)!=0:
            temp.append(idx)
    if len(temp)>1:
        s1=set_list[temp[0]]
        s2=set_list[temp[1]]
        s=s1.union(s2)
        set_list[temp[0]]=s
        del set_list[temp[1]]
        return len(s)
    elif len(temp)==1:
        s=set_list[temp[0]]
        s=s.union(name_set)
        set_list[temp[0]]=s #exchange
        return len(s)
    else:
        set_list.append(name_set)
        return 2

name_dict={}
num=int(input())
for i in range(num):
    x=int(input())
    set_list=[]
    count=0
    for j in range(x):
        name_li=sys.stdin.readline().split()
        for k in name_li:
            try:
                name_dict[k]
                pass
            except:
                name_dict[k]=count
                count+=1
        print(solution({name_dict[name_li[0]],name_dict[name_li[1]]},set_list))




