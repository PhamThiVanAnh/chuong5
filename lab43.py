# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 23:47:04 2024

@author: VanAnh
"""
n = int(input("Nhập số nguyên dương n: "))

if n <= 0:
    print("Vui lòng nhập một số nguyên dương.")
else:
    tong = 0.0
    for i in range(2 , n+1 ):
            tong += i / (i +1)
print(f"Tổng của các phân số từ 1/2 đến {n}/({n}+1 là {round(tong,3)}")