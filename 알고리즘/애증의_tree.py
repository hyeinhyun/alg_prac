#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 21:04:13 2020

@author: hihyun
"""

class Node():
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

class BinarySearchTree():
    def __init__(self):
        self.root=None
    def insert(self,node):
        if self.root is None: #만약에 루트가 없다면
            self.root=node
        else: #루트가 있다면
            prev=self.root
            self.insert_value(prev,node)
    def insert_value(self,prev,node):
        if prev.data>=node.data:
            if prev.left is None:
                prev.left=node
            else:
                prev=prev.left
                self.insert_value(prev,node)
        else:
            if prev.right is None:
                prev.right=node
            else:
                prev=prev.right
                self.insert_value(prev,node)
                
    def find(self,data):
        if self.root is None:
            return False
        else:
            prev=self.root
            print(self.find_value(prev,data))
            return self.find_value(prev,data)

    def find_value(self,prev,data):
        if prev.data>data:
            if prev.left is None:
                return False
            else:
                prev=prev.left
                self.find_value(prev,data)
        elif prev.data==data:
            x='True'
            return x
        else:
            if prev.right is None:
                return False
            else:
                prev=prev.right
                self.find_value(prev,data)
            
            
            
            
if __name__ == '__main__':
    n1=Node(3)
    n2=Node(2)
    n3=Node(4)
    n4=Node(5)
    bt=BinarySearchTree()
    bt.insert(n1)
    bt.insert(n2)
    bt.insert(n3)
    bt.insert(n4)
    bt.find(5)
