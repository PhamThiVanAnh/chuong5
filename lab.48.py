# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 01:30:19 2024

@author: VanAnh
"""
tong = 979
min_sum = float('inf')  
tongnghiem = None
for x in range(1, tong // 2 + 1):  
    for y in range(1, tong // 7 + 1):  
        for z in range(1, tong // 9 + 1):
            if 2 * x + 7 * y + 9 * z == tong:
                tongnghiem = x + y + z
                if tongnghiem < min_sum:
                    min_sum = tongnghiem
                    bonghiem = (x, y, z)
if bonghiem:
    x, y, z = bonghiem
    print(f"Nghiệm có tổng x + y + z nhỏ nhất là: x = {x}, y = {y}, z = {z}")
    print(f"Tổng x + y + z = {min_sum}")
else:
    print("Không có nghiệm nào thỏa mãn.")
