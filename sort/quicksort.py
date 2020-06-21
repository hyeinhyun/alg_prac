#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 17:22:44 2020

@author: hihyun
"""


def partition(arr,l,r):
    pivot=arr[r]
    p_idx=l-1
    for j in range(l,r):
        if arr[j]<pivot:
            p_idx+=1
            arr[j],arr[p_idx]=arr[p_idx],arr[j] #swap
    arr[r],arr[p_idx+1]=arr[p_idx+1],arr[r]
    return p_idx+1 #return pivot index

def quicksort(arr,l,r):
    if(l<r):
        p=partition(arr,l,r)
        quicksort(arr,l,p-1)
        quicksort(arr,p+1,r)
    return arr


quicksort([3,2,1,5,7],0,4)
