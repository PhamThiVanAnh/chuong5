# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 11:48:04 2024

@author: Admin
"""

def tinh_isbn(ma):
    tong = 0
    for i in range(9):
        tong += (10 - i) * int(ma[i])
    chusokt = (11 - tong % 11) % 11
    if chusokt == 10:
        chusokt = 'X'
    print(ma + str(chusokt))
ma = input("Nhập số 9 chữ số: ")
tinh_isbn(ma)
