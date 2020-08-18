#!/bin/bash
#  takes in a URL and displays all HTTP methods the server will accept.
# without the word "allow: "
curl -sI "$1" | grep "Allow" | cut -d " " -f2-
