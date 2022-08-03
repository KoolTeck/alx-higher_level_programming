#!/usr/bin/python3
import json
"""
    The 3-to_json_string module

"""


def to_json_string(my_obj):
    """ serializes an obj to its string representation """

    return (json.dumps(my_obj))
