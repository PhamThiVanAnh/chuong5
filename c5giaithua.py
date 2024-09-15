# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 18:54:03 2024

@author: VanAnh
"""
n = int(input("Nhập số n: "))
giai_thua = 1
for i in range(1, n + 1):
    giai_thua = giai_thua * i
print("Giai thừa của", n, "là:", giai_thua)
