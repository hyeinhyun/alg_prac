#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 20:32:15 2020

@author: hihyun
"""


def solution(s):
    x=sorted(list(map(lambda x:x.split(','),s[2:-2].split('},{'))),key=len)
    temp_l=[x[0][0]]
    g=set(x[0])
    for i in x[1:]:
        temp=(set(i)-g).pop()
        g.add(temp)
        temp_l.append(temp)
    answer=list(map(int,temp_l))
    return answer