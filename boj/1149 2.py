#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 18:10:58 2020

@author: hihyun
"""

import sys
##끄으으응

def solution(price,T):
    for i in range(N):
        for j in range(i,N*3):
            if i==j:
                T[i][j]=price[i//3][i%3]
            elif i%3==j%3 and j//3-i//3==1: # 하나차이나는 경우에 같은 값일때
                T[i][j]=1000000
            elif i//3==j//3:#같은 집 다른색깔
                T[i][j]=1000000
            else:
                if j%3 ==0:
                    T[i][j]=price[j//3][j%3]+min(T[(j//3)-1][1],T[(j//3)-1][2])
                elif j%3==1:
                    T[i][j]=price[j//3][j%3]+min(T[(j//3)-1][0],T[(j//3)-1][2])
                else:
                    T[i][j]=price[j//3][j%3]+min(T[(j//3)-1][1],T[(j//3)-1][0])
    print(T)


    return min(T[0][-3:]+T[1][-3:]+T[2][-3:])


N=int(input())
price=[]
for i in range(N):
    price.append(list(map(int,sys.stdin.readline().split())))

T=[[1000000 for i in range(N*3)] for j in range(N*3)]
print(solution(price,T))