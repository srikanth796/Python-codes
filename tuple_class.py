# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 09:36:05 2022

@author: Ande srikanth
"""
#list = it is a collection of elements
#tuple = immutable
t = ('srikanth','apple','cat')
t3 = 1,2,3,4,5,6;#another type declaration
print(type(t))
print(t3)
print(t[1])
print(t[-1:])
#t[3]= 300 it is an imutable
#tuple concatenation is posible
#no deletion and adding elements is not possible
t2 = t+t3
print(t2)
tu = (1,2,3,(100,200,300),[1000,2000,3000])
print(tu[4][0])
#list in tuple modyfying of elemnts is possible
del tu[4][0]
print(tu[3:])
print(tu[-1:])
min = min(t3)
print(min)
#print(min(t))
print(len(tu))#length of the tuple
#cmpare=cmp(tu,t3)
#print(cmpare)

x = [10, [3.141, 20, [30, 'baz', 2.718]], 'foo']
print(x[1][2][1][2])
a = [1,2,7,8]
a[2:2]  = [3,4,5,6]
print(a)

print('abcd'.translate('a'.maketrans('abc','bcd')))

print('ab,12'.isalnum())
print('a'.maketrans('ABC','123'))
my_string = 'talentio'
for i in range(len(my_string)):
    my_string[i].upper()
print (my_string)
print('{:#}'.format(1112223334))





