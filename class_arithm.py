# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 15:24:05 2022

@author: Ande srikanth
"""

#arithmetic operations where four functions you have to declare

class arithmetic:
    def add(self,a,b):
        self.a = a
        self.b = b
        c = self.a + self.b
        print(c)
    def sub(self,a,b):
        self.a = a
        self.b = b
        c = self.a - self.b
        print(c)
    def div(self,a,b):
        self.a = a
        self.b = b
        c = self.a / self.b
        print(c)
    def prod(self,a,b):
        self.a = a
        self.b = b
        c = self.a * self.b
        print(c)
        
        
a = int(input("enter a value:"))
b = int(input("enter b value:"))
x = arithmetic()
x.add(a,b)
x.sub(a,b)
x.div(a,b)
x.prod(a,b)

class arithmetic:
    def data(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        c = self.a - self.b
        print(c)
x = arithmetic()
x.data(10,20)
x.add()
        