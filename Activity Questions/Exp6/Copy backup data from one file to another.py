# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 15:42:02 2026

@author: User
"""

source_file = open("D:/Deepti/FY-BTech/Sem - 2/Activity Questions/Exp6/data.txt", "r")
destination_file = open("D:/Deepti/FY-BTech/Sem - 2/Activity Questions/Exp6/backup.txt", "w")


content = source_file.read()
destination_file.write(content)

source_file.close()
destination_file.close()

print("Backup completed successfully")
