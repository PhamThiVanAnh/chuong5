# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 01:34:20 2024

@author: VanAnh
"""

n = int(input("Nhập một giá trị nguyên n: "))

tu_dien = {i:i**i for i in range(1,n+1)}

print(tu_dien)
