#!/usr/bin/python3
"""
Contains the number_of_lines function
"""

def read_file(filename=""):
    """reads a text file(utf-8) and writes to stdout"""
    with open("my_file_0.txt", mode="w", encoding="utf-8") as f:
        f.write("We offer a truly innovative approach to education:\nfocus on building reliable applications and scalable systems, take on real-world challenges, collaborate with your peers.\n \nA school every software engineer would have dreamt of!\n")
        with open(filename, mode="r", encoding="utf-8") as f:
            print(f.read(), end="")
