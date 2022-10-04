# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 12:46:57 2022

@author: Ande srikanth
"""

from tkinter import *
parent = Tk()
name = Label(parent,text = "User name").grid(row = 0,column = 0)
e1 = Entry(parent).grid(row = 0,column=1)
passwd = Label(parent,text = "password").grid(row = 1,column = 0)
e2 = Entry(parent).grid(row = 1,column = 1)
buton = Button(parent,text="submit").grid(row = 3,column = 0)
parent.mainloop()