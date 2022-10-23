#!/usr/bin/python3
"""
    defines script that takes in a letter, sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import sys
import requests


if __name__ == "__main__":
    q = "" if len(sys.argv) == 1 else sys.argv[1]
    try:
        r = requests.post("http://0.0.0.0:5000/search_user", data={'q': q})
        json = r.json()
        if len(json) == 0:
            print("No result")
        else:
            print("[{}] {}".format(json['id'], json['name']))
    except ValueError:
        print("Not a valid JSON")
