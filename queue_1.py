#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 15:05:13 2019

@author: hihyun
"""



def solution(priorities, location):
    print_data=[]
    for i in enumerate(priorities):
        print_data.append(i)
    x=-1
    count=0
    while x != location:
        check=print_data.pop(0)
        if any(check[1]<q[1] for q in print_data):
            print_data.append(check)
        else:
            x=check[0]
            count+=1

    return count

location=int(input())
priorities=[]
try:
    while True:
        priorities.append(int(input()))
except:
    solution(priorities, location)