# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 19:18:52 2022

@author: Ande srikanth
"""

from tkinter import *
top = Tk()
top.geometry("200x100")

def fun():
    messagebox.showinfo("Hello", "Red Button clicked")

b1 = Button(top,text = "red",command = fun,activeforeground = "red",activebackground = "red",pady=10)
b2 = Button(top,text = "Blue",activeforeground = "Blue",activebackground = "Blue",pady=10)
b3 = Button(top,text = "Yellow",activeforeground = "Yellow",activebackground = "Yellow",pady=10)
b4 = Button(top,text = "Green",activeforeground = "Green",activebackground = "Green",pady=10)
b1.pack(side = RIGHT)
b2.pack(side = LEFT)
b3.pack(side = TOP)
b4.pack(side = BOTTOM)
top.mainloop()
