#!/usr/bin/python3
"""
    The 0-read_file nodule

"""


def read_file(filename=""):

    """ Reads a file and print to stdout

        Args:
            filename: the name of the file to read from

    """

    with open(filename, encoding='utf-8') as f:
        for line in f:
            print(line, end='')
