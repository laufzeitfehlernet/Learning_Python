#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 15 08:38:36 2025

@author: snow
"""

def is_list_of_numb(values):
    if not isinstance(values, list):
        raise TypeError("The parameter has to be a list")
        
    return all(isinstance(element, (int, float)) for element in values)

def fakultaet(x: int):
    if not isinstance(x, int):
        raise TypeError("The variable has to be an integer")
    if x == 1:
        return 1
    else:
        return x * fakultaet(x-1)
        
def quersumme(x: int):
    if not isinstance(x, int):
        raise TypeError("The variable has to be an integer")
    if (x // 10) == 0: 
        return x
    else: 
        return (x % 10) + quersumme((x // 10))
    

def mittelwert(werte):
    if is_list_of_numb(werte):
        return sum(werte) / len(werte)
    else: 
        raise TypeError("All variables have to be numbers")

def median(werte):
    if is_list_of_numb(werte):
        werte = sorted(werte)
        print(werte)
        print(len(werte) // 2)
        
        if len(werte) % 2 == 0:
            return mittelwert([werte[len(werte) // 2],werte[(len(werte) // 2)-1]])
        else:
            return werte[len(werte) % 2]    
        return
    else:
        raise TypeError("All variables have to be numbers")
        
        
if __name__ == "__main__":
    werte = [1,4,3,3,17,111]
    print(mittelwert(werte))
    print(median(werte))
