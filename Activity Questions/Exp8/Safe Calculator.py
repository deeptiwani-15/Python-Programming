# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 13:48:33 2026

@author: User
"""


try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Enter operator (+, -, *, /): ")

    if op == "+":
        print("Result:", a + b)
    elif op == "-":
        print("Result:", a - b)
    elif op == "*":
        print("Result:", a * b)
    elif op == "/":
        print("Result:", a / b)
    else:
        print("Invalid Operator")

except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")