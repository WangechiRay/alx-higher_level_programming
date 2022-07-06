#!/usr/bin/python3
"""from_json_string(my_str) function"""


import json


def from_json_string(my_str):
    """the function returns an object repr by json string"""
    return json.loads(my_str)
