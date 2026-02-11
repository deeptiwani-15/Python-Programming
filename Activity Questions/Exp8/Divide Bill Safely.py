# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 13:48:09 2026

@author: User
"""


try:
    total = float(input("Enter total bill: "))
    people = int(input("Enter number of people: "))
    print("Each pays:", total / people)
except ZeroDivisionError:
    print("Cannot divide among zero people!")

