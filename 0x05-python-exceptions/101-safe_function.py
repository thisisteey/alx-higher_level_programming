#!/usr/bin/python3
# function that executes a function safely
# using def safe_function(fct, *args) prototype

def safe_function(fct, *args):
    from sys import stderr
    try:
        funcres = fct(*args)
    except Exception as excerr:
        print("Exception: {}".format(excerr), file=stderr)
        return None
    else:
        return funcres
