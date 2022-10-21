#!/usr/bin/python3
""" fetches https://alx-intranet.hbtn.io/status """
import urllib.request


if __name__ == "__main__":
    req = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(req) as res:
        html = res.read()
        fmt = """Body response:\n \
\t- type: {}\n \
\t- content: {}\n \
\t- utf8 content: {}\n"""
        print(fmt.format(type(html), html, html.decode("utf-8")), end="")
