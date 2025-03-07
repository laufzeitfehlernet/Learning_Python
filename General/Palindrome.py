#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 07:38:04 2025

@author: snow
"""

eingabe = input("Gib ein Wort ein und ich prüfe, ob es ein Palindrom ist: ")

if eingabe.upper() == eingabe[::-1].upper():
    print("Deine Eingabe " + eingabe + " ist ein Palindrom")
else:
    print("Deine Eingabe " + eingabe + " ist kein Palindrom")
    
