#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 21:32:36 2020

@author: hihyun
"""
import sys
def solution(val):
    answer=[0]
    for i in range(1,val+1):
        if i==1:
            answer.append(0)
        else:
            cand1=100000000
            cand2=100000000
            cand3=100000000
            if i-1>=1:
                cand1=answer[i-1]+1
            if i%2==0:
                cand2=answer[i//2]+1
            if i%3==0:
                cand3=answer[i//3]+1
            answer.append(min([cand1,cand2,cand3]))
    return answer[-1]


def solution2(val,answer):
    if val==0:
        return 0
    elif val==1:
        return 0
    elif answer[val] !=1000000:
        return answer[val]
    
    else:
        answer[val]=min(solution2(val//2,answer)+val%2+1,solution2(val//3,answer)+val%3+1)
        


    return answer[val]


val=int(sys.stdin.readline())
answer=[1000000 for i in range (val+1)]
print(solution2(val,answer))