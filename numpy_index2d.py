# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 20:03:36 2021

@author: Ande srikanth
"""

import numpy as np
arr_2d = np.array([[1,2,3],[4,5,6],[8,9,10]])
print(arr_2d)
print(arr_2d[0,1])
arr = np.arange(0,11)
print(arr)
print(arr > 4)#boolean expressions
print(arr[arr>5])
print(arr[arr<=5])
arr_2d = np.arange(10).reshape(5,2)
print(arr_2d)