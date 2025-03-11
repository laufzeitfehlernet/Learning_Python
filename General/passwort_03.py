#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 22:22:44 2025

@author: snow
"""

import string
import secrets

laenge = int(input("Wie lang soll das Passwort sein? "))

alphabet = string.ascii_letters + string.digits + string.punctuation
while True:
    password = ''.join(secrets.choice(alphabet) for i in range(laenge))
    if (any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and any(c in string.punctuation for c in password)
            and sum(c.isdigit() for c in password) >= 3):
        break
    
print(password)