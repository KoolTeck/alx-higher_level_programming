#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        num_copy = number * -1
        las_dgt = num_copy % 10
    else:
        las_dgt = number % 10
    print("{:d}".format(las_dgt), end='')
    return (las_dgt)
