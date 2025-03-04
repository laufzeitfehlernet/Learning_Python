### Create a random number just because of the microseconds 
### of the actual time of the system

import time

myTime = time.time()

microseconds = int((myTime - int(myTime)) * 10000000000000000)
print(microseconds)
