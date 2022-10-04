# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 09:45:51 2022

@author: Ande srikanth
"""

#constructor:constructor initialize the values of class function,no need to call ,it can be executed automatically 
#def __init__(self,args...):
    #statements

class arith:
    def __init__(self):
        self.a = 10
        self.b = 20
    def add(self):
        c = self.a+self.b
        print(c)
obj = arith()
obj.add()

#area and perimeter of rectangle
class arith:
    def __init__(self,l,b):
        self.l =l
        self.b=b
    def area(self):
        area = self.l*self.b
        print("area of rectangle",area)
    def perimeter(self):
        peri = 2*self.l*self.b
        print("perimeter",peri)
obj = arith(20,40)
obj.area()
obj.perimeter()