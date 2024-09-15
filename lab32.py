# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 03:09:47 2024

@author: Administrator
"""
so_km = float(input("Nhập số km: "))
gia_km_dau = 15000
gia_km_2_den_5 = 13500
gia_km_tu_6 = 11000
giam_gia = 0.1
if so_km <= 0:
    print("Số km không hợp lệ")
tong_tien = 0
for km in range(1, int(so_km) + 1):
      if km == 1:
          tong_tien += gia_km_dau
      elif 1 < km <= 5:
          tong_tien += gia_km_2_den_5
      else:
          tong_tien += gia_km_tu_6
if so_km > 120:
      tong_tien *= (1 - giam_gia)
print("Số tiền phải trả là:", tong_tien,"đồng")