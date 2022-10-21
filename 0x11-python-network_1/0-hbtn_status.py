#!/usr/bin/python3
""" fetches https://alx-intranet.hbtn.io/status """
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as res:
        html = res.read()
        fmt = """Body response:\n \
\t- type: {}\n \
\t- content: {}\n \
\t- utf8 content: {}\n"""
        print(fmt.format(type(html), html, res.msg), end="")
