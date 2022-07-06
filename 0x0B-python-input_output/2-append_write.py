#!/usr/bin/python3
"""defines append_write function"""


def append_write(filename="", text=""):
    """appends a string at the end of a textfile(utf-8)"""
    with open(filename, "a", encoding="utf-8")as f:
        return f.write(text)
