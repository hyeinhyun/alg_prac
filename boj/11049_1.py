#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 14:59:48 2020

@author: hihyun
"""

import sys
sys.setrecursionlimit(10000000)

num=int(sys.stdin.readline())
matrix=[]
for i in range(num):
    matrix.append(list(map(int,sys.stdin.readline().split())))

answer_mat=[[2**31 - 1 for i in range(num)] for i in range(num) ]
if num==1:
    print(0)
else:
    for m in range(1,num):
        for n in range(0,num-m):
            i=n
            j=m+n
            if j-i==1:
                answer_mat[i][j]=matrix[i][0]*matrix[i][1]*matrix[j][1]
                continue
            answer_mat[i][j]=min([answer_mat[i+(j-k+1)][j]+answer_mat[i][j-k]+matrix[i][0]*matrix[j-k][1]*matrix[j][1] for k in range(1,j)])
    print(answer_mat[0][num-1])  

