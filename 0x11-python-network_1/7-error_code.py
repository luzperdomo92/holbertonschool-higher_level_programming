#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL
    and displays the body of the response.
    If the HTTP status code is greater than or equal to 400
    print: Error code:
"""
import requests
import sys


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    if response:
        print(response.text)
    else:
        print("Error code: {}".format(response.status_code))
