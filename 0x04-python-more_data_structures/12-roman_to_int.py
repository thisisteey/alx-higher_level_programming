#!/usr/bin/python3
# converts a Roman numeral to an integer
# using def roman_to_int(roman_string) prototype

def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    rmdict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    indec = [rmdict[num] for num in roman_string]
    fig = 0
    for dig in range(len(indec)):
        fig += indec[dig]
        if indec[dig - 1] < indec[dig] and dig != 0:
            fig -= (indec[dig - 1] + indec[dig - 1])
    return fig
