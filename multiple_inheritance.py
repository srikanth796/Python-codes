# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 11:21:37 2022

@author: Ande srikanth
"""

#multiple inheriatance 
#it can be derived from two base classes 
class Student:
    def __init__(self,name ,regd_no):
        self.name = name
        self.regd_no = regd_no
     def display(self):
        print("student name:\n",self.name)
        print("studet roll num:\n",self.regd_no)
    
class faculty:
    def __init__(self,name ,regd_no):
        self.name = name
        self.regd_no = regd_no
    def display(self):
        print("student name:\n",self.name)
        print("studet roll num:\n",self.regd_no)

class derived(Student,faculty):
    def __init__(self, name, cuisine_type):
        super().__init__(name, cuisine_type)
        self.set_flavours = []
    def show_flavours(self):
        msg = "we have the following flavours:"
        print(msg)
        for flavor in self.set_flavours:
            print("-",flavor.title())
    
            
                    
ice_cream = derived("Srikanth",3697)
ice_cream.display()
set_flavours = ["Vanila","choclate","butter scotch"]
ice_cream.show_flavours()