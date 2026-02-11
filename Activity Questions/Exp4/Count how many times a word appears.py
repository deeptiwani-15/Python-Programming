# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 15:34:22 2026

@author: User
"""

review = """
This phone is very good and the battery life is good.
The camera quality is good and the display is very good.
The phone feels good in hand and the performance is good.
Many users say the phone is good for gaming and good for daily use.
The sound quality is good and the call clarity is very good.
Overall, this phone gives a good experience and good value.

In the second paragraph, the phone continues to show good results.
The build quality is good and the software experience is good.
The charging speed is good and the backup is very good.
Even after long usage, the phone remains good and reliable.
Most customers give good feedback and good ratings online.
This makes the phone a good choice for buyers.
"""

word = "good"

review = review.lower()
word = word.lower()

words = review.split()
count = 0

for w in words:
    if w == word:
        count += 1

print("The word appears", count, "times")