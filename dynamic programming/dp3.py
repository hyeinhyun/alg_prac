#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 20:21:57 2020

@author: hihyun
"""

def fibo1(n):
    r=[0 for i in range(n+1)]
    r[0]=0
    r[1]=1
    for i in range(2,n+1):
        r[i]=r[i-1]+r[i-2]
    return r[n]

fibo1(10)


###b to up

def fibo2(n,r):
    if r[n]>=0:#값을 가지고 잇다면
        return r[n]
    elif n==0:
        val=0
    elif n==1:
        val=1
    else:
        for i in range(2,n+1):
            val=fibo2(i-2,r)+fibo2(i-1,r)
    r[n]=val
    print(r)
    return val
    
fibo2(10,[-1 for i in range(10+1)])


def fibo2(n,r):
    if r[n]>=0:#값을 가지고 잇다면
        return r[n]
    elif n==0:
        r[n]=0
    elif n==1:
        r[n]=1
    else:
        r[n]=fibo2(n-2,r)+fibo2(n-1,r)
    print(r)
    return r[n]
    
fibo2(10,[-1 for i in range(10+1)])
