#!/usr/bin/python3
def element_at(my_list, idx):
    for l in my_list:
        if idx > l:
            return None
        elif idx < 0:
            return None
        else:
            return my_list[l]
