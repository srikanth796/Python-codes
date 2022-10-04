# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 20:50:07 2022

@author: Ande srikanth
"""
"""
marks = int(input("enter your marks:\n"))
if marks>=90:
    print("O grade")
elif marks>=80 and marks<90:
    print("A grade")
elif marks>=70 and marks<80:
    print("B grade")
elif marks>=60 and marks<70:
    print("C grade")
elif marks>=50 and marks<70:
    print("D grade")
elif marks>=40 and marks<50:
    print("E grade")
else:
    print("your fail")
    """


def grade(marks):
    if marks>=90:
        print("O grade")
    elif marks>=80 and marks<90:
        print("A grade")
    elif marks>=70 and marks<80:
        print("B grade")
    elif marks>=60 and marks<70:
        print("C grade")
    elif marks>=50 and marks<70:
        print("D grade")
    elif marks>=40 and marks<50:
        print("E grade")
    else:
        print("your fail")
        
marks = int(input("enter your marks:\n"))
grade(marks)
    