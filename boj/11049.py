#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 10:55:06 2020

@author: hihyun
"""
import sys
sys.setrecursionlimit(1000)

def solution(matrix,num):
    answer_mat=[[0 for i in range(num)] for i in range(num) ]
    for m in range(1,num):
        for n in range(0,num-m):
            i=n
            j=m+n
            #order_li.append((i,j))
            if j-i==1:
                answer_mat[i][j]=matrix[i][0]*matrix[i][1]*matrix[j][1]
                continue

            min_val=2**31 - 1
            for k in range(1,j):
                if min_val>answer_mat[i+(j-k+1)][j]+answer_mat[i][j-k]+matrix[i][0]*matrix[j-k][1]*matrix[j][1]:
                    min_val=answer_mat[i+(j-k+1)][j]+answer_mat[i][j-k]+matrix[i][0]*matrix[j-k][1]*matrix[j][1]

                answer_mat[i][j]=min_val
    return answer_mat[0][num-1]
                    

num=int(sys.stdin.readline())
matrix=[]
for i in range(num):
    matrix.append(list(map(int,sys.stdin.readline().split())))
print(solution(matrix,num))