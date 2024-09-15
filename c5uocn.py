# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 01:48:21 2024

@author: Admin
"""

N = int(input("Nhập số nguyên dương: "))
while N < 0:
    N = int(input("Sai, nhập lại số: "))
print("Các ước số của N:", [i for i in range(1, N + 1) if N % i == 0])    