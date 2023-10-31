#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10
if number < 0:
    last *= -1
else:
    pass

str = "Last digit of"
if last > 5:
    print(f"{str} {number} is {last} and is greater than 5")
elif last == 0:
    print(f"{str} {number} is {last} and is {last}")
else:
    print(f"{str} {number} is {last} and is less than 6 and not 0")
