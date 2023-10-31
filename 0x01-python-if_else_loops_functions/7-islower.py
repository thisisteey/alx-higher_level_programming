#!/usr/bin/python3
# fucntion that checks for lowercase characters
# using def islower(c) prototype

def islower(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
