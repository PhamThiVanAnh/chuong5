# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 10:03:38 2024

@author: Administrator
"""
n = int(input("Nhập vào số nguyên dương:"))
tong = 0
for i in range(1, n+1):
    tong += i*i
print("Tổng các bình phương chữ số từ 1 đến", n, "là:", tong)