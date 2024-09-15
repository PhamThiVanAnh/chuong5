# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 11:55:17 2024

@author: Admin
"""
def so(num):
    if num < 2:
        print(False)
        return
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(False)
    print(True)

def dem_so_nguyen_to(n):
    count = 0
    for i in range(2, n):
        so(i)
        if i >= 2 and i < n and not i % 2 == 0:
            count += 1
    print(count)

n = 99  
dem_so_nguyen_to(n)

