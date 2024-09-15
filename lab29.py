# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 21:41:56 2024

@author: Administrator
"""
N = int(input("Nhập vào số nguyên dương:"))
tong = 0
while N > 0:
    chu_so = N % 10
    tong += chu_so
    N//= 10
print("Tổng các chữ số N là:", tong)
    