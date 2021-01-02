#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 21:29:50 2020

@author: hihyun
"""

import sys
#num=int(sys.stdin.readline())
num=int(input())
g=[0]*(num*2+1)

total=1
for i in range(num-1):
    total+=(2*i+1)




print(((g[1])+1)%9901)