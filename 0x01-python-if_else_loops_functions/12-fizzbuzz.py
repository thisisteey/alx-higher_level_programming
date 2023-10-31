#!/usr/bin/python3
# functions that prints number from 1 to 100 doing the fizzbuzz challenge
# using the def fizzbuzz() prototype

def fizzbuzz():
    for digit in range(1, 101):
        if digit % 3 == 0 and digit % 5 == 0:
            print("FizzBuzz ", end="")
        elif digit % 3 == 0:
            print("Fizz ", end="")
        elif digit % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(digit), end="")
