# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 19:27:09 2022

@author: Ande srikanth
"""

#addittion of two numbers and multiplication using inheritance

class Arithmetic:#base class
    def __init__(self):
        self.a=2
        self.b=4
    def add(self):
        print("self.a+self.b",self.a+self.b)
        
a=Arithmetic()
a.add()
class product(Arithmetic):
    def __init__(self):
        super().__init__()
    def mult(self):
        print("a*b",self.a*self.b)
    def add(self):
        super().__init__()
        
p=product()
p.mult()
p.add()