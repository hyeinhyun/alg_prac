#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 16:53:19 2020

@author: hihyun
"""

def solution(s:str):
    suffix=[]
    for c in range (len(s)):
        suffix.append(s[c:])
    return sorted(list(suffix))

s=input()
for i in solution(s):
    print(i)