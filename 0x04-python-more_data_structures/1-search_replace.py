#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if search not in my_list:
        return my_list
    i = my_list.index(search)
    new = my_list.copy()
    new[i] = replace
    return new
