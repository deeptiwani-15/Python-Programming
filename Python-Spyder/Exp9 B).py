# -*- coding: utf-8 -*-
"""
Created on Thu Jan  8 14:07:58 2026

@author: User
"""

""" b) DateTime Module"""
import datetime

now = datetime.datetime.now()
print(now.date())
print(now.time())
print(now.strftime("%A"))