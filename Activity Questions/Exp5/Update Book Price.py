# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 13:45:06 2026

@author: User
"""


library = {"Python": 500, "Java": 400}

book = input("Enter book name to update: ")
new_price = int(input("Enter new price: "))

library[book] = new_price
print("Updated Library:", library)