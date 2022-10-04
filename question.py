# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 15:38:45 2022

@author: Ande srikanth
"""

#write a program to print student derails like student name and rll num in function and another avearge of student marks

class student:
    def studentdetails(self,name,roll_num):
        self.name = name
        self.roll_num = roll_num
        print("Student name:\n",self.name)
        print("roll num:\n",self.roll_num)
    def average(self,m1,m2,m3,m4):
        self.m1=m1
        self.m2=m2
        self.m3=m3
        self.m4=m4
        avg =self.m1+self.m2+self.m3+self.m4
        avg = avg/4
        print("average of 4 subjects",avg)
name = input("enter your name")
roll_num = int(input("enter your roll num"))
m1 = int(input("enter subject1 marks:"))
m2 = int(input("enter subject2 marks:"))
m3 = int(input("enter subject3 marks:"))
m4 = int(input("enter subject4 marks:"))
x = student()
x.studentdetails(name, roll_num)
x.average(m1, m2, m3, m4)

#wap for calculating student avearage marks using constructors
class Student:
    def __init__(self,name ,regd_no,m1,m2,m3,m4):
        self.name = name
        self.regd_no = regd_no
        self.m1=m1
        self.m2=m2
        self.m3=m3
        self.m4=m4 
    def display(self):
        print("student name:\n",self.name)
        print("studet roll num:\n",self.regd_no)
    def average(self):
        avg =self.m1+self.m2+self.m3+self.m4
        avg = avg/4
        print("average of 4 subjects:",avg)
name = input("enter your name")
roll_num = int(input("enter your roll num"))
m1 = int(input("enter subject1 marks:"))
m2 = int(input("enter subject2 marks:"))
m3 = int(input("enter subject3 marks:"))
m4 = int(input("enter subject4 marks:"))
x = Student(name,roll_num,m1,m2,m3,m4)
x.display()
x.average()

        

#wap a person having 100 gold coins 50 silver coins 25 diamonds .on one day sister requested 10 diamonds and 10 gold coins then print coins of the person using constuctor
