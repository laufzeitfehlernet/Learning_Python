#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 30 12:19:49 2025

@author: idently.io
"""

from itertools import repeat
from timeit import timeit

def for_range(): 
    for _ in range(1_000_000):
        pass
    
def for_repeat():
    for _ in repeat(None, 1_000_000):
        pass
    
range_time = timeit(for_range, number=100)
print(f'{range_time=:.3f}s')

repeat_time = timeit(for_repeat, number=100)
print(f'{repeat_time=:.3f}s')
