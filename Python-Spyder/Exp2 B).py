# -*- coding: utf-8 -*-
"""
Created on Thu Jan  8 13:47:36 2026

@author: User
"""

n = int(input("Enter number: "))
fact = 1

for i in range(1, n + 1):
    fact *= i

print("Factorial:", fact)
1