#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 21:28:23 2020

@author: hihyun
"""

def lcs1(X,Y):
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

lcs1(["A","C","B"],["A","B","C"])


def lcs2(X,Y,T):
    n=len(X)
    m=len(Y)
    if T[n][m]>=0: #값이 있다면
        return T[n][m]
    elif n==0 or m==0:
        T[n][m]=0
    else:
        for i in range(1,n+1):
            for j in range(1,m+1):
                if X[i-1]==Y[j-1]:
                    val=1+lcs2(X[:(i-1)],Y[:(j-1)],T)
                else:
                    val=max(lcs2(X[:(i-1)],Y[:j],T),lcs2(X[:i],Y[:(j-1)],T))
                T[i][j]=val
    return T[n][m]




def lcs2(X,Y,T):
    n=len(X)
    m=len(Y)
    if T[n][m]>=0: #값이 있다면
        return T[n][m]
    elif n==0 or m==0:
        T[n][m]=0
    else:

        if X[n-1]==Y[m-1]:
            T[n][m]=1+lcs2(X[:(n-1)],Y[:(m-1)],T)
        else:
            T[n][m]=max(lcs2(X[:(n-1)],Y[:m],T),lcs2(X[:n],Y[:(m-1)],T))

    return T[n][m]






lcs2(["A","C","B"],["A","B","C"],[[-1 for j in range(4)] for i in range(4)])

X

T=[[0 for j in range(4)] for i in range(4)]
len([])
a=["A","C","B"]
a[:0]
[[-1 for j in range(4)] for i in range(4)]
