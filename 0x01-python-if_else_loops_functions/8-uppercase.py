#!/usr/bin/python3
# function that shows a string in uppercase
# using the prototype def uppercase(str)

def uppercase(str):
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            c = chr(ord(c) - 32)
        print("{:s}".format(c), end='')
    print('\n', end="")
