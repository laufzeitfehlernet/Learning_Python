seed = 543
anzahl = 100
konstante = 499
max = 8191
zufall = [seed] 
for n in range (1, anzahl): 
  neue_zahl= ((zufall[n-1] * konstante)+1) % max  
  zufall.append(neue_zahl)
print(zufall)
