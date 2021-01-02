#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 20:39:29 2020

@author: hihyun
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 19:16:55 2020

@author: hihyun
"""

def oreum(num_list):
    x=len(num_list)
    num_o=[1]*x
    
    for i in range(x):

        for j in range(0,i):#전 기준점
            if num_list[j]<num_list[i]:
                if num_o[i]<num_o[j]+1:
                    num_o[i]=num_o[j]+1
                else:
                    pass
    return max(num_o)
num=int(input())
num_list=list(map(int,input().split()))
max_val=oreum(num_list)
print(max_val)