# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 11:43:28 2024

@author: Admin
"""

def bienso(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print(False)
            break
    else:
        print(True)

bienso(87539319)
