#!/usr/bin/python3
# function that prints a text with 2 new lines after
# each of these characters: ., ? and :
"""A function that prints a text with two new lines after each '.'
'?' and ':' charcaters"""


def text_indentation(text):
    """Args:
    text (str): the text to print
    Error to raise:
    TypeError: if the text is not a string"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    curridx = 0
    while curridx < len(text) and text[curridx] == ' ':
        curridx += 1
    while curridx < len(text):
        print(text[curridx], end="")
        if text[curridx] == "\n" or text[curridx] in ".?":
            if text[curridx] in ".?":
                print("\n")
            curridx += 1
            while curridx < len(text) and text[curridx] == ' ':
                curridx += 1
            continue
        curridx += 1
