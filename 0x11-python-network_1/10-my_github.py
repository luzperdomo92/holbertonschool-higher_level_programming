#!/usr/bin/python3
""" script that takes your Github credentials (username and password)
    and uses the Github API to display your id
"""
import requests
import sys


if __name__ == "__main__":
    post_data = requests.get('https://api.github.com/user',
                             auth=(sys.argv[1], sys.argv[2]))
    json_dict = post_data.json()
    try:
        print(json_dict['id'])
    except KeyError:
        print('None')
