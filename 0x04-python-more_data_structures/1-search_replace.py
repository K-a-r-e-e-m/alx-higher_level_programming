#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list.copy()
    new[my_list.index(search)] = replace
    return new
