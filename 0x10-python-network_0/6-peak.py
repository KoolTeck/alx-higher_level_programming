#!/usr/bin/python3
""" the 6-peak.py module """


def find_peak(list_of_integers):
    """ finds the peak element in a list of int """
    if list_of_integers:
        peak = list_of_integers[0]
        for i in range(1, len(list_of_integers)):
            prev = list_of_integers[i - 1]
            try:
                next = list_of_integers[i + 1]
            except IndexError:
                pass
            current = list_of_integers[i]
            if current == prev or current == next:
                break
            if current > prev and current > next:
                peak = current
        return peak
