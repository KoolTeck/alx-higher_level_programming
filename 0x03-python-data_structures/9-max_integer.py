#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) > 0:
        for i in my_list:
            check = compare(my_list, i)
            if check:
                return (i)
    else:
        return None


def compare(my_list, element):
    """
       compare - compares element in a list
       my_list: the list to traverse
       element: the int to compare
       Return: true if element is greater, false otherwise
    """
    for ele in my_list:
        if element >= ele:
            continue
        else:
            return False
    return True
