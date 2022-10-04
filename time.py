# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 15:12:54 2022

@author: Ande srikanth
"""


time = float(input("enter time:\n"))
flag = 0
if (time == 9 and time >= 10) or (time<10 and time >= 11) or (time == 11 and time <4) or (time>=5 and time <5.3):
    flag = 1
else:
    flag = 0
    
if flag ==1:
    print("is happy")
else:
    print("not happy")
    """
    print("i woke up")
elif time >= 10 and time<11:
    print("break fast")       
    """
   

#learning is not meaning of copying its a remember what we studied