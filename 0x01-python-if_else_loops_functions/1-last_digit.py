#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lstdigit = abs(number) % 10
if number < 0:
    lstdigit = -lstdigit
print(f"Last digit of {number:d} is {digit:d} and is ", end="")
if lstdigit > 5:
    print("greater than 5")
elif lstdigt == 0:
    print("0")
else:
    print("less than 6 and not 0")
