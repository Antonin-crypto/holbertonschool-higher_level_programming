#!/usr/bin/python3
"""
Adds all arguments to a Python list and saves them to a file.
"""


import sys
import json
from os import path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_item():
    """Adds all arguments to a Python list and saves them to a file."""
    filename = 'add_item.json'
    items = []

    # Check if the file already exists and load its content
    if path.exists(filename):
        items = load_from_json_file(filename)

    # Add all command line arguments to the list
    items.extend(sys.argv[1:])

    # Save the list to a JSON file
    save_to_json_file(items, filename)


if __name__ == "__main__":
    add_item()
