# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 13:46:03 2026

@author: User
"""


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient Balance")

acc = BankAccount(1000)
acc.deposit(500)
acc.withdraw(200)
print("Final Balance:", acc.balance)

