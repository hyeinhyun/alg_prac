#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 19:16:55 2020

@author: hihyun
"""

def oreum(num_list):
    x=len(num_list)
    num_o=[1]*x
    
    for i in range(x):

        for j in range(0,i):#전 기준점
            if num_list[j]<num_list[i]:
                if num_o[i]<num_o[j]+1:
                    num_o[i]=num_o[j]+1
                else:
                    pass
    return num_o

    
    
def naerim(num_list):
    x=len(num_list)
    num_o=[1]*x
    
    for i in range(x):
        i=x-i
        for j in range(i,x):#전 기준점
            if num_list[j]<num_list[i]:
                if num_o[i]<num_o[j]+1:
                    num_o[i]=num_o[j]+1
                else:
                    pass
    return num_o

def solution(o_mat,n_mat,num):
    answer_li=[]
    for i in range(num):
        answer_li.append(o_mat[i]+n_mat[i])
        

    return max(answer_li)-1
            

num=int(input())
num_list=list(map(int,input().split()))
o_mat=oreum(num_list)
n_mat=naerim(num_list)
print(solution(o_mat,n_mat,num))



