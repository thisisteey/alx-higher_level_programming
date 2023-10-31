#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lstdigit = number % 10 if number >= 0 else ((-number % 10) * -1)
print("Last digit of", number "is", lstdigit, end=" ")
if lstdigit > 5:
    print("and is greater than 5")
elif lstdigit == 0:
    print("and is 0")
else lstdigit < 6 and lstdigit != 0:
    print("and is less than 6 and not 0")
