# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 15:58:55 2026

@author: User
"""

# Step 1: Store daily expenses in a file
daily_expenses = [250, 400, 150, 300, 500, 200, 350, 450, 100, 300,
                  200, 400, 250, 150, 500, 300, 350, 200, 400, 150,
                  300, 250, 450, 500, 200, 300, 400, 350, 150, 200]

# Write daily expenses to a file
with open("expenses.txt", "w") as file:
    for expense in daily_expenses:
        file.write(str(expense) + "\n")

print("Daily expenses saved in 'expenses.txt'")

# Step 2: Read expenses from the file and calculate total
total_expense = 0
with open("expenses.txt", "r") as file:
    for line in file:
        total_expense += int(line.strip())

print("Total monthly expense:", total_expense)
