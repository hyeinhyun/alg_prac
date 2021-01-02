#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 16:06:01 2019

@author: hihyun
"""


"""
def count_hanoi(block):
    count=0
    if block==0:
        count=1
        return count
    elif block==1:
        count=1
        return count
    else:
        for i in range(block):
            if block-(i+1)==0:
                count+=1
            else:
                count+=count_hanoi(block-(i+1))+block-(i+2) #연결고리 이어
        return count
"""
        
def hanoi(block,from_,to_):
    
    if block ==0:
        result=str(from_)+' '+str(to_)
        print(result)
    elif block==1:
        result=str(from_)+' '+str(to_)
        print(result)
    else:
        list_num=[1,2,3]
        list_num.remove(from_)
        list_num.remove(to_)
        rest_=list_num[0]
        
    
        for i in range(block):
            if i%2==0: #짝수 스텝
                if block-(i+1)==0:
                    hanoi(0,from_,to_)
                else:
                    hanoi(block-(i+1),from_,rest_)
                    print(str(from_)+' '+str(to_))
            else:#홀수 스텝
                if block-(i+1)==0:
                    hanoi(0,rest_,to_)
                else:
                    hanoi(block-(i+1),rest_,from_)
                    print(str(rest_)+' '+str(to_))



x_int=int(input())
if x_int<=20:
    print (2**x_int-1)
    hanoi(x_int,1,3)
else:
    print (2**x_int-1)


            
        