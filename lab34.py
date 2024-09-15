# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 03:51:51 2024

@author: Administrator
"""
import math
n = int(input("Nhập vào số nguyên dương:"))
is_prime = True
if n <= 1:
    is_prime = False
for i in range(2, int(math.sqrt(n))+1):
    if n % i == 0:
        is_prime = False
        break
if is_prime:
    print(n, "là số nguyên tố")
else:
    print(n, "không phải số nguyên tố")