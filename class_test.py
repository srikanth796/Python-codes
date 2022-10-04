# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 15:00:43 2022

@author: Ande srikanth
"""

class test:
    a=10
    b=20
    def show(self):
        print(self.a)
        print(self.b)
x = test()
print(x.a)
print(x.b)
x.show()

class test:
    a=10
    b=20
    def show(self,a,b):
        self.a = a
        self.b = b
        print(self.a)
        print(self.b)
x = test()
print(x.a)
print(x.b)
x.show(100,200)