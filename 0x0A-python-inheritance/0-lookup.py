#!/usr/bin/python3
""" The 0-lookup module
    provides a single fumction
"""


def lookup(obj):

    """ Returns a list of avialable methods and attribute
in an object
    """

    return (dir(obj))


if __name__ == "__main__":

    class MyClass1(object):
        pass

    class MyClass2(object):
        my_attr1 = 3

        def my_meth(self):
            pass

    print(lookup(MyClass1))
    print(lookup(MyClass2))
    print(lookup(int))
