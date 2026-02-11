# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 13:51:05 2026

@author: User
"""


import math

loan = float(input("Enter Loan Amount: "))
rate = float(input("Enter Annual Interest Rate (%): "))
years = int(input("Enter Years: "))

monthly_rate = rate / (12 * 100)
months = years * 12

emi = (loan * monthly_rate * math.pow(1 + monthly_rate, months)) / \
      (math.pow(1 + monthly_rate, months) - 1)

print("Monthly EMI:", round(emi, 2))