# -*- coding: utf-8 -*-
"""
Created on Thu Jan  8 14:04:13 2026

@author: User
"""

"""Object-Oriented Programming"""
class Employee:
    def __init__(self, name, eid, salary):
        self.name = name
        self.eid = eid
        self.salary = salary

    def gross_salary(self):
        return self.salary + 2000

    def display(self):
        print(self.name, self.eid, self.gross_salary())

e = Employee("Deepti", 101, 30000)
e.display()