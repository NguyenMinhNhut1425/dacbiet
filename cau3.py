# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 16:43:03 2024

@author: MINH NHUT
"""
import random
def so_nguyen_ngau_nhien(n):
    if n < 2:
        return f'{n} không phải số nguyên tố'
    for i in range(2, n):
        if n % i == 0:
            return f'{n} không phải số nguyên tố'
    return f'{n} là số nguyên tố'
n = random.randint(-99, 98)
print(n)
print(so_nguyen_ngau_nhien(n))