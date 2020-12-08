#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 16:45:33 2020

@author: hihyun
"""

def is_element(string):
    if len(string)==1:
        return True
    else:
        return is_set(string)
def is_list(string):
    if is_element(string):
        return True
    if ','  in string:
        N=len(string.split(','))
        for i in range(N):
            if is_element(string.split(',')[i]) and is_list(string.split(',')[i+1:]):
                print(is_element(string.split(',')[i]) and is_list(string.split(',')[i+1:]))
                return is_element(string.split(',')[i]) and is_list(string.split(',')[i+1:])
    else:
        return False

def is_elementlist(string):
    if string=='':
        return True
    else:
        return is_list(string)

def is_set(string):
    if len(string)>=2:
        if string[0]=="{" and string[-1]=="}":
            return is_elementlist(string[1:-1])
        else:
            return False
    else:
        return False

def solution(string):
    results.append(is_set(string))

num=int(input())
for i in range(num):
    results=[]
    solution(input())
    print(results)
    if 1:
        print("Word #{}: Set".format(i+1))
    else:
        print("Word #{}: No Set".format(i+1))