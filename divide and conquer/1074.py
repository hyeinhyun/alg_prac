#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 18:45:42 2020

@author: hihyun
"""

def dq2(N,r,c):

    if N==1:
        if r%2==0 and c%2==0:
            return 0
        elif r%2==0 and c%2==1:
            return 1
        elif r%2==1 and c%2==0:
            return 2
        else:
            return 3
    else:
        n=N-1
        m=2**n
        if r//m==0 and c//m==0:#상대적 1에 위치
            result= 0*(m*m)+dq2(n,r,c)
            
        elif r//m==0 and c//m==1:#상대적 2에 위치

            result= 1*(m*m)+dq2(n,r,c-m)
            
        elif r//m==1 and c//m==0:
            result= 2*(m*m)+dq2(n,r-m,c)
            
        else:

            result= 3*(m*m)+dq2(n,r-m,c-m)
    
    #combine
    return result

  
x=input().strip().split()
print(dq2(int(x[0]),int(x[1]),int(x[2])))    
