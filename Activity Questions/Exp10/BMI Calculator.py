# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 13:53:56 2026

@author: User
"""

weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))

bmi = weight / (height ** 2)

print("Your BMI:", round(bmi, 2))

