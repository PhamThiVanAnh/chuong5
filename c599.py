# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 00:07:10 2024

@author: Admin
"""

x = int(input("Nhập số [-99, 99]: "))
while x < -99 or x > 99:
    x= int(input("Sai, nhập lại số: "))
print("Số đã nhập:", x)
     
      