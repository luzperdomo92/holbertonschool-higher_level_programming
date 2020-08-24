#!/usr/bin/python3
"""
    script that takes in a URL and an email, sends a POST request to the
    passed URL with the email as a parameter, and displays the body of
    the response (decoded in utf-8)
"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = {'email': sys.argv[2]}

    # POST request = send data to a URL.
    data = urllib.parse.urlencode(email)

    # data should be bytes
    data = data.encode("ascii")
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        resq_data = response.read()
        print("{}".format(resq_data.decode("utf8")))
