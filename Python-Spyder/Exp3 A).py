# -*- coding: utf-8 -*-
"""
Created on Thu Jan  8 13:49:13 2026

@author: User
"""

n = int(input("Enter rows: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
