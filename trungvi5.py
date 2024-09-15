# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 12:03:34 2024

@author: Admin
"""

def trung_vi(a, b, c, d, e):
    so = [a, b, c, d, e]
    so.sort()
    return so[2] 
a = int(input("Nhập số nguyên thứ nhất: "))
b = int(input("Nhập số nguyên thứ hai: "))
c = int(input("Nhập số nguyên thứ ba: "))
d = int(input("Nhập số nguyên thứ tư: "))
e = int(input("Nhập số nguyên thứ năm: "))
print("Trung vị là:", trung_vi(a, b, c, d, e))
