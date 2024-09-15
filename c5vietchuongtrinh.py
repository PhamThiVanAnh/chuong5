# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 17:56:53 2024

@author: VanAnh
"""

import random
so_phan_tu = random.randint(20, 30)
danh_sach = [random.randint(18, 100) for _ in range(so_phan_tu)]
print("Số lượng phần tử:", so_phan_tu)
print("Danh sách các phần tử:", danh_sach)