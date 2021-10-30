import time

myTime = time.time()

microseconds = int((myTime - int(myTime)) * 10000000000000000)
print(microseconds)
