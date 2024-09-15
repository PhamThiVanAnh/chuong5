# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 01:24:24 2024

@author: VanAnh
"""
numbers = [i for i in range(2020, 3839) if i % 2 == 0]

chia_9 = [num for num in numbers if num % 9 == 0]
for num in chia_9:
    print(num, end='\t')
print()