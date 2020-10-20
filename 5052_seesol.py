#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 22:22:46 2020

@author: hihyun
"""


import sys
sys.setrecursionlimit(10000)
def solution(num_list):
    answer='YES'
    for i in range(len(num_list)-1):
        if num_list[i] in num_list[i+1][:len(num_list[i])]:
            answer='NO'
            break
    return answer



num=int(sys.stdin.readline())
for i in range(num):
    temp=int(int(sys.stdin.readline()))
    num_list=[]
    for j in range(temp):
        num_list.append(str(sys.stdin.readline().strip()))
    print(solution(sorted(num_list)))
        