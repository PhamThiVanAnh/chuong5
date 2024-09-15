# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 01:07:37 2024

@author: VanAnh
"""
tong = 979
max_tong= 0
tongnghiem= None
for x in range (1, tong // 2 +1):
    for y in range (1, tong // 7 + 1):
        for z in range (1, tong // 9 +1):
            if 2*x +7*y + 9*x == tong:
                tongnghiem = x + y +z
                if tongnghiem > max_tong:
                    max_tong = tongnghiem
                    bonghiem = (x, y, z)
if bonghiem:
    x, y, z = bonghiem
    print(f"Nghiệm có tổng x + y + z lớn nhất là:x = {x}, y = {y}, z = {z}")
    print(f"Tổng x + y + z = {max_tong}")
else:
    print("Không có nghiệm nào thỏa mãn.")