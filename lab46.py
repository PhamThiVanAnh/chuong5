# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 00:56:11 2024

@author: VanAnh
"""
tong = 979

for x in range(1, tong // 2 + 1):  
    for y in range(1, tong // 7 + 1): 
        for z in range(1, tong // 9 + 1): 
            if 2 * x + 7 * y + 9 * z == tong:
                print(f"x = {x}, y = {y}, z = {z}")

