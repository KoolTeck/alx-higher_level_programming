#!/usr/bin/python3
"""
    defines script that fetches https://alx-intranet
    hbtn.io/status using request
"""

import requests


if __name__ == "__main__":
    r = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
