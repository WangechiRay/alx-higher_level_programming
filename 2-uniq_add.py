#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = sum(sorted(set(my_list)))
    return result
