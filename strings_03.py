#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 09:04:31 2025

@author: snow
"""

def get_list(eingabe): 
    return eingabe.split()


eingabe = input("Gebe eine Phrase ein: ")
ausgabe = get_list(eingabe)
print("Du hast insgesamt", len(ausgabe), "Wörter eingegeben!\n" )
print("Und zwar:")
ausgabe.sort()
for i in range(len(ausgabe)):
    print(ausgabe[i])





