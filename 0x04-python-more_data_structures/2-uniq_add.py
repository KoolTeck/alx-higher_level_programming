#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq = 0
    for n in set(my_list):
        uniq += n
    return (uniq)
