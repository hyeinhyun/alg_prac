#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 14:22:07 2021

@author: hihyun
"""

class Node:
    def __init__(self,key,length=None):
        self.key=key
        self.length=length
        self.children={}
class Trie:
    def __init__(self):
        self.head=Node(None)
    def insert(self,string,length):
        cur_node=self.head
        for i in string:
            if i not in cur_node.children:
                cur_node.children[i]=Node(i)
            cur_node=cur_node.children[i]
        cur_node.length=length
    def search(self,string):
        l=len(string)
        cur_node=self.head
        count=0
        for i in string:
            if i not in cur_node.children:
                break
            else:
                #여기서 더해야하는데..
                if cur_node.children[i].length==l:
                    count+=1
            cur_node=cur_node.children[i]
        print(count)
        return count

def solution(user_id, banned_id):
    post=Trie()
    pre=Trie()
    
    for i in banned_id:
        if i[0]=='?':#post
            post.insert(i.replace('?',''),len(i))
        else:
            pre.insert(i.replace('?',''),len(i))

    answer=[]
    for i in user_id:
        print(i)
        count=0
        count+=post.search(i[::-1])
        count+=pre.search(i)
        answer.append(count)


    return answer
        
        
q=["fro??", "????o", "fr???", "fro???", "pro?"]
u=["frodo", "front", "frost", "frozen", "frame", "kakao"]
print(solution(u,q))
pre=Trie()
pre.insert('fro',5)
pre.insert('fr',5)
pre.insert('fr',5)

pre.search('frodo')
