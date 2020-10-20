#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 17:54:32 2020

@author: hihyun
"""
import sys
sys.setrecursionlimit(1000001)

def solution(st,ed):
    sec=[-1]*100001
    q=[st]
    pi=['']*100001
    sec[st]=0
    answer=0
    while len(q)!=0:
        cur=q.pop(0)

        if cur*2<len(sec):
            if sec[cur*2]==-1:#unvisit
                q.append(cur*2)
                sec[cur*2]=sec[cur]+1
                pi[cur*2]=cur
                if cur*2==ed:
                    answer=sec[cur*2]
                    break
        if cur-1>=0:
            if sec[cur-1]==-1:#unvisit  
                q.append(cur-1)
                sec[cur-1]=sec[cur]+1
                pi[cur-1]=cur
                if cur-1==ed:
                    answer=sec[cur-1]
                    break
        if cur+1<len(sec):
            if sec[cur+1]==-1:#unvisit
                q.append(cur+1)
                sec[cur+1]=sec[cur]+1
                pi[cur+1]=cur
                if cur+1==ed:
                    answer=sec[cur+1]
                    break


    return answer,pi
    
def path_read(pi,st,ed,answer):
    if st==ed:
        #거꾸로 만들어
        answer=answer[::-1]
        path=''
        for i in answer:
            path+=str(i)+' '
        print(path)
            
        
    else:
        answer.append(pi[ed])
        path_read(pi,st,pi[ed],answer)
        
        

st,ed=map(int,input().split())
answer,pi=solution(st,ed)
print(answer)
answer2=path_read(pi,st,ed,[ed])
