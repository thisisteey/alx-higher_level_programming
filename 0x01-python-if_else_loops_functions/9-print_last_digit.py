#!/usr/bin/python3
# fucntion that shows that last digit of a number
# using the def print_last_digit(number prototype

def print_last_digit(number):
    print(abs(number) % 10, end="")
    return (abs(number) % 10)
