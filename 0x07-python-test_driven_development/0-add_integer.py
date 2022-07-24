#!/usr/bin/python3
"""
    My ``0-add_integer`` module.
    This module defines a single function that adds
    two int or floating points numbers together

    >>> add_integer(2, 98)
    100

    >>> add_integer(2, 4.0)
    6
"""


def add_integer(a, b=98):
    """
       adds two ints or floats

       Args:
           a(int, float) - the first int
           b(int, float) - optional second int

       Returns:
               the addition of the int

    """

    err1 = TypeError("a must be an integer")
    err2 = TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    elif type(b) is float:
        b = int(b)
    if type(a) is not int:
        raise err1
    elif type(b) is not int:
        raise err2
    return (a + b)
