#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 09:19:37 2021

@author: hihyun
"""

"""
def solution(X,Y):
    n=len(X)
    m=len(Y)
    T=[[0 for j in range(m+1)] for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if X[i-1]==Y[j-1]:
                T[i][j]=1+T[i-1][j-1]
            else:
                T[i][j]=max(T[i-1][j],T[i][j-1])
    
    return T[n][m]
        

N=int(input())
l=list(map(int, input().split(' ')))
sl=sorted(list(set(l)))
print(solution(l,sl))
"""
"""
def solution(s,e,t):
    while s<e:
        m=(s+e)//2
        if result[m]>=t:
            s=m+1
        else:
            e=m-1
    return e

N=int(input())
l=list(map(int, input().split(' ')))
result=[]
for idx,i in enumerate(l):
    if idx==0:
        result.append(i)
    elif result[-1]>i:
        result.append(i)
    elif result[-1]==i:
        pass
    else:
        #자신의 위치를 찾아가야함.
        idx=solution(0,len(result)-1,i)
        result[idx]=i
print(len(result))

"""

import bisect


N=int(input())
l=list(map(lambda x : int(x)*-1, input().split(' ')))
result=[]
for idx,i in enumerate(l):
    if idx==0:
        result.append(i)
    elif result[-1]<i:
        result.append(i)
    elif result[-1]==i:
        pass
    else:
        #자신의 위치를 찾아가야함.
        idx=bisect.bisect_left(result,i)
        result[idx]=i
print(len(result))