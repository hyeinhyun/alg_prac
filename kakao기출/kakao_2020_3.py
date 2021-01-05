#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 20:59:25 2020

@author: hihyun
"""
from collections import defaultdict
from itertools import permutations
#user_id=["frodo", "fradi", "crodo", "abc123", "frodoc"]
user_id=["frodo",'abc123']
banned_id=["fr*d*", "abc1**"]
print(solution(user_id, banned_id))
def solution(user_id, banned_id):
    p=permutations(user_id,len(banned_id))
    answer = 0
    for c in p:
        flag=False
        for idx,j in enumerate(banned_id):
            print(c[idx],j)
            ii=list(c[idx])
            jj=list(j)
            while True:
                if len(jj)==0 or len(ii)==0:
                    if len(jj)==len(ii):
                        flag=True
                        break
                    break
                x=ii.pop(0)
                y=jj.pop(0)
                print(x,y)
                if x==y or y=='*':
                    pass
                else:
                    break
        if flag:
            answer+=1
    return answer
p=permutations([1,2,3],2)
list(p)
sum([1,2,3])
