#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 19:42:01 2020

@author: hihyun
"""

def matrix_chat(p):
    length=len(p)
    m= [[0 for j in range(length)] for i in range(length)]
    s= [[0 for j in range(length-1)] for i in range(length-1)]
    
    for i in range(length):
        m[i,i]=0
    
    for l in range(length):
        m[0,l]+m[l+1:length-1]+p[l-1]*p[l]*p[length-1]
            