#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 16:14:02 2021

@author: hihyun
"""

import math
def solution(numbers, hand):
    answer = ''
    cur_l=10
    cur_r=12
    for i in numbers:
        if i==0:
            i=11
        if i==1 or i==4 or i==7:
            cur_l=i
            answer+='L'
        elif i==3 or i==6 or i==9:
            cur_r=i
            answer+='R'
        else:
            temp_r=abs((i-1)//3-(cur_r-1)//3)+abs((i-1)%3-(cur_r-1)%3)
            temp_l=abs((i-1)//3-(cur_l-1)//3)+abs((i-1)%3-(cur_l-1)%3)
            if temp_r<temp_l:
                cur_r=i
                answer+='R'
            elif temp_r>temp_l:
                print(answer)
                cur_l=i
                answer+='L'
            else:
                if hand=='right':
                    cur_r=i
                    answer+='R'
                else:
                    cur_l=i
                    answer+='L'                
    return answer