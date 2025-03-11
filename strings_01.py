#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 09:04:31 2025

@author: snow
"""

eingabe = input("Gebe eine Phrase ein: ")

# Alternierend
ausgabe = ""
for zaehler in range(len(eingabe)):
    if zaehler % 2 == 0: 
        ausgabe +=eingabe.upper()[zaehler]
    else: 
        ausgabe +=eingabe.lower()[zaehler]
        
print(ausgabe)

