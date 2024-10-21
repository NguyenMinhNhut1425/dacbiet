# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 16:08:23 2024

@author: MINH NHUT
"""

def kiem_tra_chuoi_palindrome(chuoi):
    chuoi_1 = chuoi.replace(' ', '').lower()
    chuoi_dao = chuoi[::-1]
    if chuoi_1 == chuoi_dao:
        return f'{chuoi} là chuỗi Palindrome'
    else:
        return f'{chuoi} không phải là chuỗi Palindrome'
print(kiem_tra_chuoi_palindrome("hello"))
print(kiem_tra_chuoi_palindrome("madam"))