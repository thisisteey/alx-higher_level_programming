#!/usr/bin/python3
# function that prints an integer with "{:d}".format()
# using def safe_print_integer(value) prototype

def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return (True)
    except TypeError:
        return (False)
    except ValueError:
        return (False)
