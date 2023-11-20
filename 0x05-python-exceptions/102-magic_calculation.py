#!/usr/bin/python3
# using def magic_calculation(a, b) prototype

def magic_calculation(a, b):
    calres = 0
    for idx in range(1, 3):
        try:
            if idx > a:
                raise Exception("Too far")
            calres += a ** b / idx
        except Exception:
            calres = b + a
            break
    return (calres)
