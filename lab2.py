# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 13:20:17 2022

@author: Ande srikanth
"""

#value present in sequence
flag = 0
list = [1,2,3,4,5,6,7,8,9,10]
for i in range(len(list)):
    if list[i] == 6:
        print("true")
    else:
        print("false")
        
dict ={"a":"apple","b":"ball"}
print(dict)
if "a" in dict:
    print("true")
else:
    print("false")    