# -*- coding: utf-8 -*-
"""
Created on Thu Jan  8 13:58:51 2026

@author: User
"""

"""File Handling"""
f = open("course.txt", "w")
f.write("Course Outcomes:\nLearn Python basics")
f.close()

f = open("course.txt", "r")
print(f.read())
f.close()