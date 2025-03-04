#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  
#  Copyright 2020 Dirk  
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import random 

Max_add = 1000
Max_mult = 10
punkte = 0

for i in range(1, 11):
	operator = random.randint(1,4)
	if operator == 1: #addieren
		op = "+"
		a = random.randint(1,Max_add)
		b = random.randint(1,Max_add)
		ergebnis = a + b
	if operator == 2: #multiplizieren
		op = "*"
		a = random.randint(1,Max_mult)
		b = random.randint(1,Max_mult)
		ergebnis = a*b
	if operator == 3: #subtrahieren
		op = "-"
		a = random.randint(1,Max_add)
		b = random.randint(1,Max_add)
		if b > a:
			a, b = b, a
		ergebnis= a - b
	if operator == 4: #dividieren
		op = ":"
		a = random.randint(1,Max_mult)
		b = random.randint(1,Max_mult)
		ergebnis = a * b
		ergebnis, a = a, ergebnis

	rechnung = int(input("\nAufgabe: " + str(i) + ": Wieviel ist " + str(a) + " " + op + " " + str(b)  + " ? Deine Antwort: "))
	if ergebnis == rechnung:
		print("\nDas ist richtig!")
		punkte = punkte + 1
	else: 
		print("\nDas ist leider falsch!  " + str(ergebnis) + " wäre die richtige Antwort gewesen!")

print("\nDu hast insgesamt " + str(punkte) + " Punkte erreicht!")
