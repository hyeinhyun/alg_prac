#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 09:09:39 2021

@author: hihyun
"""

from itertools import permutations,combinations,product

list(permutations([1,2,3],2))
list(product([1,2,3],repeat=3))


def comb_li(l,n):
    result=[]
    if n==1:
        for i in l:
            result.append([i])
    else:
        for idx,i in enumerate(l):
            sl=l[idx+1:]
            for j in comb_li(sl,n-1):
                result.append([i]+j)
    return result

comb_li([1,2,3,4],3)
list(combinations([1,2,3,4],3))



def perm_li(l,n):
    result=[]
    if n==1:
        for i in l:
            result.append([i])
    else:
        for idx,i in enumerate(l):
            sl=l[:idx]+l[idx+1:]
            for j in comb_li(sl,n-1):
                result.append([i]+j)
    return result

perm_li([1,2,3],2)
list(permutations([1,2,3],2))

def pro_li(l,n):
    result=[]
    if n==1:
        for i in l:
            result.append([i])
    else:
        for idx,i in enumerate(l):
            sl=l
            for j in comb_li(sl,n-1):
                result.append([i]+j)
    return result

pro_li([1,2,3],2)
list(product([1,2,3],repeat=2))