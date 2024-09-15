# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 21:15:31 2024

@author: Administrator
"""
N = int(input('Nhập vào số nguyên dương N:'))
while N <= 0:
    N = int(input("Vui lòng nhập số nguyên dương:"))
for i in range(1, N+1):
    if N % i == 0:
        print("Ước chung của N là:", i)