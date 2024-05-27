#!/usr/bin/python3
"""contains the To JSON string"""


import json


def from_json_string(my_str):
    """function that returns the JSON representation of an object (string)"""
    return json.loads(my_str)
