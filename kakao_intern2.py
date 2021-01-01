#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 18:18:05 2020

@author: hihyun
"""

from collections import defaultdict
from itertools import permutations
def minus(x,y):
    return x-y
def mulp(x,y):
    return x*y
def plus(x,y):
    return x+y
def par(x,d):
    if x==d[x]:
        return x
    else:
        return par(d[x],d)
def solution(expression):
    expression+=' '
    rd=defaultdict(int)
    rd_val=defaultdict(int)
    answer = 0
    temp=''
    exp=[]
    #num=[]
    count=0
    for i in expression:
        if i=='-' or i=='*' or i=='+':
            exp.append(i)
            rd[count]=count
            rd_val[count]=int(temp)
            count+=1
            #num.append(int(temp))
            temp=''
        elif i==' ':
            rd[count]=count
            rd_val[count]=int(temp)
            count+=1
        else:
            temp+=i
    s=set(exp)
    print(s)
    # print(list(permutations(s,len(s))))
    for k in list(permutations(s,len(s))):
        print(k)
        d=rd.copy()
        d_val=rd_val.copy()
        for kk in k:
            for idx,x in enumerate(exp):
                if x==kk:
                
                    if x=='-':
                        r_num1=par(d[idx],d)
                        r_num2=par(d[idx+1],d)
                        result=minus(d_val[r_num1],d_val[r_num2])
                        ll=len(d.keys())
                        d_val[ll]=result
                        d[ll]=ll
                        d[r_num1]=ll
                        d[r_num2]=ll

                    elif x=='*':
                        r_num1=par(d[idx],d)
                        r_num2=par(d[idx+1],d)
                        result=mulp(d_val[r_num1],d_val[r_num2])
                        ll=len(d.keys())
                        d_val[ll]=result
                        d[ll]=ll
                        d[r_num1]=ll
                        d[r_num2]=ll
                    else:#plus
                        r_num1=par(d[idx],d)
                        r_num2=par(d[idx+1],d)
                        result=plus(d_val[r_num1],d_val[r_num2])
                        ll=len(d.keys())
                        d_val[ll]=result
                        d[ll]=ll
                        d[r_num1]=ll
                        d[r_num2]=ll
        if answer<abs(d_val[len(d.keys())-1]):
            answer=abs(d_val[len(d.keys())-1])
    
    return answer
print(solution("100-100*100-100+100"))
