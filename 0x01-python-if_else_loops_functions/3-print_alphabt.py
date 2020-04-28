#!/usr/bin/python3
for letters in range(97, 123):
    if(chr(letters) != 'e' and chr(letters) != 'q'):
        print("{:c}".format(letters), end = "")