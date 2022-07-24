#!/usr/bin/python3
"""
   The 3-say_my_name module
   ------------------------
   this module consists a single function say_my_name

   Example:
           >>> say_my_name("John", "Smith")
           My name is John Smith
"""


def say_my_name(first_name, last_name=""):
    """
       Prints names argument to stdout

       Args:
           first_name(str): first name arg
           last_name: optional name arg

       Returns:
              nothing
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    if last_name:
        print("My name is {:s} {:s}".format(first_name, last_name))
    else:
        print("My name is {:s}".format(first_name))


if __name__ == "__main__":
    say_my_name("John", "Smith")
    say_my_name("Walter", "White")
    say_my_name("Bob")
    try:
        say_my_name(12, "White")
        say_my_name(None)
    except Exception as e:
        print(e)
    try:
        say_my_name(None)
    except Exception as e:
        print(e)
