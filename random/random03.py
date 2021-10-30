import time

myTime = time.time()
### Get seed based upon microsecond of actual time
microseconds = int((myTime - int(myTime)) * 10000000000000000)
print(microseconds)
seed = microseconds
### Number of random numbers to be created
anzahl = 100
### Constant 
konstante = 4692157436473685
### Max value
max = 98675362126853576
### Range of random numbers
norm = 1000 
zufall_raw = [seed] 
zufall= []
### in order to analyze the strength of the generator 
### we will calculate in which centil the created 
### number belongs to 
auswertung=[0,0,0,0,0,0,0,0,0,0]
for n in range (1, anzahl): 
  neue_zahl= ((zufall_raw[n-1] * konstante)+1) % max  
  zufall_raw.append(neue_zahl)
  zufall.append(neue_zahl % norm)
  centil = int((zufall[n-1] - (zufall[n-1] % 100))/100)
  auswertung[centil]+=1
print(zufall) 
print(auswertung)
