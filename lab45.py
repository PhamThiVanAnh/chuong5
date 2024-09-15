# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 00:32:01 2024

@author: VanAnh
"""

n = int(input("Nhập số nguyên dương n: "))
x = float(input("nhập giá trị x: "))

if n <= 0:
    print("Vui lòng nhập một số nguyên dương.")
else:
    S = 0.0
    for i in range(1 , n+1 ):
        tongdayso = sum(range(1, i+1))
        S += (x**i)/tongdayso
    S += x    
print(f"Tổng là : {round(S,3)}")