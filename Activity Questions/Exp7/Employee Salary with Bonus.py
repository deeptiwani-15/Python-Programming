# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 13:46:10 2026

@author: User
"""


class Employee:
    def __init__(self, salary, bonus_percent):
        self.salary = salary
        self.bonus_percent = bonus_percent

    def total_salary(self):
        bonus = self.salary * self.bonus_percent / 100
        return self.salary + bonus

salary = float(input("Enter salary: "))
bonus = float(input("Enter bonus %: "))

emp = Employee(salary, bonus)
print("Total Salary:", emp.total_salary())