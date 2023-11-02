#!/usr/bin/python3
# python program that prints number of and lists of its arguments

if __name__ == "__main__":
    from sys import argv
    argv_count = len(argv) - 1
    if argv_count == 0:
        print("0 arguments.")
    elif argv_count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(argv_count))
    for x in range(argv_count):
        print("{}: {}".format(x + 1, argv[x + 1]))
