#!/usr/bin/python3
"""script that fetches https://intranet.hbtn.io/status"""
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        page_fech = response.read()

    print("Body response:")
    print("\t- type: {}".format(type(page_fech)))
    print("\t- content: {}".format(page_fech))
    print("\t- utf8 content: {}".format(page_fech.decode("utf8")))
