#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 23:44:40 2020

@author: hihyun
"""


def solution(num):
    if num==1:
        return 9

    else:
        n=[0,1,1,1,1,1,1,1,1,1]
        for i in range(num-1):
            temp=[n[1],n[0]+n[2],n[1]+n[3],n[2]+n[4],n[3]+n[5],n[4]+n[6],n[5]+n[7],n[6]+n[8],n[7]+n[9],n[8]]
            n=temp
        return sum(n)%1000000000
num=int(input())
print(solution(num))