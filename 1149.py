#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 13:39:30 2020

@author: hihyun
"""

import sys
sys.setrecursionlimit(1000000)
def solution(price,total_price,color):
    for i in price:
        count=len(total_price)#가지
        for c in range(count):
            cur_price=total_price.pop(0)
            cur_color=color.pop(0)
            if cur_color=='R':
                if cur_price+i[1]>cur_price+i[2]:
                    color.append('G')
                    total_price.append(cur_price+i[1])
                    
                elif cur_price+i[1]<cur_price+i[2]:
                    color.append('B')
                    total_price.append(cur_price+i[2])
                else:
                    color.append('B')
                    color.append('G')
                    total_price.append(cur_price+i[2])
                    total_price.append(cur_price+i[1])
                
            elif cur_color=='G':
                if cur_price+i[0]>cur_price+i[2]:
                    color.append('R')
                    total_price.append(cur_price+i[0])
                    
                elif cur_price+i[1]<cur_price+i[2]:
                    color.append('B')
                    total_price.append(cur_price+i[2])
                else:
                    color.append('B')
                    color.append('R')
                    total_price.append(cur_price+i[2])
                    total_price.append(cur_price+i[0])
                
            else:#else
                if cur_price+i[1]>cur_price+i[0]:
                    color.append('G')
                    total_price.append(cur_price+i[1])
                    
                elif cur_price+i[1]<cur_price+i[0]:
                    color.append('R')
                    total_price.append(cur_price+i[0])
                else:
                    color.append('R')
                    color.append('G')
                    total_price.append(cur_price+i[0])
                    total_price.append(cur_price+i[1])

    return min(total_price)
                
            
        
        
    

h_num=int(sys.stdin.readline())
price=[]
for i in range(h_num):
    price.append(list(map(int,sys.stdin.readline().strip().split(' '))))
price=price[::-1]
print(solution(price[1:],price[0],['R','G','B']))
    