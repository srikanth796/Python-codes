# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 09:35:04 2022

@author: Ande srikanth
"""

#write a program for finding area and perimeter of square
class square:
    def data(self,a):
        self.a = a
        """
    def rdata(self,l,b):
        self.l=l
        self.b=b
        """
    def area(self):
        c = a *a
        print("area of square",c)
    def perimeter(self):
        c = 4*a
        print("perimetr of square",c)
a = int(input("enter a side of square:"))
#l = int(input("length of rectangle"))
obj = square()
obj.data(a)
obj.area()
obj.perimeter()

        