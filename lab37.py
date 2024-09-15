# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 10:09:05 2024

@author: Administrator
"""
n = int(input("Nhập số chẵn:"))
tong = 0
if n % 2 == 0:
    for i in range(2, n+1, 2):
        tong += i
    print("Tổng các số chẵn là:", tong)
else:
    print("Vui lòng nhập số chẵn")