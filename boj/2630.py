#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 23 23:45:57 2020

@author: hihyun
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 18 17:33:03 2020

@author: hihyun
"""

    

def sum_mat(arr):
    result=0
    for i in arr:
        result+=sum(i)
    return result
def block_div(arr,N):
    b1=[]
    b2=[]
    b3=[]
    b4=[]
    for idx,i in enumerate(arr):
        if idx<N:
            b1.append(i[:N])
            b2.append(i[N:])
        else:
            b3.append(i[:N])
            b4.append(i[N:])
    return b1,b2,b3,b4

def solution(arr, N):
    if N==1:
        if sum_mat(arr)==0:
            return [1,0]
        else:#1
            return [0,1]
    if sum_mat(arr)==0:
        return [1,0]
    elif sum_mat(arr)==N*N:
        return [0,1]
    n=N//2
    b1,b2,b3,b4=block_div(arr,n)
    r1=solution(b1,n)
    r2=solution(b2,n)
    r3=solution(b3,n)
    r4=solution(b4,n)
    
    #conquer
    
    x=r1[0]+r2[0]+r3[0]+r4[0]
    y=r1[1]+r2[1]+r3[1]+r4[1]
    return [x,y]    
    
    



num=int(input())
li=[]
for i in range(num):
    x=input()
    temp=x.split(' ')
    temp=[int(i) for i in temp]
    li.append(temp)
result=solution(li,num)
print(result[0])
print(result[1])

