# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 14:38:45 2026

@author: User
"""


def calculate_emi(principal, rate, years):
    r = rate / (12 * 100)   # monthly interest rate
    n = years * 12          # number of months
    emi = (principal * r * (1 + r) ** n) / ((1 + r) ** n - 1)
    return emi

amount = float(input("Enter loan amount: "))
rate = float(input("Enter annual interest rate: "))
years = int(input("Enter loan duration (years): "))

print("Monthly EMI:", round(calculate_emi(amount, rate, years), 2))
