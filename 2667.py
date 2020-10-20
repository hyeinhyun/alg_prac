#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 21:14:50 2020

@author: hihyun
"""
def s_to_tuple(s):
    return list(map(int,s[1:-1].split(',')))
def adj(G,N,point):
    adj_li=[]
    i,j=point
    if i-1>=0:#up
        if str((i-1,j)) in list(N.keys()):
            adj_li.append((i-1,j))
            
    if i+1<len(G):#down
        if str((i+1,j)) in list(N.keys()):
            adj_li.append((i+1,j))
            
    if j-1>=0:#left
        if str((i,j-1)) in list(N.keys()):
            adj_li.append((i,j-1))
            
    if j+1<len(G):
        if str((i,j+1)) in list(N.keys()):
            adj_li.append((i,j+1))
            
    return adj_li


def DFS(G,N,st):
    N[str(st)]=1#반복이긴 하네
    st_t=s_to_tuple(st)
    adj_li=adj(G,N,st_t)
    for x in adj_li:
        if N[str(x)]==0:#아직 방문하지 않았다면,
            N[str(x)]=1#방문으로 바꿔
            DFS(G,N,str(x))

num=int(input())
G=[]
N={}
for i in range(num):
    temp=list(map(int,list(input())))
    for idx,x in enumerate(temp):
        if x==1:
            N[str((i,idx))]=0
    G.append(temp)


#기존
total=0
prev=0
total_li=[]

#DFS(G,N,'(0,1)')

for i in N.keys():
    if N[str(i)]==0:#즉 아직 방문을 안했으면,
        DFS(G,N,i)
        total=sum(N.values())
        total_li.append(total-prev)
        prev=sum(N.values())
print(len(total_li))
for i in sorted(total_li):
    print(i)        
        
    


    