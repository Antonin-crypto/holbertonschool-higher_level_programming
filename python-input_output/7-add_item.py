#!/usr/bin/python3
"""Adds all arguments to a Python list and saves them to a file."""


import sys
import json
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

try:
    json_list = load_from_json_file('add_item.json')
except FileNotFoundError:
    json_list = []

for i in range(1, len(sys.argv)):
    json_list.append(sys.argv[i])

save_to_json_file(json_list, "add_item.json")
