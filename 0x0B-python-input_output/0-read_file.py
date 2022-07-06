#!/usr/bin/python3
"""Contains the number_of_lines function"""


def read_file(filename=""):
    """reads a text file(utf-8) and writes to stdout"""
    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read(), end="")
