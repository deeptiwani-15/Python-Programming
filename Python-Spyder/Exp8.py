# -*- coding: utf-8 -*-
"""
Created on Thu Jan  8 14:05:00 2026

@author: User
"""

"""Exception Handling"""
try:
    a = int(input("Enter number: "))
    print(10 / a)
    lst = [1, 2]
    print(lst[5])
except ZeroDivisionError:
    print("Cannot divide by zero")
except IndexError:
    print("Index error occurred")