# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 09:58:17 2024

@author: Administrator
"""
n = int(input("Nhập vào số nguyên dương:"))
tong = 0
for i in range(1, n+1):
    tong += i
print("Tổng các chữ số từ 1 đến", n, "là:", tong)