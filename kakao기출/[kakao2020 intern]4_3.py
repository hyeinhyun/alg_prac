#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 23:03:43 2021

@author: hihyun
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 14:22:07 2021

@author: hihyun
"""
from collections import defaultdict
class Node:
    def __init__(self,key,length={},string=None):
        self.key=key
        self.length=defaultdict(list)#길이..#terminate정보
        self.children={}
class Trie:
    def __init__(self):
        self.head=Node(None)
    def insert(self,r_string,length,reverse=True):
        cur_node=self.head
        if reverse:
            string=r_string[::-1].replace('?','')
        else:
            string=r_string.replace('?','')
        for i in string:
            if i not in cur_node.children:
                cur_node.children[i]=Node(i)
            cur_node=cur_node.children[i]
        cur_node.length[length].append(r_string)
        #cur_node.string=r_string
    def search(self,string):
        l=len(string)
        cur_node=self.head
        result=[]
        result+=cur_node.length[l]#????에 대한
        for i in string:
            if i not in cur_node.children:
                return result
            else:
                #여기서 더해야하는데..
                if l in cur_node.children[i].length:
                    result+=(cur_node.children[i].length[l])
            cur_node=cur_node.children[i]

        return result

def solution(user_id, banned_id):
    post=Trie()
    pre=Trie()
    result={}
    
    for i in banned_id:
        if i[0]=='?':#post
            post.insert(i,len(i))
        else:
            pre.insert(i,len(i),reverse=False)
        result[i]=0

    for i in user_id:
        for j in post.search(i[::-1]):
            result[j]+=1
        for j in pre.search(i):
            result[j]+=1
    print(result)


    return list(result.values())
        
        
q=["fro??", "????o", "fr???", "fro???", "pro??",'?????','????do','f????']
u=["frodo", "front", "frost", "frozen", "frame", "kakao"]
print(solution(u,q))
pre=Trie()
pre.insert('fro',5)
pre.insert('fr',5)
pre.insert('',5)
pre.search('frodo')
