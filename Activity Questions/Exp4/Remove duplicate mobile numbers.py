# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 15:33:26 2026

@author: User
"""

mobile_numbers = [
    9876543210, 9123456789, 9988776655, 9876543210,
    9012345678, 8899776655, 9123456789, 7766554433,
    9988776655, 6655443322, 9543216780
]

unique_numbers = []
for num in mobile_numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print("Contact list without duplicates:")
print(unique_numbers)
