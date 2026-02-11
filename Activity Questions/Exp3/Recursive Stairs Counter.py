# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 13:41:55 2026

@author: User
"""

def stairs(n):
    if n == 0:
        return 0
    return 1 + stairs(n - 1)

steps = int(input("Enter number of stairs climbed: "))
print("Total stairs counted:", stairs(steps))
