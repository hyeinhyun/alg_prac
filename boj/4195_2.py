#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 01:11:39 2020

@author: hihyun
"""

import sys
from collections import defaultdict




def is_root(parent_dic,name_li,f_dic):
    if parent_dic[name_li[0]]==0:#no root
        parent_dic[name_li[0]]=name_li[0]
    if parent_dic[name_li[1]]==0:
        parent_dic[name_li[1]]=name_li[1]

def linking(n)



num=int(input())
for i in range(num):
    parent_dic=defaultdict(int)
    f_dic=defaultdict(int)
    net=int(input())
    for j in range(net):
        name_li=sys.stdin.readline().split()
        is_root(parent_dic,name_li,f_dic)#initalize
        linking(name_li,parent,f_dic)
        
        
#parent 잡기
def parent(parent_dic,name_li,f_dic):
    if parent_dic[name_li[0]]==0:#no parent
        parent_dic[name_li[0]]=name_li[0]
        f_dic[name_li[0]]=1
    
    if parent_dic[name_li[1]]==0:
        parent_dic[name_li[1]]=name_li[1]  
        f_dic[name_li[1]]=1
        
def find(parent_dic,name):
    if parent_dic[name]==name:
        return name
    else:
        x=find(parent_dic,parent_dic[name])
        return x


def linking(name_li,parent,f_dic):
    parent1=find(parent_dic,name_li[0])
    parent2=find(parent_dic,name_li[1])
    total=f_dic[parent1]+f_dic[parent2]
    parent_dic[parent2]=parent1
    f_dic[parent1]=total
    print(total)


num=int(input())
for i in range(num):
    parent_dic=defaultdict(int)
    f_dic=defaultdict(int)
    net=int(input())
    for j in range(net):
        name_li=sys.stdin.readline().split()
        parent(parent_dic,name_li,f_dic)#initalize
        linking(name_li,parent,f_dic)
    
    
    