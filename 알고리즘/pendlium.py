#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 17:30:09 2020

@author: hihyun
"""
import sys




def solution(arr,q,T):
    #구 : T(q[0],q[1])
    i=q[0]-1
    j=q[1]-1
    if T[i][j]>0: #값이 있다면,
        return T[i][j]
    if i==j:
        T[i][j]=1

    else:
        if arr[i]==arr[j]:
            if len(arr[i+1:j])==0:
                T[i][j]=1
            elif solution(arr,(q[0]+1,q[1]-1),T)==1:
                T[i][j]=1
            else:
                T[i][j]=0
        else:
            T[i][j]=0
    return T[i][j]

        
    


l=int(input())
arr=list(map(int,sys.stdin.readline().split()))
T=[[-1 for j in range(l)] for i in range(l)]
l2=int(input())
for i in range(l2):
    q=list(map(int,sys.stdin.readline().split()))
    print(solution(arr,q,T))
        