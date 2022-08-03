#!/usr/bin/python3
"""
   The 2-append module

"""


def append_write(filename="", text=""):

    """ opens and appends to a file """

    with open(filename, 'a', encoding='utf-8') as f:
        byts_written = f.write(text)
    return (byts_written)
