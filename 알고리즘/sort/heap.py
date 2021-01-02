#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 16:40:54 2020

@author: hihyun
"""




def heapify(arr,i,heap_size):
    n=len(arr)
    left=i*2+1
    right=i*2+2
    largest=i
    if left<n and arr[largest]>=arr[left]: #cur>left
        largest=i
    elif left<n and arr[largest]<arr[left]:
        largest=left
    if right<n and arr[largest]<arr[right]:
        largest=right
    
    if largest !=i:
        arr[largest],arr[i]=arr[i],arr[largest] #exchage
        heapify(arr,largest,heap_size)
    return arr

class heap:
    def __init__(self,arr,heap_size):
        self.heap=arr
        self.heap_size=heap_size


    def build_heap(self):
        for i in range(self.heap_size//2-1,-1,-1):
            self.heap=heapify(self.heap,i,self.heap_size)
    def insert(self,key):
        self.heap_size+=1
        self.heap.append(key)
        print(self.heap_size)
        self.build_heap()
            
        
h1=heap([5,7,1,2,3],5)
h1.build_heap()
h1.insert(10)












