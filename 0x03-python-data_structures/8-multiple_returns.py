#!/usr/bin/python3
# returns a tuple, with length of string and first character
# using def multiple_returns(sentence) prototype

def multiple_returns(sentence):
    multup = ()
    if len(sentence) == 0:
        multup = 0, "None"
    else:
        multup = len(senetence), sentence[0]
    return multup
