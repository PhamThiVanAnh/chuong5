# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 01:35:07 2024

@author: Administrator
"""

a = int(input("Nhập vào số a: "))
b = int(input("Nhập vào số b: "))
c = int(input("Nhập vào số c: "))
if a <= 0 or b <= 0 or c <= 0:
    print("Vui lòng nhập số nguyên dương")
if a + b <= c or a + c <= b or b + c <= a:
    print("Đây không phải là tam giác")
else:
    if a == b == c:
        print("Tam giác đều")
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        if a == b or a == c or b == c:
            print("Tam giác vuông cân")
        else:
            print("Tam giác vuông")
    elif a == b or a == c or b == c:
        print("Tam giác cân")
    else:
        print("Tam giác thường")