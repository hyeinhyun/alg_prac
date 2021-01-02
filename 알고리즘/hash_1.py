#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 16:52:32 2019

@author: hihyun
"""

def solution(phone_book):
    phone_book=sorted(phone_book,key=len)
    #sort가 되었다고 가정
    for i in phone_book:
        count=0
        for j in phone_book:
            try:
                if i==j[:len(i)]:
                    count+=1
                if count >1:
                    return "NO"
            except:
                pass
    return "YES"

case=int(input())
answer=[]
for i in range(case):
    phone_book=[]
    num1=int(input())
    for j in range(num1):
        a=input()
        phone_book.append(a)
    answer.append(solution(phone_book))
for i in answer:
    print(i)

a=[1,2]
for i in a:
    print(i)