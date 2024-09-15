# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 17:48:12 2024

@author: VanAnh
"""
n = int(input("Nhập số nguyên dương n: "))

if n <= 0:
    print("Vui lòng nhập một số nguyên dương.")
else:
    tong = 0.0
    for i in range(1 , n + 1 ):
            tong += 1 / (2*i)
print(f"Tổng của các phân số từ 1/2 đến 1/{2*n} là {round(tong,3)}")

