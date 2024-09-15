# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 23:56:44 2024

@author: VanAnh
"""
n = int(input("Nhập số nguyên dương n: "))

if n <= 0:
    print("Vui lòng nhập một số nguyên dương.")
else:
    tong = 0.0
    for i in range(1 , n+1 ):
            tong += (2*i - 1) / (2*i)
print(f"Tổng của các phân số từ 1/2 đến (2*{n}+1)/(2*{n}+2) là {round(tong,3)}")