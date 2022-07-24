#!/usr/bin/python3
"""
   4-print_square.py module

   module provides single function print_square(size)

   sample:
         >>> print_square(4)
         ####
         ####
         ####
         ####
"""


def print_square(size):
    """
       prints a square with the character #.

        Args:
            size(int): the size of square
    """

    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if size == 0:
        print()
    for j in range(size):
        print('#' * size)
