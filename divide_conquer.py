#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 15:44:14 2019

@author: hihyun
"""

import itertools

def sosu_check(number):
    x=2
    if number==0:
        return False
    if number==1:
        return True
    while True:
        if number%2 ==0:
            if number==x:
                return True
            else:
                return False
        else:
            x+=1

    
def solution(numbers):
    count=0
    list_num=list(numbers)
    len_num=len(list_num)
    result=[]
    for i in range(1,len_num+1):
        x=itertools.permutations(list_num,i)
        for j in list(x):
            s=""
            for k in j:
                s+=k
            result.append(int(s))
    print(result)
    for i in list(set(result)):
        if all([(i%j) for j in range(2, int(i**0.5)+1)]) and i>1 :
            count+=1
    return count


numbers=input()
solution=solution(numbers)

