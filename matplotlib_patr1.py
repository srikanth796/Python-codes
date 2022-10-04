# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 16:01:54 2022

@author: Ande srikanth
"""

import matplotlib.pyplot as plt
#%matplotlib inline
plt.show()
import numpy as np
x = np.linspace(0,5,11)
y = x**2
z = x*y
print(x)
print(y)
print(plt.plot(x,y,'b-'))
#naming the lines x-axis and y-axis
print(plt.xlabel('X Label1'))
print(plt.ylabel('Y Label2'))
print(plt.title('Title'))
print(plt.subplot(1,2,1))
print(plt.plot(x,y,'r'))
print(plt.subplot(1,2,2))
print(plt.plot(y,x,'b'))
print(plt.subplot(1,2,2))
print(plt.plot(x,z,'y'))
fig = plt.figure()
axes = fig.add_axes([0.1,0.1,0.8,0.8])
print(axes.plot(x,y))
print(axes.set_xlabel('X label'))
print(axes.set_ylabel('Y label'))
print(axes.set_title('set Title'))
fig = plt.figure()
axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes2 = fig.add_axes([0.2,0.5,0.4,0.3])
print(axes1.plot(x,y,'p-'))
print(axes2.plot(x,y,'g'))
x = np.linspace(0,5,11)
y = x**2
z = x*y
fig = plt.figure()
print(fig)
fig,axes = plt.subplots(nrows =2,ncols = 2)
print(axes[0].plot(x,y))
#for current_axes in axes :
 #   print(current_axes.plot(x,y))
plt.tight_layout()