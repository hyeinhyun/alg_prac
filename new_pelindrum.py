#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 18:44:33 2020

@author: hihyun
"""
import sys

l=int(input())
arr=list(map(int,sys.stdin.readline().split()))
T=[[-1 for j in range(l)] for i in range(l)]
for j in range(l):
    for i in range(l):
        if (i<=j):
            if i==j:
                T[i][j]=1
            else:
                if arr[i]==arr[j]:
                    if (i+1)>(j-1):
                        T[i][j]=1
                    elif T[i+1][j-1]==1:
                        T[i][j]=1
                    else:
                        T[i][j]=0
                else:
                    T[i][j]=0
l2=int(input())
for i in range(l2):
    q=list(map(int,sys.stdin.readline().split()))
    print(T[q[0]-1][q[1]-1])
    