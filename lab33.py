# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 03:46:36 2024

@author: Administrator
"""
import math

n = int(input("Nhập vào số nguyên dương: "))
if n <= 0:
    print(n, "không phải là số chính phương")
else:
    kq = False
    for i in range(1, int(math.sqrt(n))+1):
        if i*i == n:
            kq = True
            break
    if kq:
        print(n, "là số chính phương")
    else:
        print(n, "không phải là số chính phương")