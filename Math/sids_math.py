#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 15 08:38:36 2025

@author: snow
"""
from collections import Counter
import math


def is_list_of_numb(values):
    if not isinstance(values, list):
        raise TypeError("The parameter has to be a list")
        
    return all(isinstance(element, (int, float)) for element in values)

def factorial(x: int):
    if not isinstance(x, int):
        raise TypeError("The variable has to be an integer")
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)
        
def digit_sum(x: int):
    if not isinstance(x, int):
        raise TypeError("The variable has to be an integer")
    if (x // 10) == 0: 
        return x
    else: 
        return (x % 10) + digit_sum((x // 10))
    

def average(values):
    if not is_list_of_numb(values):
        raise TypeError("All variables have to be numbers")
    return sum(values) / len(values)

def median(values):
    if not is_list_of_numb(values):
        raise TypeError("All variables have to be numbers")
    
    values = sorted(values)
    if len(values) % 2 == 0:
        return average([values[len(values) // 2],values[(len(values) // 2)-1]])
    else:
        return values[len(values) // 2]    

def modus(values):
    if not is_list_of_numb(values):
        raise TypeError("All variables have to be numbers")
    counts = Counter(values)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items()
            if count == max_count]

def variance(values):
    if not is_list_of_numb(values):
        raise TypeError("All variables have to be numbers")
    av = average(values)
    new_list = [math.pow(x_i-av,2) for x_i in values]
    return (sum(new_list)/len(values))

def deviation(values):
    if not is_list_of_numb(values):
        raise TypeError("All variables have to be numbers")
    return math.sqrt(variance(values))

def data_range(values):
    if not is_list_of_numb(values):
        raise TypeError("All variables have to be numbers")
    return max(values) - min(values)

def quantile(values, p):
    if not is_list_of_numb(values):
        raise TypeError("All variables have to be numbers")
    if not isinstance(p, float):
        raise TypeError("Parameter p has to be numbers")
    if p > 1: 
        raise TypeError("Parameter p must not be greater than 1")
    p_index = int(p * len(values))
    return sorted(values)[p_index]

if __name__ == "__main__":
    x = 123
    print("Factorial of ",x , "is ", factorial(x))
    x = factorial(x)
    print("Digit sum ",x , "is ", digit_sum(x))
    values = [1,2,3,3,7,1,9,5,5,1,6]
    print("Set of values: ", values)
    print("Sorted: ",sorted(values))
    print("Average:", average(values))
    print("Median: ", median(values))
    print("Modus:", modus(values))
    print("Variance: ", variance(values))
    print("Deviation: ", deviation(values))
    print("Range: ", data_range(values))
    print("Quantile 10%", quantile(values, 0.1))
    print("Quantile 75%", quantile(values, 0.75))
