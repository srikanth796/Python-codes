# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 19:47:33 2021

@author: Ande srikanth
"""

import numpy as np
array = np.arange(0,11)
print(array)
print(array[2:5])
slice_of_array =array[:10]
print(slice_of_array)
array[ : ] = 99
print(array)
#print(slice_of_array)
#2d_arrays
#import numpy as np
#arr_2d = np.array([[2,3,4][5,6,7][8,9,10]])
#print(arr_2d)