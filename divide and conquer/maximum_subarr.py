#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 21:51:45 2020

@author: hihyun
"""
def max_arr(list,l,r,mid):
    left_sum=-10000
    left=0
    max_left=0
    for i in range(mid,l-1,-1):
        left=left+list[i]
        if left_sum<left:
            left_sum=left
            max_left=i
    
    right_sum=-100000
    right=0
    max_right=0
    for j in range(mid+1,r+1):
        right=right+list[j]
        if right_sum<right:
            right_sum=right
            max_right=j
    return right_sum+left_sum,max_left,max_right

def maximum_subarr(list,l,r):
    if l==r:
        return (list[l],l,r)
    else:
        mid=(l+r)//2
        left_max,left_l,left_r=maximum_subarr(list,l,mid)
        right_max,right_l,right_r=maximum_subarr(list,mid+1,r)
        middle_max,middle_l,middle_r=max_arr(list,l,r,mid)
    if middle_max>=left_max and middle_max>=right_max:
        return (middle_max,middle_l,middle_r)
    elif left_max>=middle_max and left_max>=right_max:
        return (left_max,left_l,left_r)
    else:
        return (right_max,right_l,right_r)
    


maximum_subarr([1,2,3],0,2)
