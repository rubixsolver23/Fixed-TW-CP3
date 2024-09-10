import time
import random

print("This will be a completely new project now!!!")

time.sleep(5)
while True:
    time.sleep(random.random() * 5)
    time1 = time.time()
    choice = random.choice(["type", "yes"])
    print(choice)
    timerr = input("Now!!!")
    if timerr != choice:
        break
    total = time.time() - time1
    print("It took you %s seconds bro"% total)
    if total > 3:
        break
print("You lose LLLLLL")