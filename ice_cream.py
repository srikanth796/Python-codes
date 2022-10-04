# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 10:41:56 2022

@author: Ande srikanth
"""

#ice_cream stand
class Restaurant:
    def __init__(self,name,cuisine_type):
        self.name = name.title()
        self.cuisine_type=cuisine_type
        self.served=0
    
    def describe_restaurant(self):
        msg = self.name + " serves wonderful " + self.cuisine_type + "."
        print("\n",msg)
        
    def open_restaurant(self):
        msg = self.name + " is open please come in"
        print("\n",msg)
        
    def set_number_served(self):
        self.served=served
    
    def increment_served(self):
        self.served=+additional_served
        
#inheriting the base class from parent class
class Icecream(Restaurant):
    def __init__(self, name, cuisine_type):
        super().__init__(name, cuisine_type)
        self.set_flavours = []
    def show_flavours(self):
        msg = "we have the following flavours:"
        print(msg)
        for flavor in self.set_flavours:
            print("-",flavor.title())
        
big_one = Icecream("the big one", "Ice cream")
big_one.set_flavours = ["Vanila","choclate","butter scotch"]
big_one.describe_restaurant()
big_one.show_flavours()

