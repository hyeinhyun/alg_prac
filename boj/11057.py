#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 10:14:49 2021

@author: hihyun
"""
def solution(N,arr):
    if N==-1:#1
        return 10
    elif N==0:
        return 55
    else:
        for i in range(1,N+1):
            temp=[]
            for j in range(10):
                temp.append(sum(arr[i-1][j:]))
            arr.append(temp)
        return sum(arr[-1])
N=int(input())-2
arr=[[i for i in range(1,11)][::-1]]
print(solution(N,arr)%10007)