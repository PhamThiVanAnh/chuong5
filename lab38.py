# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 17:26:41 2024

@author: VanAnh
"""
n = int(input("Nhập số lẻ dương n: "))
if n <= 0 or n % 2 == 0:
    print("Vui lòng nhập một số lẻ dương")
else:
    S = 1
    for i in range(1, n + 1):
        S *= i
    print(f"Giá trị của S = 1 * 2 * 3 * ... * {n} là {S}")
