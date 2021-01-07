#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 15:37:37 2021

@author: hihyun
"""
#prefix먼저
from collections import defaultdict
class Node:
    def __init__(self,length={}):
        self.length=defaultdict(int)
        self.children={}
class Trie:
    def __init__(self):
        self.head=Node()
    def insert(self,string,length):
        cur_node=self.head
        cur_node.length[length]+=1 #for ?????
        for i in string:
            if i not in cur_node.children:
                cur_node.children[i]=Node()
            cur_node.children[i].length[length]+=1
            cur_node=cur_node.children[i]
        
    def search(self,string,length):
        cur_node=self.head
        for i in string:
            if i not in cur_node.children:
                return 0
            cur_node=cur_node.children[i]
        
        return cur_node.length[length]
def solution(user_id, banned_id):
    post=Trie()
    pre=Trie()
    
    for i in user_id:
        post.insert(i[::-1],len(i))
        pre.insert(i,len(i))

    answer=[]
    for i in banned_id:
        if i[0]=='?':
            answer.append(post.search(i[::-1].replace('?',''),len(i)))
        else:
            answer.append(pre.search(i.replace('?',''),len(i)))

    return answer
        
        
q=["fro??", "????o", "fr???", "fro???", "pro??",'?????','????do','f????']
u=["frodo", "front", "frost", "frozen", "frame", "kakao"]
print(solution(u,q))