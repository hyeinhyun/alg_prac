#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 13:29:55 2019

@author: hihyun
"""
#__ --> 특별한 메소드

class Human():
    def __init__(self,name,weight):
        """초기화"""
        print("__init start")
        self.name=name
        self.weight=weight
        print("name is {}, weight is {}".format(name,weight))
        
    def ___str__(self):
        """문자열"""
        return "{}'s weight {}kg".format(self.name,self.weight)

    def eat(self):
        self.weight+=0.1
        print("{}가 먹어서 {}kg이 되었다".format(self.name,self.weight))
    def walk(self):
        self.weight-=0.1
        print("{}가 먹어서 {}kg이 되었다".format(self.name,self.weight))
    def speak(self,message):
        print(message)

person=Human('hyein',50)
person.eat()
print(person)
##자동으로 return 도 해주는구만

class Animal():
    def __init__(self,name):
        self.name=name
    def walk(self):
        print("walk")
    def eat(self):
        x=count()
        print(x)
        print("eat")
    def greet(self):
        print("{} is 인사한다".format(self.name))

def count():
    return 1

class Human(Animal):
    def __init__(self,name,hand):
        super().__init__(name)
        self.hand=hand
    def greet(self):
        super().greet()
        print("wave+ing using {}".format(self.hand))

class Dog(Animal):

    def greet(self):
        print("wag")
        
person=Human("사람",'right')
person.greet()

