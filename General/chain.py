#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 30 12:03:01 2025


"""

from itertools import chain 
from typing import Iterator 
from sys import getsizeof
from string import ascii_letters


print(ascii_letters)

# First chain
a: list[int] = [1,2,3]
b: list[int] = [111,222]
my_chain: Iterator[int] = chain(a,b)

print(list(my_chain))

# Chain from list of lists
my_lists: list[list[int]] = [[4,5,6],[333,444]]

new_chain: Iterator[int] = chain.from_iterable(my_lists)
print(list(new_chain))

# Efficency
iter1: Iterator[str] = iter(ascii_letters)
iter2: Iterator[int] = iter(range(1_000_000))
next_chain: Iterator[str | int] = chain(iter1, iter2)

print(getsizeof(iter1), 'bytes')
print(getsizeof(iter2), 'bytes')
print(getsizeof(next_chain), 'bytes')

extracted: list[str | int] = list(next_chain)
print(getsizeof(extracted), 'bytes')
