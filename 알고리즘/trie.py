#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 14:03:11 2021

@author: hihyun
"""

class Node:
    def __init__(self,key,data=None):
        self.key=key
        self.data=data
        self.children={}

class Trie:
    def __init__(self):
        self.head=Node(None)#root
    def insert(self,string):
        cur_node=self.head#항상 root부터 시작
        for i in string:
            if i not in cur_node.children:
                cur_node.children[i]=Node(i)
            cur_node=cur_node.children[i]
        cur_node.data=string
    def search(self,string):
        cur_node=self.head#서치도 항상  root
        for i in string:
            if i not in cur_node.children:
                return False
            cur_node=cur_node.children[i]
        if cur_node.data!=None:
                return True
        return False            
    def starts_with(self,prefix):
        cur_node=self.head
        result=[]
        for i in prefix:
            if i in cur_node.children:
                cur_node=cur_node.children[i]
            else:
                return None
        candidate=list(cur_node.children.values())
        while candidate:
            cur=candidate.pop()
            if cur.data != None:
                result.append(cur.data)
            candidate+=list(cur.children.values())
        return result
            

x=Trie()
x.insert('')
x.insert('hyein')
x.insert('hyewon')
x.insert('yonghee')
x.insert('kyeongjoon')
x.search('hyein')
x.search('hyeiw')
x.starts_with('hye')
x.search('')
