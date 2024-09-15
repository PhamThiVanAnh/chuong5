# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 00:17:05 2024

@author: VanAnh
"""

x = float(input("Nhập số [-89.9;88.8]: "))
while x < -89.9 or x > 88.8:
    x = float(input("Sai, nhập lại số: "))
print("Số đã nhập:",x)