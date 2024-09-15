# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 12:15:17 2024

@author: Admin
"""

import random

def khong_chuyen(n):
    return sum(random.randint(0, 2) == random.randint(0, 2) for _ in range(n))

def chuyen(n):
    return sum(random.randint(0, 2) != random.randint(0, 2) for _ in range(n))

def mo_phong(n):
    print(f"Không chuyển đổi: {khong_chuyen(n) / n:.2%}")
    print(f"Chuyển đổi: {chuyen(n) / n:.2%}")

mo_phong(100)
