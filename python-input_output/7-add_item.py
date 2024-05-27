#!/usr/bin/python3
"""constaint the Load, add, save"""


import json
import sys
from os import path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_item_to_list_and_save():
    """script that adds all arguments to a Python list,
    and then save them to a file:"""
    # Check if the file exists
    if path.exists("add_item.json"):
        # Load existing data
        data = load_from_json_file("add_item.json")
    else:
        data = []

    # Add arguments to the list
    for arg in sys.argv[1:]:
        data.append(arg)

    # Save the list to a JSON file
    save_to_json_file(data, "add_item.json")


if __name__ == "__main__":
    add_item_to_list_and_save()
