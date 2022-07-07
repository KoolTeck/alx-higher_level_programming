#!/usr/bin/python3
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


def best_score(a_dictionary):
    if a_dictionary is not None:
        val_lis = []
        for val in a_dictionary.values():
            val_lis.append(val)
        for key, val in a_dictionary.items():
            best_key = compare(val_lis, val)
            if best_key:
                return key
    return (None)
