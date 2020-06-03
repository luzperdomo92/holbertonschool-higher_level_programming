#!/usr/bin/python3
"""
script that adds all arguments to a
Python list, and then save them to a file
"""

import sys

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

file_name = "add_item.json"

try:
    my_new_list = load_from_json_file(file_name)
except:
    my_new_list = []
for iter in range(1, len(sys.argv)):
    my_new_list.append(sys.argv[iter])
save_to_json_file(my_new_list, file_name)
