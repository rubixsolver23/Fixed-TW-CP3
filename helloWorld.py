import time
import random

print("Type the following or die in the lavaAAA")

time.sleep(5)
while True:
    time.sleep(random.random() * 5)
    time1 = time.time()
    choice = random.choice(["left", "right", "up", "down", "jump", "lean"])
    print(choice)
    timerr = input("Now!!!")
    if timerr != choice:
        break
    total = time.time() - time1
    print("It took you %s seconds bro"% total)
    if total > 4:
        break
print("You lose LLLLLLL")