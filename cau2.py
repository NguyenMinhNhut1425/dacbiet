# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 16:25:14 2024

@author: MINH NHUT
"""

def tim_phan_tu_list_x(danh_sach, x):
    try:
        vi_tri = danh_sach.index(x)
        return f"Giá trị {x} có vị trí là {vi_tri}"
    except ValueError:
        return f"Giá trị {x} có vị trí là None"
danh_sach = [1,3,5,7,9,11]
print(tim_phan_tu_list_x(danh_sach, 5))
print(tim_phan_tu_list_x(danh_sach, 10))