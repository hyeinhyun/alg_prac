#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 23:10:50 2020

@author: hihyun
"""

class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def size(self):
        
        l=self.left.size() if self.left else 0

        r=self.right.size() if self.right else 0

        return l+r+1
    def depth(self):
        l=self.left.depth() if self.left else 0
        r=self.right.depth() if self.right else 0
        return max(l,r)+1
    def inorder(self):
        traversal=[]
        if self.left:
            traversal+=self.left.inorder()
        traversal.append(self.data)
        if self.right:
            traversal+=self.right.inorder()
        return traversal
        
        

class tree:
    def __init__(self,n):
        self.root=n
    def size(self):
        result=self.root.size() if self.root else 0
        return result

    def depth(self):
        result= self.root.depth() if self.root else 0
        return result
    
    def inorder(self):
        if self.root:
            return self.root.inorder()
    def BFS(self):
        if self.root:
            queue=[self.root]
            visit=[self.root]
            while len(queue)!=0:
                cur=queue.pop(0)
                if cur.left:
                    queue.append(cur.left)
                    visit.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                    visit.append(cur.right)
        return visit
                    
        
        
n1=node(0)
t=tree(n)
t.depth()
