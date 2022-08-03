#!/usr/bin/python3
""" The 1-write_file module """


def write_file(filename="", text=""):
    """
        writes text content to a file

        Args:
            filename(str): the file to write to
            text: the text content to write

        Returns: numbers of chars written

    """

    with open(filename, 'w', encoding='utf-8') as f:
        byte_written = f.write(text)
    return (byte_written)
