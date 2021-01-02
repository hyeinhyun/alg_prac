#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 15:40:08 2020

@author: hihyun
"""
####트라이
class Node:
    def __init__(self,value):
        self.value=value
        self.child_list=[]

    def append_child(self,child):
        self.child_list.append(child)


class Tree:
    def __init__(self,value :Node):
        self.root=value
    def traverse(self,sp):
        
        
        


root_list={}
num=int(input())
for i in range(num):
    phone_num=str(input())
    if phone_num[0] not in root_list.keys():
        r_node=Node(phone_num[0])
        tree=Tree(node)
        root_list[phone_num[0]]=tree
    r_node=root_list(phone_num[0]).root

    for idx,p in enumerate(phone_num[1:-1]):
        node=Node(p)
        if node.value in r_node.child_list
        r_node.append(node)
        r_node=node
