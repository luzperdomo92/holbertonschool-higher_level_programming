#!/bin/bash
# A header variable must be sent with the value 98
curl -sH "X-HolbertonSchool-User-Id:98" "$1"
