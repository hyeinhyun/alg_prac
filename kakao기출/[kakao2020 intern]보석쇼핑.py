#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 15:29:18 2021

@author: hihyun
"""

def solution(gems):
    min_val=[1000000,[0,0]]
    s=set(gems)
    l=len(gems)
    sp=-1
    ep=0
    while ep<l:
        if sp==-1:
            sp+=1
        else:
                    ep+=1

            print(sp)
            if gems[ep]==gems[sp]:
                sp+=1
            while gems[sp]==gems[sp+1]:
                sp+=1
        if len(gems[sp:ep+1])<min_val[0]:
            if set(gems[sp:ep+1])==s:
                min_val[0]=len(gems[sp:ep+1])
                min_val[1]=[sp,ep]
    return 0

solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])