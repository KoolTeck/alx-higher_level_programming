#!/usr/bin/python3
def safe_print_division(a, b):
    result = 0
    try:
        result = a / b
    except ZeroDivisionError:
        print("{}".format('division by 0'))
    except TypeError:
        print("{}".format('wrong type'))
    finally:
        return (result)


def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            ele = safe_print_division(my_list_1[i], my_list_2[i])
            result.append(ele)
        except IndexError:
            print("{}".format('out of range'))
            result.append(0)
    return (result)
