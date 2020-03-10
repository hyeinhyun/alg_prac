#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 18:34:28 2019

@author: hihyun
"""

    def popAfter(self, prev):
        if prev == self.tail:
            return None ##anything to remove!
        elif self.nodeCount==0:
            return None
        else:
            curr=prev.next
            prev.next=curr.next
            if curr==self.tail:
                prev=self.tail
                
            self.nodeCount-=1
            return curr.data


    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError #pos<1 : cannot remove! 
        elif self.nodeCount==1:
            prev=self.head
        else:
            prev=self.getAt(pos-1)
        return self.popAfter(prev)
            