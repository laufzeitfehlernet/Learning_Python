#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 09:04:31 2025

@author: snow
"""

def konvertiere(eingabe): 
    ausgabe = ""
    for zaehler in range(len(eingabe)):
        if zaehler % 2 == 0: 
            ausgabe +=eingabe.upper()[zaehler]
        else: 
            ausgabe +=eingabe.lower()[zaehler]
    return ausgabe


eingabe = input("Gebe eine Phrase ein: ")
print(konvertiere(eingabe))


