#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lstdigit = abs(number) % 10
if number < 0:
    lstdigit = -lstdigit
print(f"Last digit od {number:d} is {lstdigit:d} and is ", end="")
if lstdigit > 5:
    print("greater than 5")
elif lstdigit == 0:
    print("0")
else:
    print("less than 6 and not 0")
