#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            ele = my_list_1[i] / my_list_2[i]
            result.append(ele)
        except ZeroDivisionError:
            print("{}".format('division by 0'))
            result.append(0)
        except (ValueError, TypeError):
            print("{}".format('wrong type'))
            result.append(0)
        except IndexError:
            print("{}".format('out of range'))
            result.append(0)
    return (result)
