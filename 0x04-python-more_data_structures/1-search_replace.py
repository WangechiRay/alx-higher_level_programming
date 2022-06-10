#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for new_list in my_list:
        if new_list == search:
            my_list[search] = replace
            return my_list
