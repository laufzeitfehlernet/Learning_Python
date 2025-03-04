### To calculate the Collatz conjecture

start = int(input("Enter a integer to start the madness: "))
loop = 1
print(start)
while start > 1:
  if (start % 2) == 0:
    start = int(start / 2)
  else: 
      start = start * 3 + 1
  loop+=1
  print(start)
print("It was in total", loop, "loops it it ends!")
