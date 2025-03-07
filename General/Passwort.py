#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 17:34:24 2025

@author: snow
"""

import random

laenge = int(input("Wie lang soll das Passwort sein? "))

pool = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzÄäÜüÖö1234567890!§$%&/=+*-_.:,;"

passwort = ""

for t in range(laenge):
    passwort = passwort + pool[int(len(pool)*random.random())]
    
print("Das generierte Passwort lautet: " + passwort)
    
