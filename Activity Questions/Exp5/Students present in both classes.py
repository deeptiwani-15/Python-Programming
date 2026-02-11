# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 15:39:17 2026

@author: User
"""

class_A = {101, 102, 103, 104, 105, 110}
class_B = {104, 105, 106, 107, 110, 120}

common_students = class_A.intersection(class_B)

print("Students present in both classes:", common_students)
