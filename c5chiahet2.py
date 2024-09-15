# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 00:23:46 2024

@author: VanAnh
"""

numbers = []
for x in range(2018, 2829):
    if x % 2 == 0 and x % 5 == 0:
        numbers += [x]  
print("Danh sách đã hoàn tất")
print(numbers)


