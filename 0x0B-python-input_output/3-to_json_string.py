#!/usr/bin/python3
"""
    The 3-to_json_string module

"""


import json


def to_json_string(my_obj):
    """ serializes an obj to its string representation """

    return (json.dumps(my_obj))
