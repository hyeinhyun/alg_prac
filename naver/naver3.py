#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 22:15:31 2020

@author: hihyun
"""


def solution(list):
    fever_time=0
    score=len(list)
    for idx,i in enumerate(list):
        time=i[0]
        item=i[1]
        if item !=1: #아이템이 아닐때
            if time<=fever_time:
                score+=50

        
        else:
            if time>fever_time: #fever time 안에 안들어갔을때
                if time+10<=list[idx+1][0]:#10초 안에 다음 아이템이 안나올때
                    fever_time=time+9.5+30
                else:
                    fever_time=list[idx+1][0]-0.5+30
                
                score+=10*(idx+1)
            
            else:#피버타임안에 들어갔을때
                temp=-1
                flag=0
                for num in range(1,len(list)-idx):
                    if list[idx+num][0]<(time+10) and list[idx+num][0]<fever_time:
                        if list[idx+num][1] ==1: #또다른 item 발견
                            temp=idx+num
                            flag=1
                            break
                    elif list[idx+num][0]>(time+10) or list[idx+num][0]>fever_time:
                        temp=idx+num-1
                        break
                
                if temp !=-1:  
                    fever_time=list[temp][0]-0.5+30
                    if flag==0:
                        score+=10*(temp+1)+50
                    else:
                        score+=10*(temp)+50

                else:
                    fever_time=time+9.5+30+50
                    score+=10*(len(score))
    return score

print(solution([[5,0],[7,1],[12,0],[16,0],[20,1],[29,1],[35,0],[38,0],[60,0],[72,0]]))


                
                    