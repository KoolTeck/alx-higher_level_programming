#!/usr/bin/python3
""" inherit module """


def inherits_from(obj, a_class):
    """
    checks if an obj is inherited directly or indirectly

    """

    if isinstance(type(obj), a_class):
        if type(obj) is not a_class:
            return (True)
    return False


if __name__ == "__main__":
    a = True
    if inherits_from(a, int):
        print("{} inherited from class {}".format(a, int.__name__))
    if inherits_from(a, bool):
        print("{} inherited from class {}".format(a, bool.__name__))
    if inherits_from(a, object):
        print("{} inherited from class {}".format(a, object.__name__))
