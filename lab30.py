# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 22:01:15 2024

@author: Administrator
"""
thang = int(input("Nhập vào tháng(1-12):"))
nam = int(input("Nhập vào năm:"))
thang_31_ngay = [1, 3, 5, 7, 8, 10, 12]
if 1 <= thang <= 12 and nam > 0:
    nhuan = False
    for i in range(4, 501, 396):
      if nam % 400 == 0:
         nhuan = True
         break
      if not nhuan and nam % 4 == 0 and nam % 100 != 0:
           nhuan = True
    if nhuan == True:
               print("Năm này là năm nhuận")
    else:
               print("Năm này không phải là năm nhuận")
    if thang in thang_31_ngay:
        print("Tháng có 31 ngày")
    elif thang == 2:
        if nhuan:
            print("Tháng có 29 ngày")
        else:
            print("Tháng có 28 ngày")
    else:
        print("Tháng có 30 ngày")
else:
    print("Tháng hoặc năm không hợp lệ")