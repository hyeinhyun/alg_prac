#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 19:56:37 2020

@author: hihyun
"""
import sys


def solution(info):
    alarm=[]
    i_type=[]
    save=[]
    for i in info:
        if i != "check notification":
            alarm.append(i.split()[0])
            i_type.append(i.split()[1])
            
        else:#check notification
            temp=[]
            cur=i_type.pop()
            temp.append(alarm.pop())
            try:
                while i_type[-1]==cur:
                    i_type.pop()
                    temp.append(alarm.pop())
                if cur=="share":
                    cured="shared"
                if cur=="comment":
                    cured="commented"
                if len(temp)==1:
                    save.append("{} {} your post".format(temp[0],cured))
                elif len(temp)==2:
                    save.append("{} and {} {} your post".format(temp[1],temp[0],cured))
                else:
                    save.append("{} and {} others {} your post".format(temp[-1],len(temp)-1,cured))
            except:
                if cur=="share":
                    cured="shared"
                if cur=="comment":
                    cured="commented"
                if len(temp)==1:
                    save.append("{} {} your post".format(temp[0],cured))
                
    return save

                
            

a=input()[1:-1].split(',')
new=[i.strip()[1:-1] for i in a]
print(solution(new))
