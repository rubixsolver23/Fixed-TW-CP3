import time
import random

print("This will be a completely new project now!!!")

while True:
    time.sleep(random.random * 5)
    time1 = time.time
    timerr = input("Now!!!")
    total = time.time - time1
    print("It took you %s seconds bro")
    if total > 3:
        break
print("You lose, too slow")