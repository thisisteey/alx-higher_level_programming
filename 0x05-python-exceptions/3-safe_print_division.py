#!/usr/bin/python3
# function that divides 2 integers and prints the result
# using def safe_print_division(a, b) prototype

def safe_print_division(a, b):
    quot = None
    try:
        quot = a / b
    except TypeError:
        quot = None
    except ZeroDivisionError:
        quot = None
    finally:
        print("Inside result: {}".format(quot))
    return (quot)
