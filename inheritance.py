# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 19:10:58 2022

@author: Ande srikanth
"""

"""
INHERITANCE
to inherit the properties of parent class by child class
class child_class name(parent class name):
    def __init__(self):
        super().__init__()
        
        
  """  
  
  
  
class Animal:
    def __init__(self):
        self.eyes=2
        
    def breathe(self):
        print("inhale,exhale")
a=Animal()
a.breathe()

class Fish(Animal):
    def __init__(self):
        super().__init__()
    def breathe(self):
        super().__init__()
    def swim(self):
        print("it can move in water")        

nemo= Fish()
nemo.breathe()
nemo.swim()