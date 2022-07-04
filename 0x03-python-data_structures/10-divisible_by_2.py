#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    lis_len = len(my_list)
    if lis_len > 0:
        lis_copy = my_list.copy()
        for i in range(lis_len):
            lis_copy[i] = True if my_list[i] % 2 == 0 else False
        return (lis_copy)
