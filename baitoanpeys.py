# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 12:07:29 2024

@author: Admin
"""

import math
def xs_1_sau():
    k_1_sau = (5/6) ** 6 
    xs_1 = 1 - k_1_sau
    print(f"Xác suất có ít nhất một lần số 1 khi gieo 6 lần: {xs_1:.4f}")
    return xs_1

def xs_2_muoi_hai():
    k_1_muoi_hai = (5/6) ** 12  
    d_1_muoi_hai = (math.comb(12, 1) * (1/6) * (5/6) ** 11) 
    xs_2 = 1 - (k_1_muoi_hai + d_1_muoi_hai)  
    print(f"Xác suất có ít nhất hai lần số 1 khi gieo 12 lần: {xs_2:.4f}")
    return xs_2

xs1 = xs_1_sau()
xs2 = xs_2_muoi_hai()

if xs1 > xs2:
    print("Gieo 6 lần có khả năng nhận được ít nhất một lần số 1 cao hơn.")
else:
    print("Gieo 12 lần có khả năng nhận được ít nhất hai lần số 1 cao hơn.")

