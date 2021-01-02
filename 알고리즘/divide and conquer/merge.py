#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 20:44:55 2020

@author: hihyun
"""

def merge(list):
    length=len(list)
    if length<=1: #itialize
        return list
    
    #divide
    g1=merge(list[:length//2])
    g2=merge(list[length//2:])
    #conquer
    sorted=[]
    while g1 and g2:
        if g1[0]<=g2[0]:
            sorted.append(g1[0])
            g1=g1[1:]
        elif g1[0]>g2[0]:
            sorted.append(g2[0])
            g2=g2[1:]
    if g1:
        sorted=sorted+g1
    if g2:
        sorted=sorted+g2
    return sorted

merge([5,9,3,2,1])


def merge2(list,l,r,mid):
    l_li=list[l:mid+1]
    r_li=list[mid+1:r+1]
    l_li.append(1000000) #infinity
    r_li.append(1000000) #infinity
    l_idx=0
    r_idx=0
    for i in range(l,r+1):
        if l_li[l_idx]<=r_li[r_idx]:
            list[i]=l_li[l_idx]
            l_idx+=1
        else:
            list[i]=r_li[r_idx]
            r_idx+=1
            

def mergesort(list,l,r):
    if(l<r):
        mid=(l+r)//2
        mergesort(list,l,mid)
        mergesort(list,mid+1,r)
        merge2(list,l,r,mid)
    return list
        
mergesort([5,9,3,2,1],0,4)
   
    