# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 09:14:36 2022

@author: Ande srikanth
"""

import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0,5,11)
y = x**2
z = x*y
fig = plt.figure()
print(fig)
fig,axes = plt.subplots(nrows =3,ncols = 2)
print(axes[0].plot(x,y))
print(axes[1].plot(x,z))
print(axes[2].plot(z,y))
print(plt.show)
#for current_axes in axes :
 #   print(current_axes.plot(x,y))
plt.tight_layout()
