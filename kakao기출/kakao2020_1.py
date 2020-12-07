#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 20:19:00 2020

@author: hihyun
"""

from collections import defaultdict
def solution(board, moves):
    count=0
    d=[-1]
    list_dic=defaultdict(list)
    length=len(board)
    for i in board[::-1]:
        for j in range(length):
            if i[j]!=0:
                list_dic[j].append(i[j])
    for i in moves:
        if len(list_dic[i-1])!=0:
            temp=list_dic[i-1].pop()
            if d[-1]==temp:
                d.pop()
                count+=2
            else:
                d.append(temp)
    answer = count
    return answer