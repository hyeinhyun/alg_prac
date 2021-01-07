#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 16:55:48 2021

@author: hihyun
"""

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
        self.length=defaultdict(list)
        self.children={}
class Trie:
    def __init__(self):
        self.head=Node()
    def insert(self,r_string):
        cur_node=self.head
        r_
        cur_node.length[length].append() #for ?????
        for i in string:
            if i not in cur_node.children:
                cur_node.children[i]=Node()
            cur_node.children[i].length[length]+=1
            cur_node=cur_node.children[i]
        
    def search(self,string,length):
        l=length
        cur_node=self.head
        count=0
        for i in string:
            if i not in cur_node.children:
                return 0
            cur_node=cur_node.children[i]
        if l in cur_node.length:
            count=cur_node.length[length]
        return count
def solution(user_id, banned_id):
    post=Trie()
    pre=Trie()
    
    for i in banned_id:
        post.insert(i[::-1])
        pre.insert(i)

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