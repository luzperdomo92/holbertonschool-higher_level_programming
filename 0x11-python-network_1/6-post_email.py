#!/usr/bin/python3
"""
    script that takes in a URL, sends a request to the URL
    and displays the value of the variable X-Request-Id in the response header
 """
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = {'email': sys.argv[2]}
    post_data = requests.post(url, data=email)
    print(post_data.text))
