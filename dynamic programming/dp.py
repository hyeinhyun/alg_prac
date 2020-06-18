#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 18:56:42 2020

@author: hihyun
"""
#재귀
def rod1(length,prices):
    if length==0:
        return 0
    else:
        max=0
        for i in range(1,length+1):
            val=prices[i]+rod1(length-i,prices)
            if max<val:
                max=val
    return max

rod1(4,[0,1,5,8,9])


def b_to_u_rod(length,prices):
    r=[0]
    for i in range(1,length+1):
        q=0
        for j in range(1,i+1):
            q=max(q,prices[j]+r[i-j])
        r.append(q)
    return r[length]

b_to_u_rod(4,[0,1,5,8,9])


def t_to_d_rod(length,prices,r):
    if r[length]>=0:#값을 가지고 있다면
        return r[length]
    elif length==0:
        q=0
    else:#no value
        q=-10000
        for i in range(1,length+1):
            q=max(q,prices[i]+t_to_d_rod(length-i,prices,r))
    
    r[length]=q
    print(r)
    return q

t_to_d_rod(4,[0,1,5,8,9],[])
