#!/usr/bin/python3
""" The 3-is_kind_of_class module """


def is_kind_of_class(obj, a_class):
    """ checks if an obj is an instance of , or instance of a class

        inherited from a class
    """
    return (isinstance(obj, a_class))


if __name__ == '__main__':
    a = 1
    if is_kind_of_class(a, int):
        print("{} comes from {}".format(a, int.__name__))
    if is_kind_of_class(a, float):
        print("{} comes from {}".format(a, float.__name__))
    if is_kind_of_class(a, object):
        print("{} comes from {}".format(a, object.__name__))
