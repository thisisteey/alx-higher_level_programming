#!/usr/bin/python3
for numeral1 in range(0, 10):
    for numeral2 in range(numeral1 + 1, 10):
        if numeral1 == 8 and numeral2 == 9:
            print("{}{}".format(numeral1, numeral2))
        else:
            print("{}{}".format(numeral1, numeral2), end=", ")
