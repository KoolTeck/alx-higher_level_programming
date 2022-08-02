#!/usr/bin/python3
""" The 1-my_list module, supplies a single class """


class MyList(list):

    """ extends on list builtin """

    def print_sorted(self):
        """ prints list in sorted order """
        print(sorted(self))


if __name__ == "__main__":
    my_list = MyList([1, 2, 5, 4, 3])
    print(my_list)
    my_list.print_sorted()
    print(my_list)
