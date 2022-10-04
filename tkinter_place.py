# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 13:05:07 2022

@author: Ande srikanth
"""

from tkinter import *
parent = Tk()
parent.geometry("400x250")
name = Label(parent,text = "User name").place(x = 30,y = 50)
e1 = Entry(parent).place(x=60,y = 50)
passwd = Label(parent,text = "password").place(x = 30,y = 90)
e2 = Entry(parent).place(x = 60,y = 90)
buton = Button(parent,text="submit").place(x = 30,y = 130)
parent.mainloop()