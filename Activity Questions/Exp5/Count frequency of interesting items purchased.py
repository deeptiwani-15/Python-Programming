# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 15:40:03 2026

@author: User
"""

items = [
    "coffee", "croissant", "coffee", "donut", "matcha",
    "coffee", "sandwich", "donut", "bubble_tea", "matcha",
    "coffee", "brownie", "sandwich", "donut", "bubble_tea"
]

frequency = {}

for item in items:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1

print("Item purchase frequency:")
for item, count in frequency.items():
    print(item, ":", count)
