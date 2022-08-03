#!/usr/bin/python3
""" The 7-add_item Module """


import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
try:
    arg_lis = load_from_json_file(filename)
except Exception:
    save_to_json_file([], filename)

if len(sys.argv) > 1:
    arg_lis = load_from_json_file(filename)
    i = 1
    while (i < len(sys.argv)):
        arg_lis.append(sys.argv[i])
        i += 1
    save_to_json_file(arg_lis, filename)
