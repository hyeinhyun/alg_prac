#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 14:06:50 2019

@author: hihyun
"""

class Node:
    def __init__(self,item):
        self.data=item
        self.next=None

        
        

class LinkedList:
    def __init__(self):
        self.nodeCount=0
        self.head=None
        self.tail=None
        
    def __repr__(self):
        if self.nodeCount==0:
            return "LinkedList : empty"
        s=''
        curr=self.head
        while curr !=None:
            s+=repr(curr.data)
            if curr.next !=None:
                s+="->"
            curr=curr.next
        return s
    def getAt(self,pos):
        if pos<=0 or pos>self.nodeCount:
            return None
        i=1
        curr=self.head
        while i<pos:
            curr=curr.next
            i+=1
        return curr
    
    def insertAt(self,pos,newNode):
        if pos<1 or pos>self.nodeCount+1:
            return False
        if pos==1:
            newNode.next=self.head
            self.head=newNode
        else:
            if pos==self.nodeCount+1:
                prev=self.tail
            else:
                prev=self.getAt(pos-1)
            newNode.next=prev.next
            prev.next=newNode
        if pos==self.nodeCount+1:
            self.tail=newNode
        self.nodeCount+=1
        return True
    

node1=Node(1)
node2=Node(2)
node3=Node(3)
node4=Node(4)
node5=Node(5)
node6=Node(6)



L=LinkedList()
L
L.insertAt(1,node1)
L
L.insertAt(2,node2)
L
L.insertAt(3,node3)
L
L.insertAt(4,node4)
L
L.insertAt(3,node5)
L
L.insertAt(1,node6)
L
