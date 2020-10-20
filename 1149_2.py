#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 16:35:23 2020

@author: hihyun
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 13:39:30 2020

@author: hihyun
"""

import sys
sys.setrecursionlimit(1000000)
def solution(price,total_price):
    for i in price:
        R=i[0]
        G=i[1]
        B=i[2]
        temp_R=min(total_price[1],total_price[2])+R #R
        temp_G=min(total_price[0],total_price[2])+G #R
        temp_B=min(total_price[1],total_price[0])+B #R
        total_price[0]=temp_R
        total_price[1]=temp_G
        total_price[2]=temp_B




    return min(total_price)
                
            
        
        
    

h_num=int(sys.stdin.readline())
price=[]
for i in range(h_num):
    price.append(list(map(int,sys.stdin.readline().strip().split(' '))))
price=[[26,40,83],[49,60,57],[13,89,99]]
print(solution(price[1:],price[0]))
    