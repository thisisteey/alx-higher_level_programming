#!/usr/bin/python3
# function that divides element by element 2 lists
# using def list_division(my_list_1, my_list_2, list_length) prototype

def list_division(my_list_1, my_list_2, list_length):
    quotlist = []
    for idx in range(list_length):
        try:
            quot = my_list_1[idx] / my_list_2[idx]
        except TypeError:
            print("wrong type")
            quot = 0
        except ZeroDivisionError:
            print("division by 0")
            quot = 0
        except IndexError:
            print("out of range")
            quot = 0
        finally:
            quotlist.append(quot)
    return (quotlist)
