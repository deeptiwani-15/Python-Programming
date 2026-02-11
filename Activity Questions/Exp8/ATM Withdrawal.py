# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 13:48:32 2026

@author: User
"""


balance = 5000

try:
    amount = float(input("Enter withdrawal amount: "))
    if amount > balance:
        raise ValueError("Insufficient Balance")
    balance -= amount
    print("Remaining Balance:", balance)
except ValueError as e:
    print("Error:", e)

