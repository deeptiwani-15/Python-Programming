# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 13:45:56 2026

@author: User
"""


class Student:
    def __init__(self, marks):
        self.marks = marks

    def grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 50:
            return "C"
        else:
            return "Fail"

marks = int(input("Enter marks: "))
s = Student(marks)
print("Grade:", s.grade())

