#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is not None:
        rev = my_list[::-1]
        [print("{:d}".format(n)) for n in rev]
