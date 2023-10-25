#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
exe = 0
if number < 0:
    number *= -1
    exe = 1
lastd = number % 10
if exe == 1:
    number *= -1
    lastd *= -1
print(f"Last digit of {number} is ".format(number), end="")
if lastd > 5:
    print(f"{number} and is greater than 5".format(lastd))
elif lastd == 0:
    print(f"{number} and is 0".format(lastd))
else:
    print(f"{number} and is less than 6 and not 0".format(lastd))
