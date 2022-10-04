# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 07:23:59 2022

@author: Ande srikanth
"""

class car: #class named car
    def __init__(self,modelname,year):#2 attributes
        self.modelname=modelname
        self.year=year
    def display(self):
        print(self.modelname,self.year)
        
c1=car("BMW",2003)#c1 as object
c1.display()